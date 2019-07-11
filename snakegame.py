import pygame
import random
import time
import sys

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (150,0,0)
green = (0,100,0)
blue = (165, 197, 247)

bright_red = (255,0,0)
bright_green = (0,255,0)

pygame.init()

#essentials:
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

#tags:
pygame.display.set_caption('Snake Game')

#loaded files:
#bounce_sound = pygame.mixer.Sound("ballsound.wav")
game_sound = pygame.mixer.Sound("gamemenu.wav")
menu_sound = pygame.mixer.Sound("snakemusic.wav")
crash_sound = pygame.mixer.Sound("bloop_x.wav")
bite_sound = pygame.mixer.Sound("apple_bite.wav")
snakeImage = pygame.image.load('snake.png')
controlImage = pygame.image.load('controls.png')
ksnakeImage = pygame.image.load('ksnake.png')
appleImage = pygame.image.load('apple.png')
snImage = pygame.image.load('sni.jpg')

speed = 2
pause = False
mus = True
hs = 0

def quitgame(args = None):
	pygame.quit()
	sys.exit()

def snake(x,y):
	gameDisplay.blit(snakeImage, (x,y))

def ksnake(x,y):
	gameDisplay.blit(ksnakeImage, (x,y))

def sn(x,y):
	gameDisplay.blit(snImage, (x,y))	

def text_objects(text,font,color=black):
	textSurface = font.render(text,True,color)
	return textSurface, textSurface.get_rect()

def messege_display(text,size,x,y,color = black):
	largeText = pygame.font.SysFont(None,size)
	TextSurf, TextRect = text_objects(text,largeText,color)
	TextRect.center = ((x),(y))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()	
	if text == 'You Collided':
		pygame.display.update()
		time.sleep(2)
		gameloop()

def set_speed(s):
	#global snake
	global speed
	speed = s
	print(speed)

