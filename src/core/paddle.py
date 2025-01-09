import pygame

class Paddle:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def move(self, keys, up_key, down_key, WINDOW_HEIGHT):
        if keys[up_key]:
            self.y -= self.speed
        if keys[down_key]:
            self.y += self.speed

        # Prevent the paddle from going out of bounds
        self.y = max(0, min(self.y, WINDOW_HEIGHT - self.height))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))