## pipe.py
import pygame
import random

class Pipe:
    def __init__(self, x: float):
        self.x = x
        self.speed = 2
        self.gap = 100  # Gap between top and bottom pipes
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.image.load('pipe_top.png')  # Load top pipe image
        self.PIPE_BOTTOM = pygame.image.load('pipe_bottom.png')  # Load bottom pipe image
        self.passed = False  # Whether the bird has passed the pipe
        self.set_height()

    def set_height(self):
        """
        Randomly set the height of the pipe
        """
        height = random.randrange(50, 300)
        self.top = height - self.PIPE_TOP.get_height()
        self.bottom = height + self.gap

    def show(self, win):
        """
        Display the pipe on the screen
        """
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def update(self):
        """
        Update the position of the pipe
        """
        self.x -= self.speed

    def offscreen(self) -> bool:
        """
        Check if the pipe is off the screen
        """
        return self.x + self.PIPE_TOP.get_width() < 0
