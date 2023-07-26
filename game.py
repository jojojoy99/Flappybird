import pygame
import sys
from bird import Bird
from pipe import Pipe

class Game:
    def __init__(self):
        self.score = 0
        self.bird = Bird(230, 350)
        self.pipes = [Pipe(600)]
        self.win = pygame.display.set_mode((500, 800))  # Game window
        self.bg_img = pygame.image.load('bg.png')  # Load background image
        self.game_over = False

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)  # Set the game's frame rate to 30
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.bird.up()

            self.bird.update()
            self.add_pipe()
            self.move_pipes()

            if self.collision_check():
                self.game_over = True

            self.draw_window()

            if self.game_over:
                self.end()

    def draw_window(self):
        self.win.blit(self.bg_img, (0, 0))  # Draw the background image
        self.bird.show(self.win)
        for pipe in self.pipes:
            pipe.show(self.win)
        pygame.display.update()

    def add_pipe(self):
        if len(self.pipes) > 0 and self.pipes[-1].x < 400:
            self.pipes.append(Pipe(600))

    def move_pipes(self):
        for pipe in self.pipes:
            pipe.update()
            if pipe.offscreen():
                self.pipes.remove(pipe)
                self.score += 1

    def collision_check(self):
        for pipe in self.pipes:
            if self.bird.hits(pipe) or self.bird.y > 750:
                return True
        return False

    def end(self):
        print("Game Over! Your score is: ", self.score)
        pygame.quit()
        sys.exit()

    def restart(self):
        self.score = 0
        self.bird = Bird(230, 350)
        self.pipes = [Pipe(600)]
        self.game_over = False
        self.run()
