import time
import pygame
import os
import sys
import math

import game

WINDOW_WIDTH, WINDOW_HEIGHT = 720, 500

pygame.init()
pygame.display.set_caption("Pong V2")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Fonts
title_font = pygame.font.Font("../../assets/fonts/ARCADECLASSIC.TTF", 100)  # Larger font for title
button_font = pygame.font.Font("../../assets/fonts/ARCADECLASSIC.TTF", 55)  # Smaller font for buttons

options_menu_open = False
color_time = 0

options_bg = pygame.image.load("../../assets/imgs/options_bg.svg")
options_bg = pygame.transform.scale_by(options_bg, 7)

# Initial button and title texts
start_text = button_font.render("play", True, (255, 255, 255))
options_text = button_font.render("options", True, (255, 255, 255))
exit_text = button_font.render("exit", True, (255, 255, 255))

# Set up button and title rectangles
start_rect = start_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 45))
options_rect = options_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 60))
exit_rect = exit_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 75))
gametitle_rect = title_font.render("Pong V2", True, (255, 255, 255)).get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 25))

while True:
    screen.fill("black")

    # Update color_time for smooth transitions
    color_time += 0.02

    # Calculate RGB values using sine waves
    title_r = int((math.sin(color_time) + 1) * 127.5)  # Oscillates between 0 and 255
    title_g = int((math.sin(color_time + 2) + 1) * 127.5)  # Phase-shifted for variation
    title_b = int((math.sin(color_time + 4) + 1) * 127.5)  # Further phase-shifted

    # Render the title with updated colors
    gametitle_text = title_font.render("Pong V2", True, (title_r, title_g, title_b))

    # Default button rendering
    start_text = button_font.render("play", True, (255, 255, 255))
    options_text = button_font.render("options", True, (255, 255, 255))
    exit_text = button_font.render("exit", True, (255, 255, 255))

    #check button hover
    mouse_pos = pygame.mouse.get_pos()
    if start_rect.collidepoint(mouse_pos):
        shadow_text = button_font.render("play", True, (0, 155, 155))
        shadow_rect = start_rect.copy()
        shadow_rect.x -= 1
        shadow_rect.y += 4
        screen.blit(shadow_text, shadow_rect)
        start_text = button_font.render("play", True, (0, 255, 0))

    if options_rect.collidepoint(mouse_pos):
        shadow_text = button_font.render("options", True, (0, 0, 255))
        shadow_rect = options_rect.copy()
        shadow_rect.x += 3
        shadow_rect.y -= 3
        screen.blit(shadow_text, shadow_rect)
        options_text = button_font.render("options", True, (255, 255, 255))

    if exit_rect.collidepoint(mouse_pos):
        shadow_text = button_font.render("exit", True, (200, 200, 200))
        shadow_rect = exit_rect.copy()
        shadow_rect.x -= 2
        shadow_rect.y += 2
        screen.blit(shadow_text, shadow_rect)
        exit_text = button_font.render("exit", True, (255, 0, 0))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(ev.pos):
                if options_menu_open:
                    pass
                game.main()
            elif options_rect.collidepoint(ev.pos):
                if options_menu_open:
                    pass
                else:
                    options_menu_open = True
            elif exit_rect.collidepoint(ev.pos):
                if options_menu_open:
                    options_menu_open = False
                    exit_rect = exit_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 75))
                else:
                    pygame.quit()
                    sys.exit()
            

    # Draw title
    screen.blit(gametitle_text, gametitle_rect)

    # Draw buttons
    screen.blit(start_text, start_rect)
    screen.blit(options_text, options_rect)
    screen.blit(exit_text, exit_rect)

    if options_menu_open:
        screen.blit(options_bg, ((WINDOW_WIDTH - options_bg.get_width()) // 2, (WINDOW_HEIGHT - options_bg.get_height()) // 2))

        # Draw the vertical separator in the middle
        separator_width = 4  # Thickness of the separator
        separator_height = WINDOW_HEIGHT / 1.7  # Full height of the window
        separator_x = (WINDOW_WIDTH // 2) - (separator_width // 2)  # Center the separator
        separator_rect = pygame.Rect(separator_x, (WINDOW_HEIGHT / 100) * 15, separator_width, separator_height)

        pygame.draw.rect(screen, (255,255,255), separator_rect)  # Draw the separator

        exit_text = button_font.render("Back", True, (255, 255, 255))
        exit_rect = exit_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 82))
        screen.blit(exit_text, exit_rect)

    pygame.display.flip()
    clock.tick(60)
