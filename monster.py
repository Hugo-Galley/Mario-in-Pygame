from random import randint

import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/Images/sprites/goomba.png')
        self.rect = self.image.get_rect()
        self.rect.x = 720 + randint(0, 20)
        self.rect.y = 400
        self.velocity_init = 1
        self.velocity = randint(self.velocity_init,self.velocity_init + 3)
        self.touch = 0

    # supprime un monstre
    def remove(self):
        self.game.all_monsters.remove(self)
        self.game.kill += 1
        self.game.spawn_monster()

    # fait avancer un monstre
    def forward(self):

        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity