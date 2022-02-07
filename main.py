
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
    list.append(random.randrange(10, 500))
    
def draw():
    screen.fill((0, 0, 0))
    i = 0
    for x in list:
        pygame.draw.rect(screen, (255, 255, 255), (((width / amount) * i), 0, (width / amount), x))
        i+=1
    pygame.display.flip() #update graphics
while running: #sortof a game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(len(list)):
        for j in range(len(list)):
            if i < 49:
                j = i + 1
            draw()
            if(list[i] < list[j]):
                #print(i, j)
                list[i], list[j] = list[j], list[i]
            pygame.draw.rect(screen, (255, 0, 0), (((width / amount) * i), 0, (width / amount), list[i]))
            pygame.draw.rect(screen, (255, 0, 0), (((width / amount) * j), 0, (width / amount), list[j]))
            pygame.display.flip()
            
pygame.quit()
