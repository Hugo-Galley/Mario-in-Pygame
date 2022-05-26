import pygame
from random import randint


class Monster(pygame.sprite.Sprite):

    def __init__(self, game, sprite, sprite2=None, have_animation=False, spe_chara=False):
        super().__init__()
        self.game = game
        self.is_alive = True
        self.have_animation = have_animation
        self.spe_chara = spe_chara
        self.monster_chara = self.get_chara()
        self.velocity = self.monster_chara[0]
        self.health = self.monster_chara[1]
        self.max_health = self.monster_chara[1]
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = 720 - randint(0, 20)

    def remove(self):
        self.game.all_monsters.remove(self)
        self.game.kill += 1
        self.game.spawn_monster()

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

    def get_chara(self):

        if not self.spe_chara:
            lvl_chara = [[randint(1, 3), 1], [randint(2,3), 1], [randint(3, 5), 2]]
            lvl = self.game.lvl - 1
            return lvl_chara[lvl]

        lvl_chara = [[randint(4, 6), 1], [randint(7, 9), 1], [randint(4, 6), 2]]
        lvl = self.game.lvl - 1
        return lvl_chara[lvl]


class Goomba(Monster):

    def __init__(self, game):
        super().__init__(game, "assets/Images/sprites/goomba.png")
        self.rect.y = 385
        self.channel = pygame.mixer.Channel(0)
        self.sound = pygame.mixer.Sound("assets/Sound_effects/death_Sound.mp3")

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.sound.play()
            self.remove()
        

class BobOmb(Monster):

    def __init__(self, game):
        super().__init__(game, "assets/Images/sprites/bob_omb.png")
        self.rect.y = 425
        self.channel = pygame.mixer.Channel(1)
        self.sound = pygame.mixer.Sound("assets/Sound_effects/explosion_Sound.wav")

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.explode()
            self.is_alive = False

    def explode(self):
        self.image = pygame.image.load("assets/Images/sprites/explosion.png")
        self.channel.play(self.sound)

    def sound_status(self):
        if not self.channel.get_busy():
            self.remove()


class Koopa(Monster):

    def __init__(self, game):
        super().__init__(game, "assets/Images/sprites/koopa/yellow_koopa(1).png", have_animation=True, spe_chara=True)
        self.have_armor = True
        self.rect.y = 430

    def damage(self, amount):

        if self.have_armor:
            self.have_armor = False
            self.change_sprite()
            return

        self.health -= amount

        if self.health <= 0:
            self.remove()

    def change_sprite(self):
        x_position = self.rect.x
        self.velocity = self.velocity // 2
        self.image = pygame.image.load("assets/Images/sprites/koopa/yellow_koopa(2).png")
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = 375