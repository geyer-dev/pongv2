import time
import pygame
import os
import sys

import game

WINDOW_WIDTH, WINDOW_HEIGHT = 720, 500

pygame.init()
pygame.display.set_caption("Pong V2")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

os.chdir(os.path.dirname(os.path.realpath(__file__)))

font = pygame.font.Font("../../assets/fonts/ARCADECLASSIC.TTF", 55)
start_text = font.render("play", True, (255, 255, 255))
options_text = font.render("options", True, (255, 255, 255))
exit_text = font.render("exit", True, (255, 255, 255))

# Set up button rectangles
start_rect = start_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 45))
options_rect = options_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 60))
exit_rect = exit_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 75))

while True:
    screen.fill("black")

    # Default button rendering
    start_text = font.render("play", True, (255, 255, 255))
    options_text = font.render("options", True, (255, 255, 255))
    exit_text = font.render("exit", True, (255, 255, 255))

    # Check if buttons are hovered
    mouse_pos = pygame.mouse.get_pos()
    if start_rect.collidepoint(mouse_pos):
        shadow_text = font.render("play", True, (0, 155, 155))
        shadow_rect = start_rect.copy()
        shadow_rect.x -= 1
        shadow_rect.y += 4
        screen.blit(shadow_text, shadow_rect)
        start_text = font.render("play", True, (0, 255, 0))

    if options_rect.collidepoint(mouse_pos):
        shadow_text = font.render("options", True, (0, 0, 255))
        shadow_rect = options_rect.copy()
        shadow_rect.x += 3
        shadow_rect.y -= 3
        screen.blit(shadow_text, shadow_rect)
        options_text = font.render("options", True, (255, 255, 255))

    if exit_rect.collidepoint(mouse_pos):
        shadow_text = font.render("exit", True, (200, 200, 200))
        shadow_rect = exit_rect.copy()
        shadow_rect.x -= 2
        shadow_rect.y += 2
        screen.blit(shadow_text, shadow_rect)
        exit_text = font.render("exit", True, (255, 0, 0))
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                print("Start button clicked!")
                game.main()
            elif exit_rect.collidepoint(event.pos):
                print("Exit button clicked!")
                pygame.quit()
                sys.exit()

    # Draw buttons
    screen.blit(start_text, start_rect)
    screen.blit(options_text, options_rect)
    screen.blit(exit_text, exit_rect)

    pygame.display.flip()
    clock.tick(60)
