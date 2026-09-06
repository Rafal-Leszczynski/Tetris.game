# main.py

# Importujemy wymagane biblioteki i pliki
import sys
import pygame
import pickle
from game import Game                   # Serce gry, zawiera logikę gry
from colors import Colors               # Pobieranie kolorów
from main_menu import show_main_menu    # Obsługa menu w grze
import time                             # Będziemy używać time.sleep do opóźnienia na ekranie końcowym

# Załadowanie obrazów do gry z testem
try:
    # Próba załadowania obrazów tła
    game_background = pygame.image.load("game_background.jpg")
    game_background = pygame.transform.scale(game_background, (520, 650))  # Dopasowanie obrazu do rozmiaru ekranu
    menu_background = pygame.image.load("menu_background.jpg")
    menu_background = pygame.transform.scale(menu_background, (520, 650))
    score_background = pygame.image.load("score_background.jpg")
    score_background = pygame.transform.scale(score_background, (520, 650))
    secondary_background = pygame.image.load("secondary_background.jpeg")
    secondary_background = pygame.transform.scale(secondary_background, (520, 650))
except pygame.error as e:
    # Jeśli załadowanie któregoś obrazu nie powiedzie się, program zakończy działanie
    print(f"Załadowanie bądź przeskalowanie któregoś z obrazów było nie możliwe: {e}")
    sys.exit(1)

# Funkcja dodająca wynik i zapisująca tabelę wyników
def add_score_and_save(scores, name, score):
    scores.append((name, score))  # Dodajemy nowy wynik
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]  # Sortowanie wyników po punktach
    save_scores(scores)  # Zapisanie tabeli wyników do pliku
    return scores

