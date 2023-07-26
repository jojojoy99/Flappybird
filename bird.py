import pygame
from pipe import Pipe

class Bird:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 0.6
        self.lift = -15
        self.bird_img = pygame.image.load('bird.png')  # Load bird image

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        # Limit the bird's falling speed
        if self.velocity > 10:
            self.velocity = 10

        # Prevent the bird from going off the top of the screen
        if self.y < 0:
            self.y = 0
            self.velocity = 0

    def show(self, win):
        win.blit(self.bird_img, (self.x, self.y))  # Draw the bird on the screen

    def up(self):
        self.velocity += self.lift

    def hits(self, pipe: Pipe) -> bool:
        bird_rect = pygame.Rect(self.x, self.y, self.bird_img.get_width(), self.bird_img.get_height())
        pipe_top_rect = pygame.Rect(pipe.x, 0, pipe.PIPE_TOP.get_width(), pipe.top)
        pipe_bottom_rect = pygame.Rect(pipe.x, pipe.bottom, pipe.PIPE_BOTTOM.get_width(), pipe.PIPE_BOTTOM.get_height())

        return bird_rect.colliderect(pipe_top_rect) or bird_rect.colliderect(pipe_bottom_rect)
