import pygame, random, math

from pygame.locals import *


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface([20,20])
        self.image.fill(Color('white'))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.changex = 0
        self.changey = 0

        self.walls = None

    def update(self):

        self.rect.x += self.changex
        
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        print block_hit_list

        self.rect.y += self.changey

    

    



class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class GameMain():

    done = False
    color_bg = Color('gray30')

    def __init__(self, width=800, height=600):

        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.player = Player(400, 300)
        self.players = pygame.sprite.Group()
        self.players.add(self.player)

        self.walls = pygame.sprite.Group()

        self.wall1 = Wall(0, 0, 800, 20, Color('black'))
        self.wall2 = Wall(0, 0, 20, 250, Color('black'))
        self.wall3 = Wall(780, 0, 20, 250, Color('black'))
        self.wall4 = Wall(0, 350, 20, 250, Color('black'))
        self.wall5 = Wall(0, 580, 800, 20, Color('black'))
        self.wall6 = Wall(780, 350, 20, 250, Color('black'))

        self.walls.add(self.wall1, self.wall2, self.wall3,
                       self.wall4, self.wall5, self.wall6)

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.players, self.walls)
        

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.player.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

        self.sprites.draw(self.screen)

        pygame.display.flip() #put all the work on the screen

    def handle_events(self):

        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.done = True
                elif event.key == K_UP:
                    self.player.changey = -6
                elif event.key == K_DOWN:
                    self.player.changey = 6
                elif event.key == K_LEFT:
                    self.player.changex = -6
                elif event.key == K_RIGHT:
                    self.player.changex = 6
            elif event.type == KEYUP:
                if event.key == K_UP:
                    self.player.changey = 0
                elif event.key == K_DOWN:
                    self.player.changey = 0
                elif event.key == K_LEFT:
                    self.player.changex = 0
                elif event.key == K_RIGHT:
                    self.player.changex = 0
                

if __name__ == '__main__':
    game = GameMain()
    game.main_loop()
