import pygame

import animation
from projectiles import *


class Player(animation.AnimateSprite):

    def __init__(self, game, sprite_name, image_number=0, have_animation=False):
        super().__init__(sprite_name, image_number)
        self.game = game
        self.velocity = 5
        self.have_animation = have_animation
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.is_flip = False

    def launch_projectile(self, cheat_on=False):
        # crée une nouvelle instance de la classe projectile
        if cheat_on:
            projectile = Knife(self)
            projectile.sound.play()
            return self.all_projectiles.add(projectile)

        projectile = FireBall(self)
        projectile.sound.play()
        self.all_projectiles.add(projectile)

    def update_animation(self):
        if self.have_animation:
            self.animate(flip=self.is_flip)

    def move_right(self):

        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
            self.start_animation()
            self.is_flip = False

    def move_left(self):
        self.rect.x -= self.velocity
        self.start_animation()
        self.is_flip = True


class Mario(Player):

    def __init__(self, game):
        super().__init__(game, "mario2", image_number=3, have_animation=True)
        self.rect.y = 425


class Luigi(Player):

    def __init__(self, game):
        super().__init__(game, "luigi", image_number=3, have_animation=True)
        self.rect.y = 415


class Toad(Player):

    def __init__(self, game):
        super().__init__(game, "toad")
        self.rect.y = 430

class Waluigi(Player):

    def __init__(self,game):
        super().__init__(game, "waluigi")
        self.rect.y = 450

class Wario(Player):

    def __init__(self,game):
        super().__init__(game, "wario")
        self.rect.y = 450
