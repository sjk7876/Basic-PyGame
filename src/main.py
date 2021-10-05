import random
import pygame

if not pygame.font: print('Warning, fonts disabled')

colors = {'black': (0, 0, 0),
          'white': (255, 255, 255),
          'red': (255, 0, 0),
          'green': (0, 255, 0),
          'blue': (0, 0, 255),
          'brownish': (169, 111, 53),
          'yellowish': (159, 135, 12),
          'pinkish': (255, 104, 175),
          'mint': (0, 191, 135),
          'purple': (89, 31, 97),
          'snot': (158, 234, 83)}
color_names = ('black', 'white', 'red', 'green', 'blue', 'brownish', 'yellowish', 'pinkish', 'mint', 'purple', 'snot')

screen_width = 1280
screen_height = 720
screen_size = (screen_width, screen_height)
speed = [1, 1]


def initialize():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	return screen


def movement(smileBox, move: int):
	if pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_w]:
		smileBox = smileBox.move(-move, -move)
	
	elif pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_s]:
		smileBox = smileBox.move(-move, move)
	
	elif pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed()[pygame.K_w]:
		smileBox = smileBox.move(move, -move)
	
	elif pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed()[pygame.K_s]:
		smileBox = smileBox.move(move, move)
	
	elif pygame.key.get_pressed()[pygame.K_a]:
		smileBox = smileBox.move(-move, 0)
	
	elif pygame.key.get_pressed()[pygame.K_w]:
		smileBox = smileBox.move(0, -move)
	
	elif pygame.key.get_pressed()[pygame.K_s]:
		smileBox = smileBox.move(0, move)
	
	elif pygame.key.get_pressed()[pygame.K_d]:
		smileBox = smileBox.move(move, 0)
	
	return smileBox


def hitEdge(smileBox2, smileBox):
	corner = False
	
	# y axis
	if smileBox.top < 0:
		smileBox2.y = smileBox.top + screen_height
		corner = True
	elif smileBox.bottom > screen_height:
		smileBox2.y = smileBox.top - screen_height
		corner = True
	else:
		smileBox2.y = smileBox.y
	
	# x axis
	if smileBox.left < 0:
		smileBox2.x = smileBox.left + screen_width
		corner = True
	elif smileBox.right > screen_width:
		smileBox2.x = smileBox.left - screen_width
		corner = True
	else:
		smileBox2.x = smileBox.x
	
	return smileBox2, corner


def main():
	screen = initialize()
	active, win, start, inStar, inStarPrev = True, False, False, False, False
	clockObject = pygame.time.Clock()
	collisions, frame, totalHits, move = 0, 0, 0, 5
	
	smile = pygame.image.load('smile_40x40.png').convert_alpha()
	star = pygame.image.load('star_15x16.png').convert_alpha()
	smileBox = smile.get_rect(centerx=screen.get_width() / 2, centery=screen.get_height() / 2)
	smileBox2 = smile.get_rect()
	
	enemiesXY = []
	
	for i in range(250):
		x = random.randint(0, screen_width)
		y = random.randint(0, screen_height)
		color = colors[color_names[random.randint(1, len(colors) - 1)]]
		enemiesXY.append([x, y, color])
	
	while not start:
		for i in enemiesXY:
			if smileBox.collidepoint(i[:2]):
				smileBox = smileBox.move(0, 10)
				start = False
				break
			else:
				start = True
	
	starXY = (random.randint(20, screen_width - 20), random.randint(20, screen_height - 20))
	
	while active:
		clockObject.tick(60)
		screen.fill(colors['black'])
		
		inStarPrev = inStar
		inStar = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				active = False
				
		if not win:
			screen.blit(star, starXY)
			
			smileBox = movement(smileBox, move)
			smileBox2, corner = hitEdge(smileBox2, smileBox)
			
			for i in enemiesXY:
				pygame.draw.circle(screen, i[2], i[:2], 3)
				if smileBox.collidepoint(i[:2]) or smileBox2.collidepoint(i[:2]):
					collisions += 1
					inStar = True
			
			if not inStar and inStarPrev:
				totalHits += 1
				
				for i in range(len(enemiesXY)):
					for j in range(2):
						enemiesXY[i][j] += random.randint(-5, 5)
			
			if smileBox.collidepoint(starXY) or smileBox2.collidepoint(starXY):
				win = True
			
			if frame < 30:
				if collisions > 1:
					frame += 1
					if pygame.font:
						font = pygame.font.Font('coolvetica rg.ttf', 36)
						text = font.render("You Got Hit!", True, colors['white'], (0, 0, 0))
						textpos = text.get_rect(centerx=screen.get_width() / 2)
						screen.blit(text, textpos)
			else:
				collisions = 0
				frame = 0
			
			if corner:
				screen.blit(smile, smileBox2)
			
			if smileBox.right < 0 or smileBox.left > screen_width or \
					smileBox.bottom < 0 or smileBox.top > screen_height:
				smileBox = smileBox2
			
			screen.blit(smile, smileBox)
			pygame.display.flip()
		if win:
			if pygame.font:
				font = pygame.font.Font('coolvetica rg.ttf', 36)
				font.set_underline(True)
				text = font.render("Congrats on winning the game!", True, colors['white'], (0, 0, 0))
				font.set_underline(False)
				text2 = font.render("# of Collisions: " + str(totalHits), True, colors['white'], (0, 0, 0))
				textpos = text.get_rect(centerx=screen.get_width() / 2, centery=screen.get_height() / 2)
				textpos2 = text.get_rect(centerx=screen.get_width() / 2, centery=(screen.get_height() / 2) + 50)
				screen.blit(text, textpos)
				screen.blit(text2, textpos2)
			
			pygame.display.flip()


if __name__ == '__main__':
	main()
