# grid.py

# Importowanie modułu pygame do rysowania oraz Colors, który zawiera kolory komórek
import pygame
from colors import Colors

# Klasa Grid zarządza planszą gry oraz wszystkimi operacjami związanymi z komórkami
class Grid:
    def __init__(self):
        # Ustawienia planszy gry: liczba wierszy (20) i kolumn (10), rozmiar komórek (30px)
        self.num_rows = 20  # Liczba wierszy na planszy
        self.num_cols = 10  # Liczba kolumn na planszy
        self.cell_size = 30  # Rozmiar pojedynczej komórki
        # Inicjalizacja pustej planszy - 2D lista, która przechowuje wartości komórek
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        # Pobranie kolorów dla komórek z klasy Colors
        self.colors = Colors.get_cell_colors()

        # Ładowanie dźwięków: dźwięk usunięcia linii, dźwięk "wow" oraz dźwięk kliknięcia
        self.clear_sound = pygame.mixer.Sound("clear.wav")
        self.clear_sound.set_volume(0.5)

        self.wow_sound = pygame.mixer.Sound("wow.mp3")  # Dźwięk 'wow' przy zniszczeniu wielu rzędów
        self.keyboard_click_sound = pygame.mixer.Sound("keyboard_click.mp3")  # Dźwięk kliknięcia w menu

        # Początkowe punkty gry (zerowe na początku)
        self.score = 0

    # Funkcja sprawdzająca pełne linie i usuwająca je
    def clear_full_rows(self):
        completed = 0  # Zmienna do liczenia liczby usuniętych pełnych rzędów
        # Sprawdzanie każdego wiersza od dołu do góry
        for row in range(self.num_rows - 1, -1, -1):
            # Jeśli wiersz jest pełny, usuń go
            if self.is_row_full(row):
                self.clear_row(row)  # Usuwamy wiersz
                self.clear_sound.play()  # Odtwarzamy dźwięk 'clear'
                completed += 1  # Zwiększamy liczbę usuniętych rzędów
            # Jeśli już usunięto jakieś rzędy, przesuwamy wiersze w dół
            elif completed > 0:
                self.move_row_down(row, completed)

        # Jeśli zniszczono więcej niż 2 rzędy, odtwarzamy dźwięk 'wow'
        if completed > 2:
            self.wow_sound.play()

        # Zwrócenie liczby usuniętych linii
        return completed

    # Funkcja resetująca planszę - wszystkie komórki ustawiamy na 0
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    # Funkcja rysująca planszę na ekranie
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]  # Pobranie wartości komórki (0 - pusta, inne - zajęta)
                # Ustawienie prostokąta dla każdej komórki i jej kolor
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11, self.cell_size - 1,
                                        self.cell_size - 1)
                # Rysowanie prostokąta na ekranie w odpowiednim kolorze
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    # Funkcja wypisująca planszę w konsoli (przydatne do debugowania)
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    # Funkcja sprawdzająca, czy komórka znajduje się w obrębie planszy
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    # Funkcja sprawdzająca, czy komórka jest pusta
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    # Funkcja sprawdzająca, czy wiersz jest pełny (wszystkie komórki zajęte)
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:  # Jeśli znajdziemy pustą komórkę, wiersz nie jest pełny
                return False
        return True

    # Funkcja usuwająca pełny wiersz (wszystkie komórki w wierszu ustawiamy na 0)
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    # Funkcja przesuwająca wiersz w dół, aby zrobić miejsce po usunięciu wiersza
    def move_row_down(self, row, num_rows):
        # Przesuwanie wszystkich komórek w wierszu w dół o 'num_rows' wierszy
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0  # Czyszczenie oryginalnej komórki
