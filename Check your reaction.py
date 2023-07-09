import pygame, sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

pygame.display.set_caption('Check Your Reaction!')

font = pygame.font.Font('freesansbold.ttf', 32)


result = []
t = 0
for i in range(5):
    screen.fill('white')
    current_time = 0
    button_pressed_time = 0


    new_round_time = float('inf')
    screen_show = float('inf')
    screen_change_time = random.randint(5000, 10000)+pygame.time.get_ticks()
    flag = True
    ingame = True
    while ingame:

        if current_time > screen_change_time and flag:
            screen.fill('green')
            flag = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                button_pressed_time, current_time  = pygame.time.get_ticks(), pygame.time.get_ticks()

                screen.fill('white')


                if button_pressed_time < screen_change_time:
                    text = font.render('Rano!', True, 'black', 'red')
                    textRect = text.get_rect()
                    textRect.center = (400, 400)
                    screen.blit(text, textRect)

                else:
                    text = font.render(f'Ваша реакция: {(button_pressed_time - screen_change_time) / 1000} sec', True, 'black','green')
                    result.append((button_pressed_time - screen_change_time) / 1000)
                    textRect = text.get_rect()
                    textRect.center = (400, 400)
                    screen.blit(text, textRect)
                    screen_show = button_pressed_time + 5500
                    new_round_time = button_pressed_time + 9500

        if current_time>screen_show and current_time < new_round_time and button_pressed_time!=100000:
            text = font.render(f"Ваша средняя реакция: {float('{:.3f}'.format(sum(result) / len(result)))} sec", True, 'black', 'green')
            textRect = text.get_rect()
            textRect.center = (400, 400)
            screen.blit(text, textRect)
        current_time = pygame.time.get_ticks()

        if current_time > new_round_time:
            screen.fill('white')
            t = pygame.time.get_ticks()
            ingame = False


        pygame.display.update()
        clock.tick(60)