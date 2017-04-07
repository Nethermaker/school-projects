import pygame, random, math

from pygame.locals import *

class GameMain():

    done = False
    color_bg = Color('white')

    def __init__(self, width=800, height=600):

        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.mousex = 0
        self.mousey = 0
        self.manning = pygame.image.load('manning.jpg')

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.draw()
            self.clock.tick(144)
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

        pygame.draw.rect(self.screen, Color('red'), (250,150,300,300))
        pygame.draw.polygon(self.screen, Color('white'), ((365,450), (435,450), (365,350)))
        pygame.draw.polygon(self.screen, Color('white'), ((330,378), (385,378), (330,305)))
        pygame.draw.rect(self.screen, Color('white'), (250,222,30,156))
        pygame.draw.rect(self.screen, Color('white'), (520,222,30,156))
        pygame.draw.polygon(self.screen, Color('white'), ((365,150), (435,150), (435,250)))
        pygame.draw.polygon(self.screen, Color('white'), ((418,226), (473,226), (473,299)))

        pygame.display.flip()

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
