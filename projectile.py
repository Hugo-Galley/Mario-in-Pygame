import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/Images/sprites/fireball.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 20
        self.rect.y = player.rect.y - 10
        self.origin_image = self.image
        self.angle = 0

    # tourner le projectile lorsque il est en deplacement
    def rotate(self):
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    # supprimer le projectile
    def remove(self):
        self.player.all_projectiles.remove(self)

    # fait bouger le projectile
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile entre en colision avec un monstre :
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            # On vérifie dans quelle niveaux se trouve le joueur
            if self.player.game.level == 1 or self.player.game.level == 2:
                 monster.remove()

            else :
                # On vérifie combien de fois a été touchée le monstre
                if self.player.game.monster.touch == 1 or self.player.game.monster2.touch == 1:

                    monster.remove()
                    self.player.game.monster.touch = 0
                    self.player.game.monster2.touch = 0
                #On ajoute 1 au nombre de touche du joueur
                else :
                    self.player.game.monster.touch += 1
                    self.player.game.monster2.touch +=1

        # verifier si projectile plus present sur ecran
        if self.rect.x > 966:
            # supprimer projectile
            self.remove()
            print("Supprimée")