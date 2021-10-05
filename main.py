import sys
import pygame

colors = {}
screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
speed = [1, 1]


def initialize():
    colors['black'] = (0, 0, 0)
    colors['white'] = (255, 255, 255)
    colors['blue'] = (0, 0, 255)
    colors['red'] = (255, 0, 0)
    colors['green'] = (0, 255, 0)

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    
    return screen


def main():
    screen = initialize()
    active = True

    ball = pygame.image.load("intro_ball.gif")
    ballrect = ball.get_rect()

    coords = [screen_width / 2, screen_height / 2]
    move = .25

    pygame.draw.circle(screen, colors['blue'], coords, 10)
    

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            
        if pygame.key.get_pressed()[pygame.K_a]:
            screen.fill(colors['black'])
            coords[0] -= move
            pygame.draw.circle(screen, colors['blue'], coords, 10)
            
        elif pygame.key.get_pressed()[pygame.K_w]:
            screen.fill(colors['black'])
            coords[1] -= move
            pygame.draw.circle(screen, colors['blue'], coords, 10)
            
        elif pygame.key.get_pressed()[pygame.K_s]:
            screen.fill(colors['black'])
            coords[1] += move
            pygame.draw.circle(screen, colors['blue'], coords, 10)
            
        elif pygame.key.get_pressed()[pygame.K_d]:
            screen.fill(colors['black'])
            coords[0] += move
            pygame.draw.circle(screen, colors['blue'], coords, 10)
        
        pygame.display.update()

            
        """if ballrect.left < 0 or ballrect.right > screen_width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > screen_height:
            speed[1] = -speed[1]"""
    
        #screen.fill(colors['black'])
        #screen.blit(ball, ballrect)
        #screen.blit(screen, circle1)
        #pygame.display.flip()
    

if __name__ == '__main__':
    main()
    