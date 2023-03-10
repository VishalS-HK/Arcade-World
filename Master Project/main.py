import pygame
import time
from pygame.locals import *
import time
import random

SIZE=40
pause=True

class Apple:
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.image=pygame.image.load("resources/apple.jpg").convert()
        self.x=120
        self.y=120

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x=random.randint(1,12)*SIZE
        self.y=random.randint(1,8)*SIZE
        

class Snake:
    def __init__(self,parent_screen,length):
        self.length=length
        self.parent_screen=parent_screen
        self.block=pygame.image.load("resources/block.jpg").convert()
        self.x=[SIZE]*length
        self.y=[SIZE]*length
        self.direction="down"

    def inc_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((110,110,5))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction="left"

    def move_right(self):
        self.direction="right"

    def move_up(self):
        self.direction="up"

    def move_down(self):
        self.direction="down"

    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        if self.direction=="up":
            self.y[0]-=40
        if self.direction=="down":
            self.y[0]+=40
        if self.direction=="right":
            self.x[0]+=40
        if self.direction=="left":
            self.x[0]-=40
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode((750,500))
        self.surface.fill((110,110,5))
        self.snake=Snake(self.surface,1)
        self.snake.draw()
        self.apple=Apple(self.surface)
        self.apple.draw()
    #snake colliding with apple
    def is_collision(self,x1,y1,x2,y2):
        if x1>=x2 and x1<x2+SIZE:
            if y1>=y2 and y1<y2+SIZE:
                return True

    def display_score(self):
        font=pygame.font.SysFont('arial',30)
        score=font.render(f"Score: {self.snake.length-1}",True,(255,255,255))
        self.surface.blit(score,(500,10))

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.apple.move()
            self.snake.inc_length()

        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                raise "Game Over"

    def show_game_over(self):     
        self.surface.fill((110,110,5))
        font=pygame.font.SysFont('arial',30)
        line1=font.render(f"Game is Over, Your Score: {self.snake.length-1}",True,(255,255,255))
        self.surface.blit(line1,(100,200))
        line2=font.render("To play again press Enter. To exit press Escape",True,(255,255,255))
        self.surface.blit(line2,(100,250))
        pygame.display.flip()
        
        
        
    def run(self):
            running=True
            pause=False

            while running:
                for event in pygame.event.get():
                    if event.type==KEYDOWN:
                        if event.key==K_ESCAPE:
                            running=False

                        if event.key==K_RETURN:
                            pause=False
                            self.snake.length=1
                        if event.key==K_ESCAPE:
                            pause=True
                            
                            self.show_game_over()
                        if event.key== K_UP:
                            self.snake.move_up()
                        if event.key== K_DOWN:
                            self.snake.move_down()
                        if event.key== K_LEFT:
                            self.snake.move_left()
                        if event.key== K_RIGHT:
                            self.snake.move_right()
                    
                    elif event.type==QUIT:
                        running=False
                try:
                    if not pause:
                        self.play()
                except Exception as e:
                    self.show_game_over()
                    pause=True
                time.sleep(0.25)
if __name__=="__main__":
    game=Game()
    game.run()
    
    


                
    
