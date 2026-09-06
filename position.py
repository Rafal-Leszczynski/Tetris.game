# position.py

# Klasa Position reprezentująca pozycję komórki w grze, zawierającą wiersz (row) i kolumnę (column)
class Position:
    # Konstruktor klasy Position, który inicjalizuje pozycję na podstawie numeru wiersza i kolumny
    def __init__(self, row, column):
        self.row = row  # Numer wiersza, w którym znajduje się komórka
        self.column = column  # Numer kolumny, w którym znajduje się komórka
