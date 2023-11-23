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


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()


# fruit = FRUIT() # niet meer nodig
main_game = MAIN()

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
