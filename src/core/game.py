import pygame
import sys
import random
import math
import time


from paddle import Paddle
from ball import Ball

def main():
    WINDOW_WIDTH, WINDOW_HEIGHT = 1024, 664
    PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
    BALL_RADIUS = 10

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (50,205,50)
    PURPLE = (255,0,255)


    pygame.init()
    pygame.display.set_caption("Pong V2")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    
    ball_types = {
    "normal": {
        "speed": 5,
        "gravity": 0,
        "special_effect": None,
        "color": (255, 255, 255)
    },
    "chaotic": {
        "speed": 5,
        "gravity": 0,
        "special_effect": "chaotic",
        "color": (255, 0, 0)
    },
    "heavy": {
        "speed": 3,
        "gravity": 0.2,
        "special_effect": None,
        "color": (0, 255, 0)
    },
    "sticky": {
        "speed": 4,
        "gravity": 0,
        "special_effect": "sticky",
        "color": (0, 0, 255)
    }}


    paddle1 = Paddle(x=30, y=WINDOW_HEIGHT//2 - PADDLE_HEIGHT//2, width=PADDLE_WIDTH, height=PADDLE_HEIGHT, color=WHITE, speed=5)
    paddle2 = Paddle(x=WINDOW_WIDTH - PADDLE_WIDTH - 30, y=WINDOW_HEIGHT//2 - PADDLE_HEIGHT//2, width=PADDLE_WIDTH, height=PADDLE_HEIGHT, color=WHITE, speed=5)
    ball = Ball(x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2, radius=BALL_RADIUS, ball_type="chaotic")  # 45 degrees

    def serveBall(ball, paddle, direction):
        ball.x = paddle.x + paddle.width if ball.velocity_x > 0 else paddle.x - ball.radius
        ball.y = paddle.y + paddle.height // 2
        ball.direction = random.uniform(-math.pi / 4, math.pi / 4)  # Slight upward/downward angle
        ball.velocity_x = ball.speed * math.cos(ball.direction)
        ball.velocity_y = ball.speed * math.sin(ball.direction)

    player2_score = 0
    player1_score = 0

    

    running = True
    while running:
        screen.fill(BLACK)

        # check scoring and serve
        if ball.x < 0:
            player2_score += 1
            serveBall(ball, paddle2, direction=-1)
        if ball.x > WINDOW_WIDTH:
            player1_score += 1
            serveBall(ball, paddle1, direction=1)

        # check game over
        """WINNING_SCORE = 5
        if player1_score >= WINNING_SCORE or player2_score >= WINNING_SCORE:
            winner = "Player 1" if player1_score >= WINNING_SCORE else "Player 2"
            print(f"{winner} Wins!")
            running = False"""

        # poll for evs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # handle paddle movement
        keys = pygame.key.get_pressed()
        paddle1.move(keys, pygame.K_w, pygame.K_s, WINDOW_HEIGHT)
        paddle2.move(keys, pygame.K_UP, pygame.K_DOWN, WINDOW_HEIGHT)

        # update ball position
        ball.update(WINDOW_HEIGHT)

        # check for colls
        if (paddle1.x < ball.x < paddle1.x + paddle1.width and paddle1.y < ball.y < paddle1.y + paddle1.height) or \
        (paddle2.x < ball.x < paddle2.x + paddle2.width and paddle2.y < ball.y < paddle2.y + paddle2.height):
            ball.velocity_x = -ball.velocity_x
            ball.velocity_y += random.uniform(-1, 1)  # Add a bit of randomness

        # draw objects
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)

        # render scores
        font = pygame.font.Font("assets/fonts/ARCADECLASSIC.TTF", 74)
        score_text1 = font.render(str(player1_score), True, WHITE)
        score_text2 = font.render(str(player2_score), True, WHITE)
        screen.blit(score_text1, (WINDOW_WIDTH // 4, 20))
        screen.blit(score_text2, (3 * WINDOW_WIDTH // 4, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()