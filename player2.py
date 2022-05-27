import pygame

import projectiles
from projectiles import *


class Player2(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/Images/sprites/toad.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 430

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