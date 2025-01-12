import pygame
import os
import sys
import math

from game import main

WINDOW_WIDTH, WINDOW_HEIGHT = 720, 500

pygame.init()
pygame.display.set_caption("Pong V2")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#fonts
title_font = pygame.font.Font("../../assets/fonts/ARCADECLASSIC.TTF", 100)  # Larger font for title
button_font = pygame.font.Font("../../assets/fonts/ARCADECLASSIC.TTF", 55)  # Smaller font for buttons

options_menu_open = False
color_time = 0

options_bg = pygame.image.load("../../assets/imgs/options_bg.svg")
options_bg = pygame.transform.scale_by(options_bg, 7)

#arrow images
try:
    right_arrow_top = pygame.image.load("../../assets/imgs/right_arrow.svg")
    left_arrow_top = pygame.image.load("../../assets/imgs/left_arrow.svg")
    right_arrow_top = pygame.transform.scale_by(right_arrow_top, 2.75)
    left_arrow_top = pygame.transform.scale_by(left_arrow_top, 2.75)
except pygame.error as e:
    print(f"Error loading arrow images: {e}")
    right_arrow_top = pygame.Surface((50, 50))
    left_arrow_top = pygame.Surface((50, 50))
    right_arrow_top.fill((255, 0, 0))
    left_arrow_top.fill((0, 255, 0))

#arrow positions
right_arrow_rect_top = right_arrow_top.get_rect(topleft=(278, 125))
left_arrow_rect_top = left_arrow_top.get_rect(topleft=(152, 125))

#initial button and title texts
start_text = button_font.render("play", True, (255, 255, 255))
options_text = button_font.render("options", True, (255, 255, 255))
exit_text = button_font.render("exit", True, (255, 255, 255))

#button and title rectangles
start_rect = start_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 45))
options_rect = options_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 60))
exit_rect = exit_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 75))
gametitle_rect = title_font.render("Pong V2", True, (255, 255, 255)).get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 25))

#circles for options menu
circles = [
    {"color": (255, 255, 255), "position": (245, 145), "radius": 15},
    {"color": (255, 0, 0), "position": (245, 145), "radius": 7},
    {"color": (0, 255, 0), "position": (245, 145), "radius": 22}
]
current_circle_index = 0



#separate rect for the back button in the options menu
back_text = button_font.render("Back", True, (255, 255, 255))
back_rect = back_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 82))

while True:
    screen.fill("black")

    #update colortime for smooth transition
    color_time += 0.02

    #calc rgb values
    title_r = int((math.sin(color_time) + 1) * 127.5)  # Oscillates between 0 and 255
    title_g = int((math.sin(color_time + 2) + 1) * 127.5)  # Phase-shifted for variation
    title_b = int((math.sin(color_time + 4) + 1) * 127.5)  # Further phase-shifted

    #render title with updated color
    gametitle_text = title_font.render("Pong V2", True, (title_r, title_g, title_b))

    #default button rendering
    start_text = button_font.render("play", True, (255, 255, 255))
    options_text = button_font.render("options", True, (255, 255, 255))
    exit_text = button_font.render("exit", True, (255, 255, 255))

    right_arrow_top = pygame.image.load("../../assets/imgs/right_arrow.svg")
    left_arrow_top = pygame.image.load("../../assets/imgs/left_arrow.svg")
    right_arrow_top = pygame.transform.scale_by(right_arrow_top, 2.75)
    left_arrow_top = pygame.transform.scale_by(left_arrow_top, 2.75)

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

    if not options_menu_open and exit_rect.collidepoint(mouse_pos):
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
            if not options_menu_open:
                if start_rect.collidepoint(ev.pos):
                    main(current_circle_index)
                elif options_rect.collidepoint(ev.pos):
                    options_menu_open = True
                elif exit_rect.collidepoint(ev.pos):
                    pygame.quit()
                    sys.exit()
            else:
                # arrow button clicks in options menu
                if right_arrow_rect_top.collidepoint(ev.pos):
                    current_circle_index = (current_circle_index + 1) % len(circles)
                elif left_arrow_rect_top.collidepoint(ev.pos):
                    current_circle_index = (current_circle_index - 1) % len(circles)
                elif back_rect.collidepoint(ev.pos):  # Back button in the options menu
                    options_menu_open = False

    #title
    screen.blit(gametitle_text, gametitle_rect)

    #draw buttons if not in options menu
    if not options_menu_open:
        screen.blit(start_text, start_rect)
        screen.blit(options_text, options_rect)
        screen.blit(exit_text, exit_rect)
    else:
        #draw options background
        screen.blit(options_bg, ((WINDOW_WIDTH - options_bg.get_width()) // 2, (WINDOW_HEIGHT - options_bg.get_height()) // 2))

        #draw the vertical separator
        separator_width = 4
        separator_height = WINDOW_HEIGHT / 1.7
        separator_x = (WINDOW_WIDTH // 2) - (separator_width // 2)
        separator_rect = pygame.Rect(separator_x, (WINDOW_HEIGHT / 100) * 15, separator_width, separator_height)
        pygame.draw.rect(screen, (255, 255, 255), separator_rect)

        #draw arrows and circle
        screen.blit(right_arrow_top, (278, 125))
        screen.blit(left_arrow_top, (152, 125))
        circle = circles[current_circle_index]
        pygame.draw.circle(screen, circle["color"], circle["position"], circle["radius"])

        #draw other elements
        options_bg_copy1_top = pygame.transform.scale_by(options_bg.copy(), 0.17)
        options_bg_copy2_top = pygame.transform.scale_by(options_bg.copy(), 0.17)
        options_bg_copy1_bot = pygame.transform.scale_by(options_bg.copy(), 0.17)
        options_bg_copy2_bot = pygame.transform.scale_by(options_bg.copy(), 0.17)

        button_W = button_font.render("W", True, (255, 255, 255))
        button_S = button_font.render("S", True, (255, 255, 255))
        button_UP = button_font.render("UP", True, (255, 255, 255))
        button_DN = button_font.render("DN", True, (255, 255, 255))

        screen.blit(options_bg_copy1_top, (375, 130))
        screen.blit(options_bg_copy2_top, (500, 130))
        screen.blit(options_bg_copy1_bot, (375, 270))
        screen.blit(options_bg_copy2_bot, (500, 270))

        screen.blit(button_W, (402, 141))
        screen.blit(button_S, (528, 141))
        screen.blit(button_UP, (390, 279))
        screen.blit(button_DN, (513, 279))

        #render back button
        screen.blit(back_text, back_rect)

    pygame.display.flip()
    clock.tick(60)
