import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, damage, image_path):
        super().__init__()
        self.player = player
        self.velocity = 5
        self.damage = damage
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.origine_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 20
        self.rect.y = player.rect.y - 10
        self.angle = 0

    def rotate(self):
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)


class FireBall(Projectile):

    def __init__(self, player):
        super().__init__(player, 1, 'assets/Images/sprites/fireball.png')
        self.sound = pygame.mixer.Sound("assets/Sound_effects/fireball_Sound.mp3")

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile entre en colision avec un monstre :
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            if monster.is_alive:
                # supprimer projectile
                self.remove()

                # infliger des dégats au monstre
                monster.damage(self.damage)

        # verifier si projectile plus present sur ecran
        if self.rect.x > 966:
            # supprimer projectile
            self.remove()
            print("Supprimée")


class Knife(Projectile):

    def __init__(self, player):
        super().__init__(player, None, 'assets/Images/sprites/knife (1).png')
        self.sound = pygame.mixer.Sound("assets/Sound_effects/gun_Sound.mp3")

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile entre en colision avec un monstre :
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer monstre
            monster.remove()

        # verifier si projectile plus present sur ecran
        if self.rect.x > 1080:
            # supprimer projectile
            self.remove()
            print("Supprimée")