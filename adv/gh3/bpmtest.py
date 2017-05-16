import pygame, random, math, pygbutton, time

from pygame.locals import *


class Note(pygame.sprite.Sprite):

    def __init__(self, tick, y, color, chord, game, sustain, sustain_tick):
        pygame.sprite.Sprite.__init__(self)

        self.tick = tick
        self.color = color
        self.game = game
        self.hopo = False
        if chord:
            self.hopo = self.game.song.note_list[-1].hopo
        else:
            if len(self.game.song.note_list) == 0:
                self.hopo = False
            else:
                if self.tick - self.game.song.note_list[-1].tick <= self.game.song.hopo_distance:
                    if self.game.song.note_list[-1].color != self.color:
                        self.hopo = True
        self.sustain_y = sustain
        self.sustain_tick = sustain_tick
        self.sustain = False
        if self.sustain_y != 0:
            self.sustain = True
        self.held = False
        self.speed = 6
        self.dead = False
        self.chord = chord
        self.missed = False

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
        if self.sustain:
            self.sustain_y += self.speed

        if self.rect.center[1] > 830 and not self.dead:
            if self.sustain != 0:
                if self.sustain_y > 830:
                    self.game.song.loaded_notes.remove(self)
                    self.dead = True
                    self.kill()
                    self.game.multiplier = 1
                    self.game.partial_multiplier = 0
            else:
                self.game.song.loaded_notes.remove(self)
                self.dead = True
                self.kill()
        elif self.rect.center[1] > 740 and not self.dead and self in self.game.song.loaded_notes:
            if self.missed == False:
                self.game.song.previous_note_hit = False
                self.missed = True
                self.game.multiplier = 1
                self.game.partial_multiplier = 0


