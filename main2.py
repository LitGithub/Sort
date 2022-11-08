from timeit import default_timer as timer
import pygame
import random
random.seed(239)
pygame.init()  
pygame.display.set_caption("rip")
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameloop = True
values = []

rows = 100
limit = 1000

def swap(list, a, b):
    tempA = list[a]
    list[a] = list[b]
    list[b] = tempA
    return list

def sort(): #bubblesort
    global values
    swapped = True
    n = len(values)
    while swapped:
        swapped = False
        for i in range(1, n):
            draw()
            if values[i - 1] > values[i]:
                values = swap(values, i - 1, i)
                swapped = True
   
def randomize():
    global values
    values = []
    for x in range(0, rows):
        values.append(random.randint(0, limit))
    print(values)
pressed = False
def events():
    global pressed
    global gameloop
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
                pygame.quit()
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        randomize()
    if mouse[2] and not pressed:
        start = timer()
        sort()
        end = timer()
        print(f"Finished Sorting after {end-start} seconds")
        pressed = True
    if not mouse[2] and pressed:
        pressed = False
def draw():
    screen.fill((0,0,0))
    for x in range(len(values)):
            position = (x*(1000/rows), limit-values[x]*(1000/limit))
            size = ((1000/rows), values[x]*rows)
            if x % 2:
                color = (120,120,120)
            else:
                color = (120,0,120)
            pygame.draw.rect(screen, color, (position, size))
    pygame.display.flip()

def main():
    randomize()
    while gameloop:
        events()
        draw()


main()
