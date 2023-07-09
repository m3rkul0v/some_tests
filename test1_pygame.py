import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

current_time = 0
button_pressed_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                screen.fill((0, 128, 0))
            if event.key == pygame.K_p:
                screen.fill((128,0,128))

    pygame.display.flip()
    clock.tick(60)
