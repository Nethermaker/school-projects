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
        self.manning = pygame.image.load('manning.jpg')

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.draw()
            self.clock.tick(144)
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

##        random_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
##
##        pygame.draw.circle(self.screen, random_color, (400, 300), 50)
##        pygame.draw.line(self.screen, random_color, (100,100), (100,300), 3)
##        #Rectangles require a startx, starty, width, and height
##        pygame.draw.rect(self.screen, random_color, (10,10,50,100))
##        pygame.draw.ellipse(self.screen, random_color, (500, 400, 50, 100))
##        pygame.draw.polygon(self.screen, random_color, ((100,500), (self.mousex,self.mousey), (125, 590)))

        self.screen.blit(self.manning, (self.mousex, self.mousey))

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
