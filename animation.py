import pygame
import math

# definir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses à faire à la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f"assets/Images/sprites/{sprite_name}.png")
        self.current_image = 0 # commencer l'anim à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    def start_animation(self):
        self.animation = True

    # definir une methode pour animer le sprite
    def animate(self):

        # vérifier si l'animation est active
        if self.animation:

            # passer à l'image suivante
            self.current_image += self.velocity/25

            # verifier si on a atteint la fin de l'animation
            if math.floor(self.current_image) >= len(self.images):
                # remettre l'animation au départ
                self.current_image = 0

            # modifier l'image précedente par la suivante
            self.image = self.images[math.floor(self.current_image)]

# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les images de ce sprite dans le dossier correspondant
    images = []
    path = f"assets/Images/sprites/{sprite_name}/{sprite_name}"

    # boucler sur chaque image dans ce dossier
    for num in range(1, 3):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'image
    return images


# definir un dictionnaire qui va contenir les images charger de chaque sprites
animations = {
    "YellowKoopa": load_animation_images("YellowKoopa"),
    "BlueKoopa": load_animation_images("BlueKoopa"),
    "RedKoopa": load_animation_images("RedKoopa")
}
