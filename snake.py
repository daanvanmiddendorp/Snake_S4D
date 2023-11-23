import pygame, sys, random
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.pos.x * cell_size),
            int(self.pos.y * cell_size),
            cell_size,
            cell_size,
        )
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]  # snake body
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:  # for every block in the body list
            x_pos = int(block.x * cell_size)  # x position of the block
            y_pos = int(block.y * cell_size)  # y position of the block
            block_rect = pygame.Rect(
                x_pos, y_pos, cell_size, cell_size
            )  # create a rectangle
            pygame.draw.rect(screen, (183, 111, 122), block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.new_block = False
        else:
            body_copy = self.body[:-1]  # copy the body list without the last element
            body_copy.insert(
                0, body_copy[0] + self.direction
            )  # insert a new element at the beginning of the list
            self.body = body_copy[:]  # copy the body_copy list to the body list

    def add_block(self):
        self.new_block = True


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()  # call the move_snake method so every 150 milliseconds the snake moves
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()  # from class FRUIT draw_fruit method in while loop
        self.snake.draw_snake()  # from class SNAKE draw_snake method in while

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # als fruit positie gelijk is aan positie 0 van snake, dus hoofd
            # print("jummie")
            self.fruit.randomize()
            self.snake.add_block()


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT  # user event is a custom event
pygame.time.set_timer(
    SCREEN_UPDATE, 150
)  # this event will be triggered every 150 milliseconds

# event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:  # if the event is triggered
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)  # move up -1 in y axis
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)  # move down 1 in y axis
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)  # move left -1 in x axis
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)  # move right 1 in x axis

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
