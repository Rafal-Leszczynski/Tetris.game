# block.py

# Importowanie niezbędnych modułów i klas
from colors import Colors  # Importowanie klasy Colors do uzyskania kolorów komórek
import pygame  # Moduł Pygame do rysowania obiektów na ekranie
from position import Position  # Importowanie klasy Position do przechowywania pozycji komórek

# Definicja klasy Block (blok)
class Block:
    def __init__(self, id):
        # Inicjalizacja obiektu Block z unikalnym identyfikatorem
        self.id = id
        self.cells = {}  # Słownik komórek dla różnych stanów obrotu
        self.cell_size = 30  # Rozmiar pojedynczej komórki (w pikselach)
        self.row_offset = 0  # Przesunięcie wierszy, początkowo 0
        self.column_offset = 0  # Przesunięcie kolumn, początkowo 0
        self.rotation_state = 0  # Stan obrotu (0 oznacza początkowy stan)
        self.colors = Colors.get_cell_colors()  # Pobranie kolorów komórek z klasy Colors

    def move(self, rows, columns):
        # Funkcja przesuwająca blok o określoną liczbę wierszy i kolumn
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_position(self):
        # Funkcja zwracająca pozycje komórek w aktualnym stanie obrotu
        tiles = self.cells[self.rotation_state]  # Pobierz odpowiednie komórki na podstawie stanu obrotu
        moved_tiles = []  # Lista pozycji po przesunięciu bloku

        # Iterowanie przez pozycje komórek i dodanie przesunięcia w wierszach i kolumnach
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)

        return moved_tiles  # Zwracamy przesunięte pozycje komórek

    def rotate(self):
        # Funkcja obracająca blok w prawo (zmiana stanu obrotu)
        self.rotation_state += 1  # Zwiększamy stan obrotu
        if self.rotation_state == len(self.cells):  # Jeśli stan obrotu przekroczy liczbę dostępnych obrotów
            self.rotation_state = 0  # Zresetuj do pierwszego stanu obrotu

    def undo_rotation(self):
        # Funkcja cofająca obrót (obrót w lewo)
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1  # Jeśli obecny stan to pierwszy, ustaw na ostatni
        else:
            self.rotation_state -= 1  # W przeciwnym razie, przejdź do poprzedniego stanu obrotu

    def draw(self, screen, offset_x, offset_y):
        # Funkcja rysująca blok na ekranie
        tiles = self.get_cell_position()  # Pobierz pozycje komórek po uwzględnieniu przesunięć

        # Rysowanie każdej komórki w odpowiednim miejscu
        for tile in tiles:
            # Tworzymy prostokąt (rect) dla każdej komórki na podstawie jej pozycji
            tile_rect = pygame.Rect(
                offset_x + tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size,
                self.cell_size - 1,  # Rozmiar komórki (odjęcie 1 pikselu dla odstępu między komórkami)
                self.cell_size - 1
            )

            # Rysujemy prostokąt w odpowiednim kolorze
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
