import pygame
from pygame.locals import *
import random
import pygame.mixer
pygame.init()
display_width=1000
display_height=600
game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Pro-gamer")
bg=pygame.image.load('rocket.png')
bg=pygame.transform.scale(bg,(100,100))
ob=pygame.image.load('images.png')
ob=pygame.transform.scale(ob,(100,100))
x=0
y=500
width=100
height=100
vel=10
isJump=False
jumpcount=10
run = True
clock=pygame.time.Clock()
b=0
l=[0,200,400,600]
a=random.choice(l)
def car(x,y):
    game_display.blit(bg, (x,y))
    game_display.blit(ob, (a,b)) 
def obstacle(b):
    if(b<=height):
        b+=10
        update()
    #b=b+vel
    #while b <= display_height:
    #    return obstacle(500,b)
    #if(b>800):
     #   a=random.choice([0,100,200,350])
def update():
    pygame.display.update()
    clock.tick(60)
shot=pygame.mixer.Sound("shot.wav")
soundin=pygame.mixer.Sound("sound.wav")
soundin.play()
def shoot():
    keys=pygame.key.get_pressed()
    if(keys[pygame.K_ESC]):
            shot.play()
while run:                
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False 
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
    	if(x<=0):
            x+=vel
        else:
            x-=vel
    if keys[pygame.K_RIGHT]:
        if(x>=1000-width):
              x-=vel
        else:
              x+=vel
    if(b<display_height):
        b+=10
        update()
    if(b==display_height):
        b=0
        a=random.choice(l)
        update()
    if not (isJump):
        if(keys[pygame.K_UP] and y>vel):
              y-=vel
        if(keys[pygame.K_DOWN] and y<600-height-vel):
              y+=vel
        if keys[pygame.K_SPACE]:
               isJump=True
    else:
        if(jumpcount>= -10):
            neg=1
            if jumpcount<0:
                neg=-1
            y-=(jumpcount**2)*0.5*neg
            jumpcount-=1
        else:
            isJump=False
            jumpcount=10
    game_display.fill((255,218,195))
    car(x,y)
    #obstacle(b)
    #update()
    game_display.blit(ob, (500,0))
    pygame.display.update()
    #pygame.draw.rect(game_display,(0,191,255),(x,y,width,height)
pygame.quit()
        
