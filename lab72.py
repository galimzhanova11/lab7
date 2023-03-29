music =[
    'C:\\Users\User\Downloads\one direction.mp3',
    'C:\\Users\User\Downloads\tekke.mp3',
    'C:\\Users\User\Downloads\syko.mp3'
]

num = int(0)
cur = (music[num])
import pygame
from pygame import * 

mixer.init()
mixer.music.load(cur)

def play():
    mixer.music.play()

def stop():
    mixer.music.stop()

def next_song():
    global num
    global cur
    mixer.music.stop()
    if num == 2:
        cur = music[0]
        num=0
        mixer.music.load(cur)
    else:
        cur = music[num+1]
        num+=1
        mixer.music.load(cur)
    mixer.music.play()
    

def prev_song():
    global num
    global cur
    mixer.music.stop()
    if num == 0:
        cur = music[2]
        num=2
        mixer.music.load(cur)
    else:
        cur = music[num-1]
        num-=1
        mixer.music.load(cur)
    play()

pygame.init()
screen = pygame.display.set_mode((600, 400))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    play()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    stop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    next_song()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    prev_song()
                
                