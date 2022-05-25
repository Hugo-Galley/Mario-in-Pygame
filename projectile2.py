import pygame


class Projectile2(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/Images/sprites/knife (1).png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 20
        self.rect.y = player.rect.y - 10
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile lorsque il est en deplacement
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile entre en colision avec un monstre :
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimée projectile

            monster.remove()

        # verifier si projectile plus present sur ecran
        if self.rect.x > 1080:
            # supprimer projectile
            self.remove()
            print("Supprimée")