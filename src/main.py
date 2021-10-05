import pygame

colors = {'black': (0, 0, 0),
          'white': (255, 255, 255),
          'red': (255, 0, 0),
          'green': (0, 255, 0),
          'blue': (0, 0, 255)}
screen_width = 720
screen_height = 480
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
	active = True
	clockobject = pygame.time.Clock()
	move = 10
	
	smile = pygame.image.load('smile_40x40.png').convert_alpha()
	smileBox = smile.get_rect()
	smileBox2 = smile.get_rect()
	
	while active:
		clockobject.tick(60)
		screen.fill(colors['black'])
		corner = False
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				active = False
		
		smileBox = movement(smileBox, move)
		smileBox2, corner = hitEdge(smileBox2, smileBox)
		
		if corner:
			screen.blit(smile, smileBox2)
		
		if smileBox.right < 0 or smileBox.left > screen_width or \
				smileBox.bottom < 0 or smileBox.top > screen_height:
			smileBox = smileBox2
		
		screen.blit(smile, smileBox)
		pygame.display.flip()


if __name__ == '__main__':
	main()
