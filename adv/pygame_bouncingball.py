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
        self.bally = 550
        self.ballx = 400
        self.ball_yspeed = 20
        self.ball_xspeed = 0

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.move_ball()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

        pygame.draw.circle(self.screen, Color('Red'), (self.ballx, self.bally), 50)

        pygame.display.flip() #put all the work on the screen

    def handle_events(self):

        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.done = True
                if event.key == K_e:
                    self.ball_xspeed += 1
                if event.key == K_q:
                    self.ball_xspeed -= 1

    def move_ball(self):
        if self.bally >= 550:
            self.ball_yspeed = 20
        self.bally -= self.ball_yspeed
        self.ball_yspeed -= 1
        self.ballx += self.ball_xspeed
        

if __name__ == '__main__':
    game = GameMain()
    game.main_loop()




