# Funkcja wyświetlająca menu wyników
def show_scores_menu(screen, scores, keyboard_click_sound):
    pygame.font.init()
    font = pygame.font.Font(None, 36)  # Czcionka dla wyników
    clock = pygame.time.Clock()

    options = ["Powrót do menu", "Wyczyść tabelę wyników"]
    selected = 0  # Domyślnie wybrana opcja

    while True:
        screen.blit(score_background, (0, 0))  # Ustawienie tła ekranu wyników

        # Wyświetlenie wyników w ramkach
        if scores:
            for i, (name, score) in enumerate(scores):
                score_text = f"{i + 1}. {name} - {score}"

                # Określenie koloru i tła dla wyników na podium
                if i == 0:
                    text_color = (255, 223, 0)  # Złoty
                    bg_color = (50, 50, 20)  # Jaśniejsze tło
                elif i == 1:
                    text_color = (200, 200, 200)  # Srebro
                    bg_color = (50, 50, 50)
                elif i == 2:
                    text_color = (222, 150, 75)  # Brąz
                    bg_color = (60, 40, 20)
                else:
                    text_color = (180, 180, 180)
                    bg_color = (30, 30, 60)

                text_surface = font.render(score_text, True, text_color)
                text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 80 + i * 40))

                # Rysowanie tła dla tekstu
                box_rect = text_rect.inflate(40, 20)
                pygame.draw.rect(screen, bg_color, box_rect, border_radius=6)
                pygame.draw.rect(screen, (100, 100, 100), box_rect, 2, border_radius=6)

                screen.blit(text_surface, text_rect)

        else:
            # Wyświetlenie komunikatu, jeśli brak wyników
            no_scores_text = "BRAK WYNIKÓW"
            no_scores_surface = font.render(no_scores_text, True, (255, 255, 0))
            no_scores_rect = no_scores_surface.get_rect(center=(screen.get_width() // 2, 120))
            box_rect = no_scores_rect.inflate(40, 20)

            # Tło i ramka dla komunikatu
            pygame.draw.rect(screen, (30, 30, 60), box_rect, border_radius=6)
            pygame.draw.rect(screen, (255, 255, 0), box_rect, 2, border_radius=6)
            screen.blit(no_scores_surface, no_scores_rect)

        # Opcje menu (powrót do menu lub wyczyszczenie wyników)
        for i, option in enumerate(options):
            is_selected = i == selected
            text_color = (255, 255, 0) if is_selected else (180, 180, 180)
            border_color = (255, 255, 0) if is_selected else (100, 100, 100)
            fill_color = (30, 30, 60) if is_selected else (0, 0, 0, 0)

            option_surface = font.render(option, True, text_color)
            option_rect = option_surface.get_rect(center=(screen.get_width() // 2, 500 + i * 50))

            # Rysowanie tła i ramki opcji
            box_rect = option_rect.inflate(30, 20)
            pygame.draw.rect(screen, fill_color, box_rect, border_radius=6)
            pygame.draw.rect(screen, border_color, box_rect, 2, border_radius=6)
            screen.blit(option_surface, option_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)  # Przesunięcie w górę
                    keyboard_click_sound.play()
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)  # Przesunięcie w dół
                    keyboard_click_sound.play()
                elif event.key == pygame.K_RETURN:
                    if selected == 0:  # Powrót do menu
                        return scores
                    elif selected == 1:  # Wyczyść tabelę wyników
                        if confirm_clear_scores(screen, keyboard_click_sound, secondary_background):
                            scores = []
                            save_scores(scores)

        clock.tick(30)

# Funkcja potwierdzająca usunięcie wyników
def confirm_clear_scores(screen, keyboard_click_sound, secondary_background):
    pygame.font.init()
    font = pygame.font.Font(None, 40)
    clock = pygame.time.Clock()

    options = ["Tak", "Nie"]  # Możliwość wyboru "Tak" lub "Nie"
    selected = 0

    while True:
        screen.blit(secondary_background, (0, 0))  # Tło dla potwierdzenia
        msg = font.render("Czy na pewno?", True, (255, 255, 255))  # Komunikat do użytkownika
        screen.blit(msg, msg.get_rect(center=(screen.get_width() // 2, 150)))

        for i, option in enumerate(options):
            is_selected = i == selected
            text_color = (255, 255, 0) if is_selected else (200, 200, 200)
            border_color = (255, 255, 0) if is_selected else (100, 100, 100)
            fill_color = (30, 30, 60) if is_selected else (0, 0, 0, 0)

            text_surface = font.render(option, True, text_color)
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 250 + i * 60))
            box_rect = text_rect.inflate(30, 20)

            pygame.draw.rect(screen, fill_color, box_rect, border_radius=6)
            pygame.draw.rect(screen, border_color, box_rect, 2, border_radius=6)
            screen.blit(text_surface, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    keyboard_click_sound.play()
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    keyboard_click_sound.play()
                elif event.key == pygame.K_RETURN:
                    return options[selected] == "Tak"  # Zwraca "True" jeśli użytkownik wybierze "Tak"

        clock.tick(30)

# Funkcja do pobierania nazwy gracza
def get_player_name(screen, keyboard_click_sound, secondary_background):
    pygame.font.init()
    font = pygame.font.Font(None, 40)
    input_box = pygame.Rect(100, 250, 300, 50)  # Okno do wpisania nazwy
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_active
    active = True
    text = ''
    clock = pygame.time.Clock()

    while True:
        screen.blit(secondary_background, (0, 0))  # Tło do wpisywania nazwy
        line1 = font.render("Wpisz nazwę gracza", True, (255, 255, 255))
        line2 = font.render("i naciśnij Enter", True, (255, 255, 255))
        screen.blit(line1, line1.get_rect(center=(screen.get_width() // 2, 160)))
        screen.blit(line2, line2.get_rect(center=(screen.get_width() // 2, 200)))

        # Rysowanie tekstu w oknie
        txt_surface = font.render(text, True, color)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 10))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    keyboard_click_sound.play()
                    if event.key == pygame.K_RETURN:
                        return text.strip() or "Gracz"  # Zwraca nazwę gracza
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 15:
                            text += event.unicode
        clock.tick(30)

# Funkcja odczytująca zawartość pliku (tabela wyników)
def load_scores():
    try:
        with open("scores.pkl", "rb") as f:
            scores = pickle.load(f)
    except (FileNotFoundError, EOFError):
        scores = []  # W przypadku braku pliku lub błędu, zwracamy pustą listę wyników
    return scores

# Funkcja zapisująca tabelę wyników do pliku
def save_scores(scores):
    with open("scores.pkl", "wb") as f:
        pickle.dump(scores, f)

#Funkcja mająca za zadanie operować komunikatem o przegraniu, pauzie, etc.
def show_game_over_screen(screen, game_background, game_over_surface, game_over_rect, game, score_surface, next_surface, title_font, score_rect, next_rect):
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < 3000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(game_background, (0, 0))

        # Rysowanie standardowych elementów interfejsu
        score_value_surface = title_font.render(str(game.score), True, Colors.white)
        screen.blit(score_surface, (365, 20))
        screen.blit(next_surface, (365, 180))
        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))


        # Rysujemy aktualny stan planszy i ekran "Przegrałeś"
        game.draw(screen)
        # Czarne tło za napisem
        box_rect = game_over_rect.inflate(40, 20)
        pygame.draw.rect(screen, (0, 0, 0), box_rect, border_radius=6)
        pygame.draw.rect(screen, (100, 100, 100), box_rect, 2, border_radius=6)
        screen.blit(game_over_surface, game_over_rect)

        pygame.display.update()
        clock.tick(60)

# Funkcja główna programu
def main():
    pygame.init()
    pygame.mixer.init()
    keyboard_click_sound = pygame.mixer.Sound("keyboard_click.mp3")
    keyboard_click_sound.set_volume(0.5)

    # Załadowanie muzyki
    pygame.mixer.music.load("game_music_tetris.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    # Inicjalizacja okna gry
    screen = pygame.display.set_mode((520, 650))
    pygame.display.set_caption("Python Tetris")
    clock = pygame.time.Clock()

    # Czcionki na ekranie gry
    title_font = pygame.font.Font(None, 40)
    over_font = pygame.font.Font(None, 60)
    score_surface = title_font.render("Wynik", True, Colors.white)
    next_surface = title_font.render("Kolejny", True, Colors.white)
    game_over_surface = over_font.render("Przegrałeś", True, Colors.white)
    game_over_rect = game_over_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    score_rect = pygame.Rect(340, 55, 170, 60)
    next_rect = pygame.Rect(340, 215, 170, 180)
    scores = load_scores()

    while True:
        # Wyświetlenie menu głównego
        option = show_main_menu(screen, menu_background)
        if option == 1:
            # Opcja rozpoczęcia gry
            player_name = get_player_name(screen, keyboard_click_sound, secondary_background)
            game = Game()  # Tworzymy nową grę
            GAME_UPDATE = pygame.USEREVENT
            pygame.time.set_timer(GAME_UPDATE, 200)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if game.game_over:
                            game.game_over = False
                            game.reset()
                        if event.key == pygame.K_LEFT and not game.game_over:
                            game.move_left()
                        if event.key == pygame.K_RIGHT and not game.game_over:
                            game.move_right()
                        if event.key == pygame.K_DOWN and not game.game_over:
                            game.move_down()
                            game.update_score(0, 1)
                        if event.key == pygame.K_UP and not game.game_over:
                            game.rotate()
                    if event.type == GAME_UPDATE and not game.game_over:
                        game.move_down()

                # Zmieniamy tło na obrazek
                screen.blit(game_background, (0, 0))

                # Rysujemy wynik gry
                score_value_surface = title_font.render(str(game.score), True, Colors.white)

                screen.blit(score_surface, (365, 20))
                screen.blit(next_surface, (365, 180))
                if game.game_over:
                    # Tło i ramka dla napisu "Przegrałeś"
                    box_rect = game_over_rect.inflate(40, 20)
                    pygame.draw.rect(screen, (0, 0, 0), box_rect, border_radius=6)  # Czarne tło
                    pygame.draw.rect(screen, (100, 100, 100), box_rect, 2, border_radius=6)  # Szara ramka
                    screen.blit(game_over_surface, game_over_rect)

                pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
                screen.blit(score_value_surface,
                            score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
                pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
                game.draw(screen)

                pygame.display.update()
                clock.tick(60)

                if game.game_over:
                    # Dźwięk końca gry
                    pygame.mixer.Sound("game_over_arcade.mp3").play()
                    show_game_over_screen(screen, game_background, game_over_surface, game_over_rect, game,
                                          score_surface, next_surface, title_font, score_rect, next_rect)
                    print(f"\nGra zakończona! {player_name} - Wynik: {game.score}")
                    scores = add_score_and_save(scores, player_name, game.score)
                    break

        elif option == 2:
            # Wyświetlanie tabeli wyników
            scores = load_scores()  # Odświeżenie danych z pliku
            scores = show_scores_menu(screen, scores, keyboard_click_sound)
            save_scores(scores)  # Zapisanie zmian

        elif option == 3:
            # Zakończenie gry
            print("Dziękujemy za grę! Do zobaczenia!")
            pygame.quit()
            sys.exit()

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()

