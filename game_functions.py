import pygame
import sys

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
                 ship.moving_right = True
        elif event.type ==pygame.KEYUP:
             if event.key == pygame.K_RIGHT:
                 ship.moving_right = False
    

def update_screen(ai_settings,screen,ship):

    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
