# importation de bibliotèque
import random
import pygame

from monsters import *
from player import *


class Game:

    # initialisation des composants de l'objet
    def __init__(self):
        self.game_state = 1
        self.is_paused = False
        self.is_playing = False
        self.music_play = False
        self.lvl = 1
        self.all_players = pygame.sprite.Group()
        self.player = Mario(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.kill = 1
        self.kill_init = 1
        self.credit = False
        self.choice_player = 1
        self.menu_perso = False


    def pause_menu(self, screen):
        # Applliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # dessiné à l'écran les ennemis et projectiles
        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)

    # supprime tout les sprites à l'écran (sauf le joueur)
    def remove_sprite(self):

        self.all_monsters = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()

    # lance la musique
    def start_music(self):
        playlist = list()
        playlist.extend(["assets/Musics/win_background_Music.mp3", "assets/Musics/background_Music.mp3", "assets/Musics/loose_background_music.mp3"])
        pygame.mixer.music.load(playlist[self.game_state])
        pygame.mixer.music.play()
        self.music_play = True

    # arrête la musique
    def stop_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        self.music_play = False

    # lance le jeux avec les paramètres par défault
    def start(self):
        self.is_paused = False
        self.is_playing = True
        self.game_state = 1
        self.stop_music()
        self.kill = self.kill_init
        self.pressed = {}
        self.player.rect.x = 0
        self.spawn_monster()
        if self.choice_player == 1:
            self.player = Mario(self)
<<<<<<< HEAD

        elif self.choice_player == 2:
=======
            print("joueur 1")
        else:
>>>>>>> 1e69ec88523d6405be1d62f77847209fe46f7267
            self.player = Toad(self)

        elif self.choice_player == 3:
            self.player = Waluigi(self)
            self.player.rect.y -= 23

        elif self.choice_player == 4:
            self.player = Wario(self)
            self.player.rect.y -= 20

        elif self.choice_player == 5:
            self.player = Luigi(self)




    # vérifie les interractions avec le jeu
    def update(self, screen):
        # Applliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actiualiser l'animation du joueur
        self.player.update_animation()

        # Faire bouger les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # faire bouger les ennemis
        for monster in self.all_monsters:

            if monster.is_alive:
                monster.forward()
                monster.update_animation()

            else:
                monster.sound_status()

        # dessiné à l'écran les ennemis et projectiles
        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)

        # lancer la musique
        if not self.music_play:
            self.start_music()

        # verifier si le joueur veut aller gauche ou droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        # vérifie si le joueur veut mettre le jeu en pause
        if self.pressed.get(pygame.K_ESCAPE):
            self.is_paused = True
            self.pressed = {}
            pygame.mixer.music.pause()

        # condition de défaite
        if self.check_collision(self.player, self.all_monsters):

            self.remove_sprite()
            self.game_state = 2
            self.stop_music()

        # condition de victoire
        if self.kill >= 16:

            self.remove_sprite()
            self.game_state = 0
            self.stop_music()

    # vérifie les interractions avec la fenêtre quand le jeu est arrêté (dans l'état gagné ou perdu)
    def scene_update(self):

        if not self.music_play:
            self.start_music()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.is_playing = False
                self.remove_sprite()
                self.stop_music()

    # vérifie les collisions
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # fait apparaître un ennemi
    def spawn_monster(self):
        if self.kill <= 5:
            for i in range(self.kill):
                monster = Goomba(self)
                monster2 = BobOmb(self)
                monster3 = Koopa(self)
                liste = [monster, monster2, monster3]
                self.all_monsters.add(random.choice(liste))
