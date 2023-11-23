import pygame, sys, random, os
from pygame.math import Vector2

snake_dir = os.path.dirname(__file__)  # main directory snake.py is in
graphics_dir = os.path.join(
    snake_dir, "graphics/"
)  # graphics directory is in main directory


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
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

        fruit_rect = pygame.Rect(
            int(self.pos.x * cell_size),
            int(self.pos.y * cell_size),
            cell_size,
            cell_size,
        )

        # pygame.draw.rect(screen,(126,166,114),fruit_rect)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]  # snake body
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load(graphics_dir + "head_up.png").convert_alpha()
        self.head_down = pygame.image.load(
            graphics_dir + "head_down.png"
        ).convert_alpha()
        self.head_right = pygame.image.load(
            graphics_dir + "head_right.png"
        ).convert_alpha()
        self.head_left = pygame.image.load(
            graphics_dir + "head_left.png"
        ).convert_alpha()

        self.tail_up = pygame.image.load(graphics_dir + "tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load(
            graphics_dir + "tail_down.png"
        ).convert_alpha()
        self.tail_right = pygame.image.load(
            graphics_dir + "tail_right.png"
        ).convert_alpha()
        self.tail_left = pygame.image.load(
            graphics_dir + "tail_left.png"
        ).convert_alpha()

        self.body_vertical = pygame.image.load(
            graphics_dir + "body_vertical.png"
        ).convert_alpha()
        self.body_horizontal = pygame.image.load(
            graphics_dir + "body_horizontal.png"
        ).convert_alpha()

        self.body_tr = pygame.image.load(graphics_dir + "body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load(graphics_dir + "body_tl.png").convert_alpha()
        self.body_br = pygame.image.load(graphics_dir + "body_br.png").convert_alpha()
        self.body_bl = pygame.image.load(graphics_dir + "body_bl.png").convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(
            self.body
        ):  # for block in self.body: # for every block in the body list
            # 1. create a rectangle for the positioning
            x_pos = int(block.x * cell_size)  # x position of the block
            y_pos = int(block.y * cell_size)  # y position of the block
            block_rect = pygame.Rect(
                x_pos, y_pos, cell_size, cell_size
            )  # create a rectangle

            # 2. what direction is the face and the tail heading
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = (
                    self.body[index + 1] - block
                )  # take the current element and add 1 to it to get the previous block
                next_block = (
                    self.body[index - 1] - block
                )  # take the current element and subtract 1 to it to get the next block
                if (
                    previous_block.x == next_block.x
                ):  # if the snake is moving vertically
                    screen.blit(self.body_vertical, block_rect)
                elif (
                    previous_block.y == next_block.y
                ):  # if the snake is moving horizontally
                    screen.blit(self.body_horizontal, block_rect)
                else:  # if the snake is turning
                    if (
                        previous_block.x == -1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == -1
                    ):  # if the snake is turning top left
                        screen.blit(self.body_tl, block_rect)
                    elif (
                        previous_block.x == -1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == -1
                    ):  # if the snake is turning down left
                        screen.blit(self.body_bl, block_rect)
                    elif (
                        previous_block.x == 1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == 1
                    ):  # if the snake is turning top right
                        screen.blit(self.body_tr, block_rect)
                    elif (
                        previous_block.x == 1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == 1
                    ):  # if the snake is turning bottom right
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):  # updates the head to face in the right direction
        head_relation = (
            self.body[1] - self.body[0]
        )  # get the relation between the head and the second block
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):  # updates the tail to face in the right direction
        tail_relation = (
            self.body[-2] - self.body[-1]
        )  # get the relation between the second to last block and the last (tail) block
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
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
apple = pygame.image.load(graphics_dir + "apple.png").convert_alpha()

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
