# game.py

# Importowanie wymaganych modułów: Grid, Blocks, random (losowanie bloków) oraz pygame do obsługi grafiki i dźwięku
from grid import Grid
from blocks import *
import random
import pygame

# Inicjalizacja miksera dźwiękowego Pygame
pygame.mixer.init()

# Wczytanie dźwięku obrotu, który będzie odtwarzany przy rotacji bloków
rotate_sound = pygame.mixer.Sound("rotate.wav")

# Klasa gry (Game) zarządzająca logiką gry Tetris
class Game:
    def __init__(self):
        # Inicjalizacja obiektu gry
        self.grid = Grid()  # Tworzenie planszy gry
        # Lista dostępnych typów bloków w grze (I, J, L, O, S, T, Z)
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_blocks()  # Losowanie pierwszego bloku
        self.next_block = self.get_random_blocks()  # Losowanie bloku, który pojawi się następny
        self.game_over = False  # Flaga informująca o zakończeniu gry
        self.score = 0  # Inicjalizacja punktów gry

    # Funkcja aktualizująca wynik na podstawie usuniętych linii i punktów za ruch w dół
    def update_score(self, lines_cleared, move_down_points):
        # Wczytanie dźwięku "kasy" (reakcja na przekroczenie progu punktowego)
        self.cash_register = pygame.mixer.Sound("cash_register.mp3")
        self.cash_register.set_volume(0.5)  # Ustalenie głośności dźwięku

        previous_score = self.score  # Przechowanie poprzedniego wyniku

        # Słownik z punktami za usunięte linie
        points_dict = {1: 50, 2: 120, 3: 250, 4: 350, 5: 500}
        # Dodawanie punktów za usunięte linie
        self.score += points_dict.get(lines_cleared, 0)

        # Dodawanie punktów za ruch w dół
        self.score += move_down_points

        # Sprawdzanie, czy gracz przekroczył próg 1000 punktów, aby zagrać dźwięk
        if (previous_score // 1000) < (self.score // 1000):
            self.cash_register.play()

    # Funkcja losująca blok z dostępnej listy
    def get_random_blocks(self):
        # Jeśli lista bloków jest pusta, uzupełniamy ją ponownie
        if not self.blocks:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)  # Wybór losowego bloku
        self.blocks.remove(block)  # Usunięcie wybranego bloku z listy
        return block

    # Funkcja przesuwająca blok w lewo
    def move_left(self):
        self.current_block.move(0, -1)
        # Sprawdzanie, czy blok mieści się na planszy
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)  # Jeśli nie, cofa blok

    # Funkcja przesuwająca blok w prawo
    def move_right(self):
        self.current_block.move(0, 1)
        # Sprawdzanie, czy blok mieści się na planszy
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)  # Jeśli nie, cofa blok

    # Funkcja przesuwająca blok w dół
    def move_down(self):
        self.current_block.move(1, 0)
        # Sprawdzanie, czy blok mieści się na planszy
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)  # Jeśli nie, cofa blok
            self.lock_block()  # Zatrzymanie bloku na swojej pozycji

    # Funkcja blokująca blok na planszy po jego upadku
    def lock_block(self):
        tiles = self.current_block.get_cell_position()  # Pobranie pozycji komórek bloku
        # Zablokowanie każdej komórki bloku na odpowiednich pozycjach w siatce
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        # Zmiana bieżącego bloku na następny
        self.current_block = self.next_block
        self.next_block = self.get_random_blocks()  # Losowanie nowego następnego bloku
        rows_cleared = self.grid.clear_full_rows()  # Sprawdzanie, czy linie zostały usunięte
        self.update_score(rows_cleared, 0)  # Aktualizacja wyniku
        if self.block_fits() == False:  # Sprawdzanie, czy nowy blok może się zmieścić
            self.game_over = True  # Zakończenie gry, jeśli blok się nie mieści

    # Funkcja resetująca stan gry
    def reset(self):
        self.grid.reset()  # Resetowanie planszy
        # Przywrócenie początkowych bloków
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_blocks()  # Losowanie nowego bloku
        self.next_block = self.get_random_blocks()  # Losowanie nowego następnego bloku
        self.score = 0  # Resetowanie punktów

    # Funkcja sprawdzająca, czy blok mieści się w siatce
    def block_fits(self):
        tiles = self.current_block.get_cell_position()  # Pobranie pozycji komórek bloku
        # Sprawdzanie, czy którakolwiek z komórek bloku nie znajduje się wypełnionym miejscu
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    # Funkcja obracająca blok
    def rotate(self):
        self.current_block.rotate()  # Obracanie bloku
        rotate_sound.play()  # Odtwarzanie dźwięku obrotu
        # Sprawdzanie, czy po obrocie blok mieści się w planszy i nie zachodzi na inne bloki
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()  # Cofnięcie obrotu, jeśli blok nie pasuje

    # Funkcja sprawdzająca, czy blok mieści się w obrębie planszy
    def block_inside(self):
        tiles = self.current_block.get_cell_position()  # Pobranie pozycji komórek bloku
        # Sprawdzanie, czy którakolwiek komórka nie wychodzi poza planszę
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    # Funkcja rysująca planszę i bieżący blok na ekranie
    def draw(self, screen):
        self.grid.draw(screen)  # Rysowanie planszy
        self.current_block.draw(screen, 11, 11)  # Rysowanie bieżącego bloku

        # Rysowanie bloku, który pojawi się następny
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
