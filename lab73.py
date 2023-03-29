import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = width, height = (400, 400)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()  
color = (RED)

x = 25
y = 25
dx = 0
dy = 0


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            dx = 0
            dy = -20 
            if y <= 25:
                y=25
            else:
                x += dx
                y += dy
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dx = 0
            dy = 20 
            if y >= height-25:
                y = height - 25
            else:
                x += dx
                y += dy
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            dx = -20
            dy = 0
            if x <= 25:
                x=25
            else:
                x += dx
                y += dy
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            dx = 20
            dy = 0
            if x >= width-25:
                x=width-25
            else:
                x += dx
                y += dy


    screen.fill(WHITE)
    

    

    pygame.draw.circle(screen, color, (x, y), 25)
    clock.tick(30)
    pygame.display.update()