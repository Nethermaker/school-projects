import pygame, random, math

from pygame.locals import *

class GameMain():

    done = False
    color_bg = Color('gray30')

    def __init__(self, width=800, height=600):

        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.mousex = 0
        self.mousey = 0

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

        pygame.display.flip() #put all the work on the screen

    def handle_events(self):

        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.done = True
            elif event.type == MOUSEMOTION:
                self.mousex, self.mousey = event.pos
                print self.mousex, self.mousey

if __name__ == '__main__':
    game = GameMain()
    game.main_loop()
