import pygame, random, math

from pygame.locals import *


class Particle(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.rect = Rect(0,0,5,5)
        self.rect.center = pos

        self.image = pygame.Surface(self.rect.size)
        self.image.fill(Color('yellow'))

        self.velx = random.randint(-5, 5)
        self.vely = random.randint(-5, 5)


    def update(self, screen):

        self.vely += 1

        self.rect.x += self.velx
        self.rect.y += self.vely

        if self.rect.y > screen.get_height():
            self.kill()
        
        
        

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
    SPEED = 10

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        self.rect = Rect(400,300,20,20)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(Color('orange'))
        
        self.velx = self.SPEED
        self.vely = self.SPEED
    
    def update(self, game):
        self.rect.x += self.velx
        self.rect.y += self.vely

        if self.rect.top <= 0:
            self.vely *= -1
        if self.rect.bottom >= self.screen.get_height():
            self.vely *= -1

        if not self.rect.colliderect(self.screen.get_rect()):
            if self.rect.x >= self.screen.get_width()/2:
                game.left_score += 1
            elif self.rect.x <= self.screen.get_width()/2:
                game.right_score += 1
            self.reset()

    def handle_collision(self, paddle, game):
        if self.velx < 0:   #If the ball is going to the left
            self.rect.left = paddle.rect.right
            self.velx *= -1
            self.vely += random.randint(-3,3)
        elif self.velx > 0: #If the ball is going to the right
            self.rect.right = paddle.rect.left
            self.velx *= -1
            self.vely += random.randint(-3,3)
        for x in range(0,random.randint(5,10)):
            game.particles.add(Particle(self.rect.center))
        

    def reset(self):
        self.rect.center = (self.screen.get_width()/2, self.screen.get_height()/2)
        self.velx = 0
        self.vely = 0


    



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

        self.ball = Ball(self.screen)
        self.balls = pygame.sprite.Group()
        self.balls.add(self.ball)

        self.left_score = 0
        self.right_score = 0

        self.particles = pygame.sprite.Group()

        self.font = pygame.font.Font('freesansbold.ttf', 32)
        
        self.left_score_text = self.font.render('{}'.format(self.left_score), True, Color('red'))
        self.left_score_rect = self.left_score_text.get_rect()
        self.left_score_rect.left = 10
        self.left_score_rect.top = 10

        self.right_score_text = self.font.render('{}'.format(self.right_score), True, Color('red'))
        self.right_score_rect = self.right_score_text.get_rect()
        self.right_score_rect.right = self.width - 10
        self.right_score_rect.top = 10

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.balls.update(game)
            self.particles.update(self.screen)

            for p in self.paddles:
                if self.ball.rect.colliderect(p.rect):
                    self.ball.handle_collision(p, game)
                    
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

        self.paddles.draw(self.screen)

        self.balls.draw(self.screen)

        self.particles.draw(self.screen)

        self.left_score_text = self.font.render('{}'.format(self.left_score), True, Color('red'))
        self.screen.blit(self.left_score_text, self.left_score_rect)
        self.right_score_text = self.font.render('{}'.format(self.right_score), True, Color('red'))
        self.screen.blit(self.right_score_text, self.right_score_rect)

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
                elif event.key == K_SPACE and self.ball.velx == 0 and self.ball.vely == 0:
                    ranges = range(0,61) + range(120,241) + range(300, 360)
                    angle = math.radians(random.choice(ranges))
                    self.ball.velx = math.cos(angle) * self.ball.SPEED
                    self.ball.vely = math.sin(angle) * self.ball.SPEED
                elif event.key == K_SPACE:
                    self.ball.reset()
                
                

if __name__ == '__main__':
    game = GameMain()
    game.main_loop()
