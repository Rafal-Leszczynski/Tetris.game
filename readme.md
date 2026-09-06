# Klasyczna Gra TETRIS w języku Python

Projekt akademicki przedstawiający implementację klasycznej gry Tetris z wykorzystaniem programowania obiektowego (OOP), zasad SOLID oraz wzorców projektowych.

## Członkowie zespołu		indeksy
*   Rafał Leszczyński	 	(56050)
*   Mateusz Jurgielewicz 	(56013)
*   Patryk Dańda 		(59704)

---

## Prawa autorskie / Copyright License

**Wszelkie prawa zastrzeżone / All rights reserved**

Kod źródłowy oraz assety zawarte w tym repozytorium stanowią własność intelektualną autorów projektu.
* Udostępniamy ten projekt **wyłącznie do wglądu dla rekruterów** w ramach procesów rekrutacyjnych.
* Kopiowanie, rozpowszechnianie, modyfikowanie, wykorzystywanie kodu (zarówno w celach prywatnych, komercyjnych, jak i akademickich) bez wyraźnej, pisemnej zgody autorów jest **surowo zabronione**.

---

## Opis projektu
Projekt to w pełni funkcjonalna implementacja gry Tetris posiadająca:
* Interfejs graficzny oparty na bibliotece **Pygame**.
* Precyzyjną logikę kolizji i rotacji klocków.
* Dynamiczny system punktacji zależny od ilości jednocześnie zbijanych linii.
* Dopasowaną do dynamiki rozgrywki oprawę dźwiękową.
* System zapisu wyników w tabeli **TOP-10** wraz z opcją resetowania bazy danych.

## Użyte technologie
* **Python 3**
* **Biblioteki:**
  * `Pygame` – obsługa grafiki, audio, logiki i zdarzeń w czasie rzeczywistym.
  * `Sys` – prawidłowe i bezpieczne zamykanie procesów gry.
  * `Pickle` – serializacja danych, odpowiada za trwały zapis tabeli wyników.

---

## Architektura i Wzorce Projektowe

### Programowanie Obiektowe & SOLID
Logika programu została podzielona na odrębne klasy o jasnych, pojedynczych odpowiedzialnościach, zgodnie z paradygmatem OOP oraz wytycznymi SOLID.

### Zastosowane Wzorce Projektowe
* **Singleton:** Zastosowany do zarządzania pojedynczą instancją obiektu zarządzającego stanem gry (`Game`). Ujednolica to dostęp do bieżących danych gry z każdego miejsca w kodzie i upraszcza sterowanie.
* **Obserwator (Uproszczony):** Gra regularnie odświeża stan, nasłuchując i reagując na zdarzenia zachodzące w czasie (np. kolizje z podłożem, interakcja użytkownika z klawiaturą).

---

## Struktura kodu

```text
PROJEKT_TETRIS/
├── main.py        # Uruchamia grę, obsługuje główną pętlę oraz operacje wejścia/wyjścia (zapis/odczyt plików, czyszczenie TOP-10, ładowanie assetów).
├── main_menu.py   # Menu główne gry (start, obsługa tablicy wyników, wyjście).
├── game.py        # Menedżer przebiegu gry (logika i stan poziomu).
├── grid.py        # Klasa Grid – plansza gry (siatka, kolizje, usuwanie linii, rysowanie).
├── block.py       # Klasa Block – pojedynczy klocek (pozycja, rotacja, kolor).
├── blocks.py      # Zbiór typów klocków (definicje kształtów i ich rotacji).
├── position.py    # Klasa Position – operacje na współrzędnych klocków.
└── colors.py      # Definicje palety kolorów używanych w interfejsie.
```

---

## Instrukcja uruchomienia

1. Upewnij się, że posiadasz zainstalowane środowisko Python 3.
2. Zainstaluj wymaganą edycję biblioteki:
   ```bash
   pip install pygame-ce
   ```
3. Uruchom grę komendą:
   ```bash
   python main.py
   ```

---

## Źródła zasobów (Credits)
Wspieraliśmy się oprogramowaniem do tworzenia ilustracji AI – **Gencraft**. Efekty dźwiękowe pochodzą z serwisów **Pixabay** oraz **Freesound**.
