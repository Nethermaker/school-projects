import pygame, random, math

from pygame.locals import *


class Note(pygame.sprite.Sprite):

    def __init__(self, tick, y, color, song, hold=0):
        pygame.sprite.Sprite.__init__(self)

        self.tick = tick
        self.color = color
        self.song = song
        self.hopo = False
        if len(self.song.note_list) == 0:
            self.hopo = False
        else:
            if self.tick - self.song.note_list[-1].tick <= self.song.hopo_distance:
                self.hopo = True
        self.hold = hold
        self.song = song
        self.speed = 4

        self.y = y
        self.x = 0

        if self.color == 'green':
            self.x = 540
        elif self.color == 'red':
            self.x = 590
        elif self.color == 'yellow':
            self.x = 640
        elif self.color == 'blue':
            self.x = 690
        elif self.color == 'orange':
            self.x = 740

        self.image = pygame.Surface([40,40])

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):

        self.rect.y += self.speed

        if self.rect.center[1] > 740:
            self.song.previous_note_hit = False
        elif self.rect.y >900:
            self.song.note_list.remove(self)
            self.kill()


class Song:

    def __init__(self, filename):

        self.chart = filename
        self.song_name = ''
        self.audio_stream = None

        self.resolution = 0
        self.hopo_distance = 0
        self.offset = 0
        self.bpm = 0
        self.bps = 0
        self.tps = 0
        self.tpf = 0
        self.previous_tick = 0
        self.current_tick = 0

        self.pixels_per_second = 240
        self.pixels_per_beat = 0
        
        self.current_bpm = 0
        self.bpm_dict = {}

        self.previous_note_hit = False

        self.note_list = []
        self.loaded_notes = []

    def load_chart(self):
        with open(self.chart, 'rb') as infile:
            for line in infile:
                line = line.strip()
                if 'AudioStream' in line:
                    self.song_name = line[14:]
                    self.audio_stream = pygame.mixer.Sound(self.song_name)
                elif 'Resolution' in line:
                    self.resolution = int(line[13:])
                    self.hopo_distance = (65*self.resolution) / 192
                    print self.hopo_distance
                elif 'Offset' in line:
                    self.offset = float(line[9:])
                elif 'BPM' in line:
                    self.bpm = int(line[6:])
                elif ' N ' in line:
                    line = line.split(' ')
                    tick = int(line[0])
                    note_type = int(line[3])
                    color = ''
                    note_beat = (tick / float(self.resolution)) + self.offset
                    pixels_per_beat = (self.bpm/60.0) * 240
                    note_y = 720.0 - (note_beat * pixels_per_beat)
                    #print note_beat, note_y
                    if note_type == 0:
                        color = 'green'
                        self.note_list.append(Note(tick, note_y/5.2, color, self))
                    elif note_type == 1:
                        color = 'red'
                        self.note_list.append(Note(tick, note_y/5.2, color, self))
                    elif note_type == 2:
                        color = 'yellow'
                        self.note_list.append(Note(tick, note_y/5.2, color, self))
                    elif note_type == 3:
                        color = 'blue'
                        self.note_list.append(Note(tick, note_y/5.2, color, self))
                    elif note_type == 4:
                        color = 'orange'
                        self.note_list.append(Note(tick, note_y/5.2, color, self))
                    elif note_type == 5:
                        if self.note_list[-1].hopo == True:
                            self.note_list[-1].hopo = False
                        else:
                            self.note_list[-1].hopo = True

        self.bps = self.bpm / 60.0
        self.tps = self.bps * self.resolution
        self.tpf = self.tps / 60.0
        #self.pixels_per_beat = self.bps * self.pixels_per_second

    def update(self):

        self.previous_tick = self.current_tick
        self.current_tick += self.tpf

        

        
                    
                    

        

