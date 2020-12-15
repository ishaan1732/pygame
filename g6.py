import pygame
from pygame.locals import *
import random
import time

pygame.display.set_caption("Pro-gamer")

pygame.init()

class Game:
    def __init__(self):
        self.display_width=600
        self.display_height=600

        self.game_display = pygame.display.set_mode((self.display_width,self.display_height))
        self.bg=pygame.image.load('rocket.png')
        self.bg=pygame.transform.scale(self.bg,(100,100))
        self.ob=pygame.image.load('Rocket1.png')
        self.ob=pygame.transform.scale(self.ob,(100,100))
        #self.bu=pygame.image.load('bullets.jpg')
        #self.bu=pygame.transform.scale(self.bu,(50,50))
        self.wl=pygame.image.load('backg.png')
        self.wl=pygame.transform.scale(self.wl ,(360,600))
        self.color=pygame.image.load('black.png')
        self.color=pygame.transform.scale(self.color ,(120,600))
        #self.cr=pygame.image.load('crash.png')
        #self.cr=pygame.transform.scale(self.cr ,(50,50))

        self.x=120
        self.y=500
        self.height=100
        self.width=100
        self.vel=10

        self.clock=pygame.time.Clock()

        self.l=[120,150,200,250,300,350,380]
        self.a=random.choice(self.l)
        self.b=0

        self.c=self.x
        self.d=self.y-100

        self.e=random.choice(self.l)
        self.f=0

        self.acc=10
        self.acc1=10
        self.score=0

        self.run=True
        self.over=True
        self.exit=False

    def car(self):
        self.game_display.blit(self.color, (0,0))
        self.game_display.blit(self.color, (480,0))
        self.game_display.blit(self.wl, (120,0))
        self.game_display.blit(self.bg, (self.x,self.y))
        self.game_display.blit(self.ob, (self.a,self.b))
        #self.game_display.blit(self.ob, (self.e,self.f))

    def update(self):
        pygame.display.update()
        self.clock.tick(60)

    def display_score(self):
        self.myfont=pygame.font.Font("freesansbold.ttf",20)
        self.scoretext=self.myfont.render("score= "+str(self.score),1,(0,191,255))
        self.game_display.blit(self.scoretext, (0,0))
        self.update()
    
    def text_objects(self,text):
	textSurface=self.myfont.render(text,True,(0,191,255))
	return textSurface,textSurface.get_rect()
    
    def message_display(self,text):
        self.largetext=pygame.font.Font('freesansbold.ttf',30)
	self.TextSurf,self.TextRect=self.text_objects(text)
	self.TextRect.center=((self.display_width/2),(self.display_height/2))
	self.game_display.blit(self.TextSurf,self.TextRect)
	self.update()

    def movement(self):
        #while self.over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.run=False
            self.keys=pygame.key.get_pressed()
            if(self.score<=50):
                self.vel=10
            elif(self.score>=50 and self.score<=100):
                self.vel=15
            elif(self.score>=100):
                self.vel=20
            if self.keys[pygame.K_LEFT] and self.x>=120:
                    self.x-=self.vel
            if self.keys[pygame.K_RIGHT] and self.x<=480-self.width:
                    self.x+=self.vel
            if self.keys[pygame.K_ESCAPE]:
                self.run=False
            self.car()
            self.obstacle()
            self.display_score()
            self.gameover_condition()
            #self.gameover()
            #self.update()
    
    def obstacle(self):
        if(self.b<self.display_height):
            self.b+=self.acc
            self.update()
        if(self.b>=self.display_height):
            self.b=0
            self.a=random.choice([120,180,240,self.x,320,380])
            self.score+=5
            self.acc+=2
            #self.vel1+=self.acc1
            self.update()
    def gameover_condition(self):
        if((self.a>self.x-50 and self.a<=self.x+40) and (self.b<=self.y+100 and self.y<self.b)):
            #self.over=True
    #def gameover(self):
            self.game_display.fill((255,255,255))
            self.message_display('Gameover Score= '+str(self.score))
            time.sleep(3)
            pygame.quit()
        #self.update()
    def gameloop(self):
        while self.run:
            self.movement()
            #while self.over:
            #    self.gameover()
g=Game()
g.gameloop()
