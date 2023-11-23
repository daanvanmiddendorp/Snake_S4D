import pygame, sys, random
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.x = random.randint(
            0, cell_number - 1
        )  # random x position -1 because 0 to 19 is 20 numbers
        self.y = random.randint(
            0, cell_number - 1
        )  # random x position -1 because 0 to 19 is 20 numbers
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.pos.x * cell_size),
            int(self.pos.y * cell_size),
            cell_size,
            cell_size,
        )
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()  # kan worden verwijderd in while loop -> if event.type == SCREEN_UPDATE

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)] # snake body
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body: # for every block in the body list
            x_pos = int(block.x * cell_size) # x position of the block
            y_pos = int(block.y * cell_size) # y position of the block
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size) # create a rectangle
            pygame.draw.rect(screen,(183,111,122),block_rect)

    def move_snake(self):
        body_copy = self.body[:-1] # copy the body list without the last element
        body_copy.insert(0,body_copy[0] + self.direction) # insert a new element at the beginning of the list
        self.body = body_copy[:] # copy the body_copy list to the body list


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()


# fruit = FRUIT() # niet meer nodig
main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT #user event is a custom event 
pygame.time.set_timer(SCREEN_UPDATE,150) # this event will be triggered every 150 milliseconds

# event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (
            event.type == SCREEN_UPDATE
        ):  # de maker van de while loop moet deze aanpassing doorvoeren, deze wordt namelijk later in de video gedaan
            main_game.update()

    screen.fill((175, 215, 70))
    # fruit.draw_fruit()  # from class FRUIT draw_fruit method in while loop --- is niet meer nodig, wordt in de main class gedaan. zelfde verhaal bij snake die straks wordt gemaakt door iemand
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