def button(msg,x,y,w,h,ic,ac,action=None,s = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x< mouse[0] < x + w and y< mouse[1] < y+h:
		pygame.draw.rect(gameDisplay,ac,(x,y,w,h))

		#pygame.mixer.Sound.play(bounce_sound)
		if click[0] == 1 and action != None:
			action(s)
	else:
		pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

	messege_display(msg,20,x+w/2,y+h/2,white)

def controls(args = None):
	gameDisplay.fill(blue)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
		gameDisplay.blit(controlImage, (50,50))
		button("BACK",650,500,100,30,green,bright_green,game_intro)
		pygame.display.update()
		clock.tick(15)

def toggle_music(args = None):
	global mus
	if mus == True:
		mus = False
		pygame.mixer.music.stop()
	else:
		mus = True
		pygame.mixer.music.play(-1)

def options(args = None):
	gameDisplay.fill(blue)
	print('options')
	global mus
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
		if mus == True:
			button("MUSIC: ON",300,100,150,50,green,bright_green,toggle_music)
		else:
			button("MUSIC: OFF",300,100,150,50,green,bright_green,toggle_music)
		button("BACK",150,500,100,40,green,bright_green,game_intro)
		pygame.display.update()
		clock.tick(15)



def levels(args = None):
	gameDisplay.fill(blue)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
		gameDisplay.fill(blue,[100,0,500,50])
		messege_display("LEVEL  :- "+str(speed-1),50,display_width/2-50,30)
		button("LEVEL 1",300,100,150,50,green,bright_green,set_speed,2)
		button("LEVEL 2",300,200,150,50,green,bright_green,set_speed,3)
		button("LEVEL 3",300,300,150,50,green,bright_green,set_speed,4)
		button("LEVEL 4",300,400,150,50,green,bright_green,set_speed,5)
		button("LEVEL 5",300,500,150,50,green,bright_green,set_speed,6)
		button("BACK",150,500,100,40,green,bright_green,game_intro)
		pygame.display.update()
		clock.tick(15)


def game_intro(args = None):
	#print('ehll')
	global mus
	if mus:
		pygame.mixer.music.load('gamemenu.wav')
		pygame.mixer.music.play(-1)
	gameDisplay.fill(blue)
	sn(00,00)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()

		messege_display("Snake Game",120,display_width/2,120,white)
		snake(600,400)
		ksnake(200,400)
		button('PLAY',50,350,150,30,green,bright_green,gameloop)
		button('CONTROLS',50,400,150,30,green,bright_green,controls)
		button('OPTIONS',50,450,150,30,green,bright_green,options)
		button('LEVELS',50,500,150,30,green,bright_green,levels)
		button('EXIT',50,550,150,30,red,bright_red,quitgame)
		pygame.display.update()
		clock.tick(15)

def over():

	#global pause
	pygame.mixer.music.stop()
	gameDisplay.fill(blue)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()

		messege_display("GAME OVER !!!",70,display_width/2,70)
		button("TRY AGAIN",150,450,100,50,green,bright_green,gameloop)
		button("MENU",350,450,100,50,green,bright_green,game_intro)
		button("QUIT",550,450,100,50,red,bright_red,quitgame)
		pygame.display.update()
		clock.tick(15)


def unpause(args = None):
	global pause
	pause = False

def paused():

	#global pause
	gameDisplay.fill(blue)
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()

		messege_display("PAUSED",70,display_width/2,70)
		button("CONTINUE",150,450,100,50,green,bright_green,unpause)
		button("MENU",350,450,100,50,green,bright_green,game_intro)
		button("QUIT",550,450,100,50,red,bright_red,quitgame)
		pygame.display.update()
		clock.tick(15)

def Snake(x,y):
	pygame.draw.rect(gameDisplay, bright_red, [x, y,15,15])

def display_food(x,y):
	gameDisplay.blit(appleImage, (x,y))

def gameloop(args = None):
	#print('hello')
	global mus
	if mus:
		pygame.mixer.music.load('snakemusic.wav')
		pygame.mixer.music.play(-1)

	x = 200
	y = 300
	fx = random.randrange(0,800)
	fy = random.randrange(0,600)
	eat = False
	direction = 'right'
	body = []
	body.insert(0,(x+7.5,y+7.5))
	body.insert(0,(x+7.5,y+7.5))
	body.insert(0,(x+7.5,y+7.5))
	body.insert(0,(x+7.5,y+7.5))
	score = 0
	global hs
	global pause
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and direction!='right':
					direction = 'left'
					#body.insert(1,(x+7.5,y+7.5))
				elif event.key == pygame.K_RIGHT and direction != 'left':
					direction = 'right'
					#body.insert(1,(x+7.5,y+7.5))
				elif event.key == pygame.K_UP and direction != 'down':
					direction = 'up'
					#body.insert(1,(x+7.5,y+7.5))
				elif event.key == pygame.K_DOWN and direction != 'up':
					direction = 'down'
					#body.insert(1,(x+7.5,y+7.5)) 
				elif event.key == pygame.K_SPACE:
					pause = True
					paused()

		gameDisplay.fill((7, 216, 0))
		if eat==True:
			display_food(fx,fy)
		else:
			fx = random.randrange(20,800-30)
			fy = random.randrange(20,600-30)
			eat = True
		if direction == 'left':
			x = x - speed
		elif direction == 'right':
			x = x + speed
		elif direction == 'down':
			y = y + speed
		elif direction == 'up':
			y = y - speed
		Snake(x,y)
		if (x+7.5,y+7.5) in body:
			pygame.mixer.Sound.play(crash_sound)
			pygame.mixer.music.stop()
			time.sleep(2)
			over()
		if x-10<=fx<=x+15 and y-10<=fy<=y+15:
			body.insert(1,(x+7.5,y+7.5))
			body.insert(1,(x+7.5,y+7.5))
			body.insert(1,(x+7.5,y+7.5))
			body.append(body[len(body)-1])
			score = score + 1
			pygame.mixer.Sound.play(bite_sound)
			#pygame.mixer.music.stop()
			eat = False
		if not((15<=x<=770) and (15<=y<=570)):
			pygame.mixer.Sound.play(crash_sound)
			pygame.mixer.music.stop()
			time.sleep(2)
			over()
		body.insert(0,(x+7.5,y+7.5))
		body.pop()
		pygame.draw.lines(gameDisplay,(0, 129, 216) , False, body, 5)
		pygame.draw.rect(gameDisplay, black, [10, 10,780,580],10)
		messege_display("SCORE: "+str(score),20,80,25)
		if hs<score:
			hs = score
		messege_display("HIGHEST SCORE: "+str(hs),20,80,50)
		pygame.display.update()
		clock.tick(60)

game_intro()
pygame.quit()
quit()


'''
Windows Fonts:
Agency FB
Algerian Regular
Arial
Arial Rounded MT Bold
Bell MT
Corbel
Courier New
Elephant New
Elephant
Edwardian Script ITC Regular
'''