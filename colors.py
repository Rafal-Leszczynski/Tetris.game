# colors.py

# Klasa Colors, która zawiera definicje kolorów używanych w grze
class Colors:
    # Definicje kolorów w formacie RGB
    dark_gray = (26, 31, 40)  # Szary kolor
    green = (47, 230, 23)  # Zielony kolor
    red = (232, 18, 18)  # Czerwony kolor
    orange = (226, 116, 17)  # Pomarańczowy kolor
    yellow = (237, 234, 4)  # Żółty kolor
    purple = (166, 0, 247)  # Fioletowy kolor
    cyan = (21, 204, 209)  # Cyjanowy kolor
    blue = (13, 64, 216)  # Niebieski kolor
    white = (255, 255, 255)  # Biały kolor
    dark_blue = (44, 44, 127)  # Ciemnoniebieski kolor
    light_blue = (59, 85, 162)  # Jasnoniebieski kolor

    # Metoda klasy, która zwraca listę kolorów, które będą używane do wypełniania komórek bloków
    @classmethod
    def get_cell_colors(cls):
        # Zwraca listę kolorów w kolejności od dark_gray do blue
        return [cls.dark_gray, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
