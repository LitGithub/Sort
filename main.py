import pygame #handles graphics, sound, game timings, keyboard input, etc
import random
pygame.init()

width = 1000

#creates game screen and caption
screen = pygame.display.set_mode((width, 500))
pygame.display.set_caption("Silly Shapes")
running = True

list = []
amount = 50
for x in range(0, amount):
    list.append(random.randrange(0, 500))
    
def draw():
    screen.fill((0, 0, 0))
    for x in range(len(list)):
        pygame.draw.rect(screen, (255, 255, 255), (((width / amount) * x), 500-list[x], (width / amount), list[x]))
    pygame.display.flip() #update graphics

while running: #sortof a game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(1, len(list)):
        j = i - 1
        draw()
        if(list[i] < list[j]):
            list[i], list[j] = list[j], list[i]
        pygame.draw.rect(screen, (255, 0, 0), (((width / amount) * i), 500-list[i], (width / amount), list[i]))
        pygame.draw.rect(screen, (255, 0, 0), (((width / amount) * j), 500-list[j], (width / amount), list[j]))
        pygame.display.flip()
            
pygame.quit()
