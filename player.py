import pygame

import animation
from projectiles import *


class Player(animation.AnimateSprite):

    def __init__(self, game, sprite_name):
        super().__init__(sprite_name)
        self.game = game
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 0

    def launch_projectile(self, cheat_on=False):
        # crée une nouvelle instance de la classe projectile
        if cheat_on:
            projectile = Knife(self)
            projectile.sound.play()
            return self.all_projectiles.add(projectile)

        projectile = FireBall(self)
        projectile.sound.play()
        self.all_projectiles.add(projectile)

    def move_right(self):

        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity


class Mario(Player):

    def __init__(self, game):
        super().__init__(game, "mario")
        self.rect.y = 450


class Toad(Player):

    def __init__(self, game):
        super().__init__(game, "toad")
        self.rect.y = 430
