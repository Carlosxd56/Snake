# import libraries and modules
import pygame
from pygame.locals import *
import constants

class Snake():
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.snake_body = pygame.image.load("Images\snake_body.png")
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_window.blit(self.snake_body, (self.x, self.y))
        pygame.display.flip()

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def move_up(self):
        self.y += 10
    
    def move_down(self):
        self.y -= 10


class GAME():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(constants.Size)
        self.title = pygame.display.set_caption(constants.title)
        self.window.fill(constants.BG_Color)
        icon = pygame.image.load("Images\icon.png")
        pygame.display.set_icon(icon)

        self.snake = Snake(self.window)
        self.snake.draw()

        pygame.display.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()
                    
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    
                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

game = GAME()

game.run()