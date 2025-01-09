import time 
import pygame
import sys

import game

WINDOW_WIDTH, WINDOW_HEIGHT = 720, 500

pygame.init()
pygame.display.set_caption("Pong V2")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font("assets/fonts/ARCADECLASSIC.TTF", 55)
button_text = font.render("play", True, (255,255,255))
button_rect = button_text.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 100) * 45 ))

while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                game.main()
                print("Button clicked!")

    pygame.draw.rect(screen, (0,0,0), button_rect.inflate(00, 00))
    screen.blit(button_text, button_rect)

    pygame.display.flip()

    clock.tick(60)