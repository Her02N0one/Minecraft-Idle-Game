import pygame
import os

os.system('clear')

clock = pygame.time.Clock()
FPS = 60

width, height = (500, 500)
screen = pygame.display.set_mode((height, width))

square = pygame.Rect(((width/2)-128, (height/2)-128, 256, 256))
mousePos = pygame.Vector2()
running = True

grass_block = pygame.transform.scale(
    pygame.image.load("assets/sprites/grass_block.png"),
    (square.width, square.height)
)

wood = None
stone = None
iron = None
diamond = None

clicks = 0

print("item list bought for clicks:\n\
wood pick(100), stone(500), iron(1000), and diamond(10000)\n\
type the items material to buy")

# buy = input("you want buy?: ")

while running:
    clock.tick(FPS)
    dt = clock.get_time() / 1000

    mousePos.update(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if square.collidepoint(mousePos):
                clicks += 1
                os.system('clear')
                print("clicks:", clicks)

    screen.fill((255, 255, 255))

    screen.blit(grass_block, square)

    pygame.display.flip()