class Fret(pygame.sprite.Sprite):

    def __init__(self, x, y, color, num, game):
        pygame.sprite.Sprite.__init__(self)

        self.num = num

        self.x = x
        self.y = y
        self.color = color

        self.image = pygame.Surface([50,50])

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.pressed = False
        self.game = game


    def check_for_strum(self):

        note_hit_list = pygame.sprite.spritecollide(self, self.game.song.note_list, False)

        for note in note_hit_list:
            if note.rect.center[1] > 700 and note.rect.center[1] < 740:
                for fret in self.game.frets:
                    if not fret.num > self.num and fret.pressed and note in self.game.song.note_list:
                        self.game.song.note_list.remove(note)
                        self.game.song.previous_note_hit = True

    def check_for_hopo(self):

        note_hit_list = pygame.sprite.spritecollide(self, self.game.song.note_list, False)

        for note in note_hit_list:
            if note.rect.center[1] > 700 and note.rect.center[1] < 740:
                if note.hopo == True and self.game.song.previous_note_hit == True and self.pressed == True:
                    for fret in self.game.frets:
                        if not fret.num > self.num and fret.pressed and note in self.game.song.note_list:
                            self.game.song.note_list.remove(note)
                            self.game.song.previous_note_hit = True

class GameMain():

    done = False
    color_bg = Color('black')

    def __init__(self, width=1280, height=800):
        
        pygame.mixer.pre_init(44100,-16,2,2048)
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.song = Song('thestage.chart')
        self.song.load_chart()

        self.frets = pygame.sprite.Group()
        self.fret0 = Fret(540, 720, Color('green'), 0, self)
        self.fret1 = Fret(590, 720, Color('red'), 1, self)
        self.fret2 = Fret(640, 720, Color('yellow'), 2, self)
        self.fret3 = Fret(690, 720, Color('blue'), 3, self)
        self.fret4 = Fret(740, 720, Color('orange'), 4, self)

        self.frets.add(self.fret0, self.fret1, self.fret2, self.fret3, self.fret4)

        self.song.audio_stream.play()
        

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.song.update()
            for note in self.song.note_list:
                note.update()
            for fret in self.frets:
                fret.check_for_hopo()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

        for fret in self.frets:
            pygame.draw.circle(self.screen, fret.color, fret.rect.center, 25)
            if fret.pressed:
                pygame.draw.circle(self.screen, Color('black'), fret.rect.center, 15)

        for note in self.song.note_list[0:1000]:
            pygame.draw.circle(self.screen, Color(note.color), note.rect.center, 20)
            if note.hopo == True:
                pygame.draw.circle(self.screen, Color('white'), note.rect.center, 10)
                
        

        pygame.display.flip() #put all the work on the screen

    def handle_events(self):

        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.done = True
                elif event.key == K_a:
                    self.fret0.pressed = True
                elif event.key == K_s:
                    self.fret1.pressed = True
                elif event.key == K_d:
                    self.fret2.pressed = True
                elif event.key == K_f:
                    self.fret3.pressed = True
                elif event.key == K_g:
                    self.fret4.pressed = True
                elif event.key == K_LEFT or event.key == K_RIGHT:
                    for fret in self.frets:
                        if fret.pressed:
                            fret.check_for_strum()
            elif event.type == KEYUP:
                if event.key == K_a:
                    self.fret0.pressed = False
                elif event.key == K_s:
                    self.fret1.pressed = False
                elif event.key == K_d:
                    self.fret2.pressed = False
                elif event.key == K_f:
                    self.fret3.pressed = False
                elif event.key == K_g:
                    self.fret4.pressed = False

if __name__ == '__main__':
    game = GameMain()
    game.main_loop()


#notes to self because I'm not smart:
    #Note position is in ticks
    #Resolution is ticks per beat
    #Notes are moving at 4 pixels/frame, for 240 pixels/second
    #Bpm is beats per minute, divide by 60 to get beats per second
    #To get the beat that the note is on divide its position by resolution,
    # then multiply beat by 240 (pixels/second) and add some amount to get y position.
    #I don't know why I couldn't figure this out earlier.

















