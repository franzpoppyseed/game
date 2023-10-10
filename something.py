import pygame
pygame.init() #makes instance of pygame
black = (0,0,0) #set color
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

done = False

while done == False: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()