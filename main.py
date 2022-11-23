# import libraries and modules
import pygame
from pygame.locals import *
import constants

class GAME():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(constants.Size)
        self.title = pygame.display.set_caption(constants.title)
        self.window.fill(constants.BG_Color)
        icon = pygame.image.load("Images\icon.png")
        pygame.display.set_icon(icon)
        pygame.display.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False

game = GAME()

game.run()