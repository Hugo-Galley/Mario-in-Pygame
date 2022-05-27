import pygame
from game import Game

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
FPS = 60

# creer la fenêtre
pygame.display.set_caption("Mario vs Goumba")
screen = pygame.display.set_mode((933, 600))
pygame_icon = pygame.image.load('assets/Images/icone.png')
pygame.display.set_icon(pygame_icon)

# creer les backgrounds
background = pygame.image.load('assets/Images/backgrounds/bg.png')
background_level2 = pygame.image.load('assets/Images/backgrounds/background_level2 (1).jpg')
background_level3 = pygame.image.load('assets/Images/backgrounds/background_level3 .jpg')
win_background = pygame.image.load('assets/Images/backgrounds/win-(1).jpeg')
loose_background = pygame.image.load('assets/Images/backgrounds/gameover (1).jpg')
font = pygame.image.load('assets/Images/font.png')
font_menu = pygame.image.load('assets/Images/font_image(1).png')

# charger nos boutons
play_button = pygame.image.load('assets/Images/buttons/play_button.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = 350
play_button_rect.y = 150

replay_button = pygame.image.load('assets/Images/buttons/replay_button.png')
replay_button_rect = replay_button.get_rect()
replay_button_rect.x = 350
replay_button_rect.y = 250

exit_button = pygame.image.load('assets/Images/buttons/exit_button.png')
exit_button_rect = exit_button.get_rect()
exit_button_rect.x = 350
exit_button_rect.y = 340

level_1 = pygame.image.load('assets/Images/buttons/sign.png')
level_1_rect = level_1.get_rect()
level_1_rect.x = 220
level_1_rect.y = 373

level_2 = pygame.image.load('assets/Images/buttons/level.png')
level_2_rect = level_2.get_rect()
level_2_rect.x = 380
level_2_rect.y = 373

level_3 = pygame.image.load('assets/Images/buttons/sign(1).png')
level_3_rect = level_3.get_rect()
level_3_rect.x = 530
level_3_rect.y = 373

# charger notre jeu
game = Game()

running = True
game.game_state = 1

while running:
    if game.is_playing:

        if game.game_state == 1:

            # afficher le background sur l'écran
            if game.lvl == 1:
                screen.blit(background, (0, 0))
            elif game.lvl == 2:
                screen.blit(background_level2, (0, -35))
            elif game.lvl == 3:
                screen.blit(background_level3, (0, 0))
            screen.blit(font, (200, 0))

            if game.is_paused:

                game.pause_menu(screen)

                # afficher les boutons sur l'écran
                screen.blit(play_button, play_button_rect)
                screen.blit(replay_button, replay_button_rect)
                screen.blit(exit_button, exit_button_rect)

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()

                    # si la souris est cliqué
                    elif event.type == pygame.MOUSEBUTTONDOWN:

                        # verification pour savoir si la souris est en collision avec un bouton
                        if play_button_rect.collidepoint(event.pos):
                            # relancé le jeu
                            game.is_paused = False
                            pygame.mixer.music.unpause()

                        elif replay_button_rect.collidepoint(event.pos):
                            # recommencé la partie
                            game.remove_sprite()
                            game.start()

                        elif exit_button_rect.collidepoint(event.pos):
                            # retourné au menu
                            game.is_playing = False
                            game.is_paused = False
                            game.remove_sprite()
                            game.stop_music()

            else:

                # vérifier les interraction du joueur avec le jeux
                game.update(screen)

                for event in pygame.event.get():

                    # si le joueur quitte la fenêtre
                    if event.type == pygame.QUIT:
                        # on coupe le jeux
                        running = False
                        pygame.quit()

                    # detecter si un joueur presse une touche du clavier
                    elif event.type == pygame.KEYDOWN:
                        game.pressed[event.key] = True

                        # detecter si la touche espace est enclenchée pour lancer notre projectile
                        if event.key == pygame.K_SPACE:
                            game.player.launch_projectile()

                        # detecter si la touche k est enclenchée pour lancer notre projectile
                        if event.key == pygame.K_h or event.key == pygame.K_a or event.key == pygame.K_k:
                            game.player.launch_projectile(True)

                    # detecter si un joueur lache une touche du clavier
                    elif event.type == pygame.KEYUP:
                        game.pressed[event.key] = False

        elif game.game_state == 0:

            # charger le background sur l'écran
            screen.blit(win_background, (0, 0))
            # vérifier les interractions avec la fenêtre
            game.scene_update()

        elif game.game_state == 2:

            # charger le background sur l'écran
            screen.blit(loose_background, (0, 0))
            # vérifier les interractions avec la fenêtre
            game.scene_update()
    else:
        screen.blit(background, (0, 0))
        screen.blit(level_1, level_1_rect)
        screen.blit(level_2, level_2_rect)
        screen.blit(level_3, level_3_rect)
        screen.blit(font_menu, (16, 20))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # si la souris est cliqué
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if level_1_rect.collidepoint(event.pos):
                # relancé le jeu
                game.lvl = 1
                game.start()

            elif level_2_rect.collidepoint(event.pos):
                game.lvl = 2
                game.start()

            elif level_3_rect.collidepoint(event.pos):
                game.lvl = 3
                game.start()

    # vérifier que le jeu est toujours en marche avant d'update l'écran pour éviter les erreurs
    if running:
        pygame.display.flip()

    clock.tick(FPS)
