import pygame, sys

class Person(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

person = Person(50, 50, 100, 100, (255, 255, 255))

person_group = pygame.sprite.Group()
person_group.add(person)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    person_group.draw(screen)
    clock.tick(165)