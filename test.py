import pygame
from monsters import *
from game import Game

pygame.init()
pygame.mixer.init()

# creer la fenêtre
pygame.display.set_caption("Mario vs Goumba")
screen = pygame.display.set_mode((933, 600))
pygame_icon = pygame.image.load('assets/Images/icone.png')
pygame.display.set_icon(pygame_icon)

# creer les backgrounds
background = pygame.image.load('assets/Images/backgrounds/bg.png')

game = Game()

all_monsters = pygame.sprite.Group()

monster1 = Goomba(game)
monster1.rect.x = 0
monster2 = BobOmb(game)
monster2.rect.x = 300
monster3 = Koopa(game)
monster3.rect.x = 600
monster4 = Koopa(game)
monster4.image = pygame.image.load("assets/Images/sprites/koopa/yellow_koopa.png")
monster4.rect = monster4.image.get_rect()
monster4.rect.x = 600
monster4.rect.y = 375

all_monsters.add(monster1)
all_monsters.add(monster2)
all_monsters.add(monster3)
all_monsters.add(monster4)

running = True
while running:
    # afficher le background sur l'écran
    screen.blit(background, (0, 0))

    all_monsters.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():

        # si le joueur quitte la fenêtre
        if event.type == pygame.QUIT:
            # on coupe le jeux
            running = False
            pygame.quit()

        # detecter si un joueur presse une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                monster3.change_sprite()

        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False