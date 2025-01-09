# Ball class
import math
import random
import pygame

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

class Ball:
    def __init__(self, x, y, radius, ball_type):
        ball_params = ball_types[ball_type]
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = ball_params["speed"]
        self.gravity = ball_params["gravity"]
        self.special_effect = ball_params["special_effect"]
        self.color = ball_params["color"]
        self.direction = math.pi / 4  # Default 45-degree angle
        self.velocity_x = self.speed * math.cos(self.direction)
        self.velocity_y = self.speed * math.sin(self.direction)

    def update(self, WINDOW_HEIGHT):
        # update ball pos
        self.x += self.velocity_x
        self.y += self.velocity_y

        # apply gravity if needed
        if self.gravity:
            self.velocity_y += self.gravity

        # ball boundary coll (bounce off top and bottom)
        if self.y <= 0 or self.y >= WINDOW_HEIGHT - self.radius:
            self.velocity_y = -self.velocity_y  # Reverse vertical direction

        # handle chaotic 
        if self.special_effect == "chaotic":
            # slightly randomize the velocity direction
            angle_variation = random.uniform(-0.05, 0.05)  # Small random angle adjustment
            new_direction = math.atan2(self.velocity_y, self.velocity_x) + angle_variation

            # recalculate velocities with the adjusted direction
            speed = (self.velocity_x**2 + self.velocity_y**2)**0.5  # Maintain current speed
            self.velocity_x = speed * math.cos(new_direction)
            self.velocity_y = speed * math.sin(new_direction)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)