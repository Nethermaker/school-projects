import pygame, random, math, datetime

from pygame.locals import *

class GameMain():

    done = False
    color_bg = Color('gray30')

    def __init__(self, width=800, height=800):

        pygame.mixer.pre_init(44100,-16,2,2048)
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        
        self.centerx = self.width/2
        self.centery = self.height/2
        self.radius = self.centerx - 50

        #Create some text!
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text_obj = self.font.render('00:00:00', True, Color('white'))
        self.text_rect = self.text_obj.get_rect()
        self.text_rect.center = (self.centerx, self.height-20)

        #12
        self.twelve = self.font.render('XII', True, Color('blue'))
        self.twelve_rect = self.twelve.get_rect()
        self.twelve_rect.center = (self.centerx, self.centery-self.radius+30)

        self.tock = pygame.mixer.Sound('click2.wav')
        

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.get_time()
            self.draw()
            self.tock.play()
            self.clock.tick(1)
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

        second_angle = 2*math.pi*self.second/60 - math.pi/2
        minute_angle = 2*math.pi*self.minute/60 + 2*math.pi*self.second/(60*60) - math.pi/2
        hour_angle = 2*math.pi*self.hour/12 + 2*math.pi*self.minute/(60*12) - math.pi/2
        

        #CLOCK FACE
        pygame.draw.circle(self.screen, Color('white'),
                           (self.centerx, self.centery),
                           self.radius, 0)
        #HOUR HAND
        pygame.draw.line(self.screen, Color('red'),
                         (self.centerx, self.centery),
                         (self.centerx+0.6*self.radius*math.cos(hour_angle),
                          self.centery+0.6*self.radius*math.sin(hour_angle)),5) #CHANGE THIS
        #MINUTE HAND
        pygame.draw.line(self.screen, Color('black'),
                         (self.centerx, self.centery),
                         (self.centerx+0.8*self.radius*math.cos(minute_angle),
                          self.centery+0.8*self.radius*math.sin(minute_angle)),3) #CHANGE THIS
        #SECOND HAND
        pygame.draw.line(self.screen, Color('green'),
                         (self.centerx, self.centery),
                         (self.centerx+0.9*self.radius*math.cos(second_angle),
                          self.centery+0.9*self.radius*math.sin(second_angle)),2) #CHANGE THIS
        #DISPLAY TIME
        self.text_obj = self.font.render('{}:{}:{}'.format(str(self.hour).zfill(2),
                                                           str(self.minute).zfill(2),
                                                           str(self.second).zfill(2)),
                                         True, Color('white'))
        self.screen.blit(self.text_obj, self.text_rect)
        #12
        self.screen.blit(self.twelve, self.twelve_rect)
        

        pygame.display.flip() #put all the work on the screen

    def handle_events(self):

        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.done = True

    def get_time(self):
        self.current = datetime.datetime.now()
        self.second = self.current.second
        self.minute = self.current.minute
        self.hour = self.current.hour

if __name__ == '__main__':
    game = GameMain()
    game.main_loop()




























