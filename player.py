import pygame

from projectile import Projectile
from projectile2 import Projectile2


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/Images/sprites/mario.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 450

    # lance le projectile
    def launch_projectile(self):
        # crée une nouvelle instance de la classe projectile
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    # Code triche
    def cheat(self):
        projectile = Projectile2(self)
        self.all_projectiles.add(projectile)

    # Deplacement du joueur
    def move_right(self):

        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity