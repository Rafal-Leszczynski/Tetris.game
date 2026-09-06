# main_menu.py

# Importowanie pygame oraz sys do zarządzania ekranem i systemem
import pygame
import sys

# Funkcja wyświetlająca główne menu gry
def show_main_menu(screen, background):
    # Inicjalizacja czcionek w pygame
    pygame.font.init()
    font = pygame.font.Font(None, 35)  # Ustawienie czcionki dla tekstu w menu
    menu_items = ["Start gry", "Tabela wyników", "Wyjście"]  # Lista opcji menu
    selected_index = 0  # Indeks wybranej opcji (domyślnie pierwsza)
    clock = pygame.time.Clock()  # Ustawienie zegara do kontrolowania liczby klatek na sekundę

    # Załadowanie dźwięku kliknięcia klawisza (używane przy nawigacji po menu)
    keyboard_click = pygame.mixer.Sound("keyboard_click.mp3")
    keyboard_click.set_volume(0.5)  # Ustawienie głośności dźwięku na 50%

    # Pętla główna menu, która będzie działać aż użytkownik podejmie decyzję
    while True:
        # Rysowanie tła (background) na ekranie
        screen.blit(background, (0, 0))

        # Rysowanie każdej z opcji menu
        for i, item in enumerate(menu_items):
            # Sprawdzenie, czy ta opcja jest aktualnie wybrana
            is_selected = i == selected_index
            # Ustalenie koloru tekstu i ramki w zależności od tego, czy opcja jest wybrana
            text_color = (255, 255, 0) if is_selected else (255, 255, 255)  # Żółty kolor dla wybranej opcji
            border_color = (255, 255, 0) if is_selected else (180, 180, 180)  # Jasnoszary dla niewybranych
            fill_color = (30, 30, 60) if is_selected else (0, 0, 0, 0)  # Tło wybranej opcji (ciemne)

            # Renderowanie tekstu z użyciem czcionki
            label = font.render(item, True, text_color)
            # Ustalenie pozycji tekstu na ekranie (na środku)
            text_rect = label.get_rect(center=(screen.get_width() // 2, 250 + i * 60))
            # Rozszerzenie prostokąta na potrzeby tła i ramki
            box_rect = text_rect.inflate(30, 20)

            # Rysowanie tła dla opcji (wypełnienie prostokąta)
            pygame.draw.rect(screen, fill_color, box_rect, border_radius=10)
            # Rysowanie ramki wokół tekstu (z zaokrąglonymi rogami)
            pygame.draw.rect(screen, border_color, box_rect, 2, border_radius=10)
            # Rysowanie samego tekstu na ekranie
            screen.blit(label, text_rect)

        # Aktualizacja ekranu
        pygame.display.update()

        # Obsługa zdarzeń (np. naciśnięcie klawisza lub zamknięcie okna)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Zamyka pygame
                sys.exit()  # Zamyka aplikację
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:  # Przesunięcie wyboru w dół
                    selected_index = (selected_index + 1) % len(menu_items)
                    keyboard_click.play()  # Odtwarzanie dźwięku kliknięcia
                elif event.key == pygame.K_UP:  # Przesunięcie wyboru w górę
                    selected_index = (selected_index - 1) % len(menu_items)
                    keyboard_click.play()  # Odtwarzanie dźwięku kliknięcia
                elif event.key == pygame.K_RETURN:  # Naciśnięcie Enter - wybór opcji
                    keyboard_click.play()  # Odtwarzanie dźwięku kliknięcia
                    return selected_index + 1  # Zwrócenie wybranego indeksu (dodajemy 1, bo zaczynamy od 0)

        # Kontrolowanie liczby klatek na sekundę (60 FPS)
        clock.tick(60)
