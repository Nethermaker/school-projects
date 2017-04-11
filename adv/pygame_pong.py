import pygame, random, math

from pygame.locals import *


class Paddle(pygame.sprite.Sprite):
    WIDTH, HEIGHT = 15, 150
    SPEED = 20

    def __init__(self, pos, up, down):
        pygame.sprite.Sprite.__init__(self)

        self.rect = Rect(0,0,Paddle.WIDTH,Paddle.HEIGHT)
        self.rect.center = pos

        self.image = pygame.Surface(self.rect.size)
        self.image.fill(Color('orange'))

        self.up = up
        self.down = down

    def handle_keystate(self, keys, screen):

        if keys[self.up] and self.rect.top > 0:
            self.rect.top -= self.SPEED
        if keys[self.down] and self.rect.bottom < screen.get_height():
            self.rect.top += self.SPEED



class Ball(pygame.sprite.Sprite):
    SPEED = 5

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self. rect = Rect(400,300,20,20)

        self.image = pygame.Surface(self.rect.size)
        self.image.fill(Color('orange'))
        



class GameMain():

    done = False
    color_bg = Color('blue')

    def __init__(self, width=800, height=600):

        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.player1 = Paddle((50,300), K_a, K_d)
        self.player2 = Paddle((self.width-50, 300),K_RIGHT, K_LEFT)

        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.player1, self.player2) #put the paddles in a group

        self.ball = Ball()
        self.balls = pygame.sprite.Group()
        self.balls.add(self.ball)

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

        self.paddles.draw(self.screen)

        self.balls.draw(self.screen)

        pygame.display.flip() #put all the work on the screen

    def handle_events(self):

        events = pygame.event.get()

        keys = pygame.key.get_pressed()
        self.player1.handle_keystate(keys, self.screen)
        self.player2.handle_keystate(keys, self.screen)
        
        for event in events:

            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.done = True
                

if __name__ == '__main__':
    game = GameMain()
    game.main_loop()
