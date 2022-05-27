import pygame
import animation
from random import randint


class Monster(animation.AnimateSprite):

    def __init__(self, game, sprite_name, have_animation=False, spe_chara=False):
        super().__init__(sprite_name)
        self.game = game
        self.is_alive = True
        self.have_animation = have_animation
        self.spe_chara = spe_chara
        self.monster_chara = self.get_chara()
        self.velocity = self.monster_chara[0]
        self.health = self.monster_chara[1]
        self.max_health = self.monster_chara[1]
        self.rect = self.image.get_rect()
        self.rect.x = 720 - randint(0, 20)

    def remove(self, sound=None):
        if sound is not None:
            sound.play()
        self.game.all_monsters.remove(self)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

    def update_animation(self):
        if self.have_animation:
            self.animate()

    def get_chara(self):

        if not self.spe_chara:
            lvl_chara = [[randint(1, 3), 1], [randint(3, 5), 1], [randint(4, 6), 2]]
            lvl = self.game.lvl - 1
            return lvl_chara[lvl]

        lvl_chara = [[randint(2, 4), 1], [randint(4, 6), 1], [randint(6, 8), 2]]
        lvl = self.game.lvl - 1
        return lvl_chara[lvl]


class Goomba(Monster):

    def __init__(self, game):
        super().__init__(game, "goomba")
        self.rect.y = 385
        self.sound = pygame.mixer.Sound("assets/Sound_effects/death_Sound.mp3")

    def damage(self, amount=0, death=False):

        if death:
            self.remove(self.sound)
            self.game.kill += 1
            self.game.spawn_monster()
            return

        self.health -= amount

        if self.health <= 0:
            self.sound.play()
            self.remove(self.sound)
            self.game.kill += 1
            self.game.spawn_monster()
        

class BobOmb(Monster):

    def __init__(self, game):
        super().__init__(game, "bob_omb")
        self.rect.y = 425
        self.channel = pygame.mixer.Channel(1)
        self.sound = pygame.mixer.Sound("assets/Sound_effects/explosion_Sound.wav")

    def damage(self, amount=0, death=False):

        if death:
            self.remove(self.sound)
            self.game.kill += 1
            self.game.spawn_monster()
            return

        self.health -= amount

        if self.health <= 0:
            self.explode()
            self.is_alive = False
            self.game.kill += 1
            self.game.spawn_monster()

    def explode(self):
        self.image = pygame.image.load("assets/Images/sprites/explosion.png")
        self.channel.play(self.sound)

    def sound_status(self):
        if not self.channel.get_busy():
            self.remove()


class Koopa(Monster):

    def __init__(self, game):
        super().__init__(game, self.get_koopa_color(game), have_animation=True, spe_chara=True)
        self.rect.y = 430
        self.have_armor = True
        self.color = self.get_koopa_color(game)
        self.sound = pygame.mixer.Sound("assets/Sound_effects/death_Sound2.mp3")

    def get_koopa_color(self, game):
        colors = ["YellowKoopa", "BlueKoopa", "RedKoopa"]
        color = colors[game.lvl - 1]
        return color

    def damage(self, amount=0, death=False):

        if death:
            self.remove(self.sound)
            self.game.kill += 1
            self.game.spawn_monster()
            return

        if self.have_armor:
            self.have_armor = False
            self.change_sprite()
            return

        self.health -= amount

        if self.health <= 0:
            self.remove(self.sound)
            self.game.kill += 1
            self.game.spawn_monster()

    def change_sprite(self):
        x_position = self.rect.x
        self.velocity = self.velocity // 2
        self.image = pygame.image.load(f"assets/Images/sprites/{self.color}/{self.color}1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = 375
        self.start_animation()