class Song:

    def __init__(self, filename, game):

        self.chart = filename
        self.song_name = ''
        self.audio_stream = None
        self.game = game

        self.resolution = 0
        self.hopo_distance = 0
        self.offset = 0
        self.bpm = 0
        self.divisor = 0
        self.bps = 0
        self.tps = 0
        self.tpf = 0
        self.current_y = 0
        self.current_tick = 0

        self.pixels_per_second = 240
        self.pixels_per_beat = 0
        
        self.current_bpm = 0
        self.current_bpm_tick = 0
        self.bpm_list = []

        self.previous_note_hit = False

        self.note_list = []
        self.loaded_notes = []

        self.done = False
        self.time = 0

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
                    #print self.hopo_distance
                elif 'Offset' in line:
                    self.offset = float(line[9:])
                #elif 'BPM' in line:
                 #   self.bpm = int(line[6:])
                elif 'Divisor' in line:
                    self.divisor = float(line[10:])
                    #print self.divisor
                elif ' B ' in line:
                    line = line.split(' ')
                    tick = int(line[0])
                    bpm = int(line[-1]) / 1000.0
                    self.bpm_list.append((tick, bpm))
                elif ' N ' in line:
                    line = line.split(' ')
                    tick = int(line[0])
                    note_type = int(line[3])
                    color = ''
                    note_beat = (tick / float(self.resolution)) + self.offset
                    pixels_per_beat = (self.bpm/60.0) * 360
                    note_y = (720.0 - (note_beat * pixels_per_beat)) / self.divisor
                    chord = False
                    sustain = 0
                    if int(line[-1]):
                        sustain = int(line[-1]) + tick
                        sustain_end_beat = (sustain / float(self.resolution)) + self.offset
                        sustain = (720.0 - (sustain_end_beat * pixels_per_beat)) / self.divisor
                        sustain = int(round(sustain))
                        #print sustain
                    if len(self.note_list) != 0:
                        if tick == self.note_list[-1].tick and note_type != 5:
                            chord = True
                            self.note_list[-1].chord = True
                        else:
                            chord = False
                    sustain_tick = int(line[-1])
                    #print note_beat, note_y
                    if note_type == 0:
                        color = 'green'
                        self.note_list.append(Note(tick, note_y, color, chord, self.game, sustain, sustain_tick))
                    elif note_type == 1:
                        color = 'red'
                        self.note_list.append(Note(tick, note_y, color, chord, self.game, sustain, sustain_tick))
                    elif note_type == 2:
                        color = 'yellow'
                        self.note_list.append(Note(tick, note_y, color, chord, self.game, sustain, sustain_tick))
                    elif note_type == 3:
                        color = 'blue'
                        self.note_list.append(Note(tick, note_y, color, chord, self.game, sustain, sustain_tick))
                    elif note_type == 4:
                        color = 'orange'
                        self.note_list.append(Note(tick, note_y, color, chord, self.game, sustain, sustain_tick))
                    elif note_type == 5:
                        if self.note_list[-1].hopo == True:
                            self.note_list[-1].hopo = False
                        else:
                            self.note_list[-1].hopo = True

        self.bps = self.bpm / 60.0
        self.tps = self.bps * self.resolution
        self.tpf = self.tps /60.0
        #print self.tpf
        print self.bpm_list

    def update(self):

        self.current_y -= 6
        self.current_tick += self.tpf*1.04
        #The *1.04 is needed because the game generally runs at 58 FPS, and was falling behind
        self.current_tick
        for note in self.note_list:
            #if self.current_y - 2000 <= note.rect.center[1] and note.dead == False and note not in self.loaded_notes:
            if self.current_tick + (self.resolution*10) >= note.tick and note.dead == False and note not in self.loaded_notes:
                self.loaded_notes.append(note)
        for note in self.loaded_notes:
            if note.dead:
                self.loaded_notes.remove(note)


        if self.note_list[-1].dead and not self.done:
            self.audio_stream.fadeout(3000)
            self.done = True
            self.time = time.time()

        if self.done:
            if time.time() - self.time > 5:
                self.game.song_over = True
            

        

        
                    
                    

        

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

        self.held_note = None
        self.held_note_s_y = None


    def check_for_strum(self):

        note_hit_list = pygame.sprite.spritecollide(self, self.game.song.loaded_notes, False)

        for note in note_hit_list:
            if note.rect.center[1] > 700 and note.rect.center[1] < 740 and note in self.game.song.loaded_notes:
                if note.chord:
                    note.dead = True
                    self.game.song.previous_note_hit = True
                    self.game.score += 50 * self.game.multiplier
                    self.game.partial_multiplier += 1
                else:
                    for fret in self.game.frets:
                        if fret.pressed and fret.num > self.num:
                            break
                    else:
                        note.dead = True
                        self.game.song.previous_note_hit = True
                        self.game.score += 50 * self.game.multiplier
                        self.game.partial_multiplier += 1
                if note.sustain != 0 and self.pressed:
                    note.held = True
                    self.held_note = note

    def update(self):

        note_hit_list = pygame.sprite.spritecollide(self, self.game.song.loaded_notes, False)

        for note in note_hit_list:
            if note.rect.center[1] > 700 and note.rect.center[1] < 740 and note in self.game.song.loaded_notes:
                if note.hopo == True and self.game.song.previous_note_hit == True and self.pressed == True:
                    if note.chord:
                        note.dead = True
                        self.game.song.previous_note_hit = True
                        self.game.score += 50 * self.game.multiplier
                        self.game.partial_multiplier += 1
                    else:
                        for fret in self.game.frets:
                            if fret.pressed and fret.num > self.num:
                                break
                        else:
                            note.dead = True
                            self.game.song.previous_note_hit = True
                            self.game.score += 50 * self.game.multiplier
                            self.game.partial_multiplier += 1
                    if note.sustain != 0 and self.pressed:
                        note.held = True
                        self.held_note = note
                        #self.held_note_s_y = note.sustain_y

        #if self.held_note != None:
         #   self.held_note_s_y += 6

        if self.held_note != None:
            self.game.score += 2 * self.game.multiplier
            if self.held_note.sustain_y  > 720:
                self.held_note = None
            if not self.pressed:
                self.held_note = None
        if self.game.partial_multiplier >= 9:
            self.game.partial_multiplier = 0
            if self.game.multiplier != 4:
                self.game.multiplier += 1
            
                

