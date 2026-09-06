# blocks.py

# Importowanie niezbędnych modułów i klas
from block import Block  # Importowanie klasy Block, której będą dziedziczyć wszystkie bloki
from position import Position  # Importowanie klasy Position do reprezentacji pozycji komórek

# Klasa LBlock dziedzicząca po Block (blok w kształcie litery L)
class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)  # Wywołanie konstruktora klasy Block z id = 1 (kolor)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],  # Stan obrotu 0 (forma litery L)
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],  # Stan obrotu 1
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],  # Stan obrotu 2
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]   # Stan obrotu 3
        }
        self.move(0, 3)  # Przesunięcie bloku o (0, 3) na planszy

# Klasa JBlock dziedzicząca po Block (blok w kształcie litery J)
class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)  # Wywołanie konstruktora klasy Block z id = 2 (kolor)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],  # Stan obrotu 0 (forma litery J)
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],  # Stan obrotu 1
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],  # Stan obrotu 2
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]   # Stan obrotu 3
        }
        self.move(0, 3)  # Przesunięcie bloku o (0, 3) na planszy

# Klasa IBlock dziedzicząca po Block (blok w kształcie litery I)
class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)  # Wywołanie konstruktora klasy Block z id = 3 (kolor)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],  # Stan obrotu 0 (forma litery I)
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],  # Stan obrotu 1
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],  # Stan obrotu 2
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]   # Stan obrotu 3
        }
        self.move(-1, 3)  # Przesunięcie bloku o (-1, 3) na planszy (bardziej przesunięty w górę)

# Klasa OBlock dziedzicząca po Block (blok w kształcie kwadratu - O)
class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)  # Wywołanie konstruktora klasy Block z id = 4 (kolor)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]  # Stan obrotu 0 (kwadrat)
        }
        self.move(0, 4)  # Przesunięcie bloku o (0, 4) na planszy

# Klasa SBlock dziedzicząca po Block (blok w kształcie litery S)
class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)  # Wywołanie konstruktora klasy Block z id = 5 (kolor)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],  # Stan obrotu 0 (forma litery S)
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],  # Stan obrotu 1
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],  # Stan obrotu 2
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]   # Stan obrotu 3
        }
        self.move(0, 3)  # Przesunięcie bloku o (0, 3) na planszy

# Klasa TBlock dziedzicząca po Block (blok w kształcie litery T)
class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)  # Wywołanie konstruktora klasy Block z id = 6 (kolor)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],  # Stan obrotu 0 (forma litery T)
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],  # Stan obrotu 1
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],  # Stan obrotu 2
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]   # Stan obrotu 3
        }
        self.move(0, 3)  # Przesunięcie bloku o (0, 3) na planszy

# Klasa ZBlock dziedzicząca po Block (blok w kształcie litery Z)
class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)  # Wywołanie konstruktora klasy Block z id = 7 (kolor)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],  # Stan obrotu 0 (forma litery Z)
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],  # Stan obrotu 1
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],  # Stan obrotu 2
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]   # Stan obrotu 3
        }
        self.move(0, 3)  # Przesunięcie bloku o (0, 3) na planszy
