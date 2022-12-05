# import libraries and modules
import pygame
from pygame.locals import *
import constants
import time

class Snake():
    def __init__(self, parent_window, length):
        self.parent_window = parent_window
        self.snake_body = pygame.image.load("Images\snake_body.png")
        
        self.direction = "down"
        self.length = length
        self.x = [64]*length
        self.y = [64]*length


    def draw(self):
        self.parent_window.fill(constants.BG_Color)
        
        for i in range(self.length):
            self.parent_window.blit(self.snake_body, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"
    
    def move_down(self):
        self.direction = "down"

    def walk(self):
        # update body 
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            
            # update head
        if self.direction == "left":
            self.x[0] -= constants.Size_snake

        if self.direction == "right":
            self.x[0] += constants.Size_snake

        if self.direction == "up":
            self.y[0] -= constants.Size_snake
        
        if self.direction == "down":
            self.y[0] += constants.Size_snake

        self.draw()


class GAME():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(constants.Size)
        self.title = pygame.display.set_caption(constants.title)
        self.window.fill(constants.BG_Color)
        icon = pygame.image.load("Images\icon.png")
        pygame.display.set_icon(icon)

        self.snake = Snake(self.window, 5)
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

            self.snake.walk()
            time.sleep(0.2)

game = GAME()

game.run()