class GameMain():

    done = False
    color_bg = Color('black')

    def __init__(self, chart, width=1280, height=800):
        
        pygame.mixer.pre_init(44100,-16,2,2048)
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.chart = chart
        self.song = Song(self.chart, self)
        self.song.load_chart()

        self.frets = pygame.sprite.Group()
        self.fret0 = Fret(540, 720, Color('green'), 0, self)
        self.fret1 = Fret(590, 720, Color('red'), 1, self)
        self.fret2 = Fret(640, 720, Color('yellow'), 2, self)
        self.fret3 = Fret(690, 720, Color('blue'), 3, self)
        self.fret4 = Fret(740, 720, Color('orange'), 4, self)

        self.frets.add(self.fret0, self.fret1, self.fret2, self.fret3, self.fret4)

        self.score = 0
        self.multiplier = 1
        self.partial_multiplier = 0
    
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.score_text = self.font.render('0', True, Color('white'))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.center = (940, 400)

        self.multiplier_text = self.font.render('x1', True, Color('white'))
        self.multiplier_text_rect = self.score_text.get_rect()
        self.multiplier_text_rect.center = (940, 500)

        self.partial_text = self.font.render('', True, Color('white'))
        self.partial_text_rect = self.partial_text.get_rect()
        self.partial_text_rect.center = (940, 530)

        self.song.audio_stream.play()

        self.song_over = False
        

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.song.update()
            for note in self.song.note_list:
                note.update()
            for fret in self.frets:
                fret.update()
            self.draw()
            self.clock.tick(60)
            #print len(self.song.loaded_notes)
            print self.clock.get_fps()
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

        if not self.song_over:

            for fret in self.frets:
                pygame.draw.circle(self.screen, fret.color, fret.rect.center, 25)
                if fret.held_note != None:
                    pygame.draw.line(self.screen, fret.color, fret.rect.center, (fret.rect.center[0],fret.held_note.sustain_y), 3) 
                if fret.pressed:
                    pygame.draw.circle(self.screen, Color('black'), fret.rect.center, 15)

            for note in self.song.loaded_notes:
                pygame.draw.circle(self.screen, Color(note.color), note.rect.center, 20)
                if note.sustain:
                    if not note.held:
                        pygame.draw.line(self.screen, Color(note.color), note.rect.center, (note.rect.center[0], note.sustain_y))
                if note.hopo == True:
                    pygame.draw.circle(self.screen, Color('white'), note.rect.center, 10)


            self.score_text = self.font.render('{}'.format(self.score), True, Color('white'))
            self.screen.blit(self.score_text, self.score_text_rect)

            self.multiplier_text = self.font.render('x{}'.format(self.multiplier), True, Color('white'))
            self.screen.blit(self.multiplier_text, self.multiplier_text_rect)

            if self.multiplier == 4:
                self.partial_multiplier = 8
            self.partial_text = self.font.render('I'*self.partial_multiplier, True, Color('white'))
            self.screen.blit(self.partial_text, self.partial_text_rect)

            pygame.draw.line(self.screen, Color('green'), (1015, 517), (1015, 539.5), 4)

        else:

            self.final_score_text = self.font.render('Final Score: {}'.format(self.score), True, Color('blue'))
            self.final_score_rect = self.final_score_text.get_rect()
            self.final_score_rect.center = (self.width/2, self.height/2 - 50)

            self.play_again_text = self.font.render('Press A or Green to return to menu', True, Color('green'))
            self.play_again_rect = self.play_again_text.get_rect()
            self.play_again_rect.center = (self.width/2, self.height/2)

            self.quit_text = self.font.render('Press S or Red to quit', True, Color('red'))
            self.quit_rect = self.quit_text.get_rect()
            self.quit_rect.center = (self.width/2, self.height/2 + 50)
            
            self.screen.blit(self.final_score_text, self.final_score_rect)
            self.screen.blit(self.play_again_text, self.play_again_rect)
            self.screen.blit(self.quit_text, self.quit_rect)
                
        

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
                    if self.song_over:
                        menu = Menu()
                        menu.main_loop()
                elif event.key == K_s:
                    self.fret1.pressed = True
                    if self.song_over:
                        self.done = True
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




class Menu():

    done = False
    color_bg = Color('gray30')

    def __init__(self, width=800, height=600):

        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.thestage = pygbutton.PygButton((325, 125, 150, 50), 'The Stage')
        self.thestage.bgcolor = Color('green')
        self.cliffs = pygbutton.PygButton((325, 225, 150, 50), 'Cliffs of Dover')
        self.cliffs.bgcolor = Color('red')
        self.hail = pygbutton.PygButton((325, 325, 150, 50), 'Hail to the King')
        self.hail.bgcolor = Color('yellow')
        self.peace = pygbutton.PygButton((325, 425, 150, 50), 'Peace of Mind')
        self.peace.bgcolor = Color('blue')

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)

        self.thestage.draw(self.screen)
        self.cliffs.draw(self.screen)
        self.hail.draw(self.screen)
        self.peace.draw(self.screen)

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
                    game = GameMain('thestage.chart')
                    game.main_loop()
                elif event.key == K_s:
                    game = GameMain('cliffs.chart')
                    game.main_loop()
                elif event.key == K_d:
                    game = GameMain('hail.chart')
                    game.main_loop()
                elif event.key == K_f:
                    game = GameMain('peaceofmind.chart')
                    game.main_loop()

            if 'click' in self.thestage.handleEvent(event):
                game = GameMain('thestage.chart')
                game.main_loop()
            if 'click' in self.cliffs.handleEvent(event):
                game = GameMain('cliffs.chart')
                game.main_loop()
            if 'click' in self.hail.handleEvent(event):
                game = GameMain('hail.chart')
                game.main_loop()
            if 'click' in self.peace.handleEvent(event):
                game = GameMain('peaceofmind.chart')
                game.main_loop()


if __name__ == '__main__':
    menu = Menu()
    menu.main_loop()
    #game = GameMain('thestage.chart')
    #game.main_loop()

#notes to self because I'm not smart:
    #Note position is in ticks
    #Resolution is ticks per beat
    #Notes are moving at 6 pixels/frame, for 360 pixels/second
    #Bpm is beats per minute, divide by 60 to get beats per second
    #To get the beat that the note is on divide its position by resolution,
    # then multiply beat by 240 (pixels/second) and add some amount to get y position.
    #I don't know why I couldn't figure this out earlier.

















