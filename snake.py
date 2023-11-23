import pygame, sys, random, os
from pygame.math import Vector2

snake_dir = os.path.dirname(__file__)  # main directory snake.py is in
graphics_dir = os.path.join(snake_dir, "graphics/")  # graphics directory is in main directory
font_dir = os.path.join(snake_dir, "font/") # font directory is in main directory
sound_dir = os.path.join(snake_dir, "sound/") # sound directory is in main directory


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size,)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size,)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]  # snake body
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load(graphics_dir + "head_up.png").convert_alpha()
        self.head_down = pygame.image.load(graphics_dir + "head_down.png").convert_alpha()
        self.head_right = pygame.image.load(graphics_dir + "head_right.png").convert_alpha()
        self.head_left = pygame.image.load(graphics_dir + "head_left.png").convert_alpha()

        self.tail_up = pygame.image.load(graphics_dir + "tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load(graphics_dir + "tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load(graphics_dir + "tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load(graphics_dir + "tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load(graphics_dir + "body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load(graphics_dir + "body_horizontal.png").convert_alpha()

        self.body_tr = pygame.image.load(graphics_dir + "body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load(graphics_dir + "body_tl.png").convert_alpha()
        self.body_br = pygame.image.load(graphics_dir + "body_br.png").convert_alpha()
        self.body_bl = pygame.image.load(graphics_dir + "body_bl.png").convert_alpha()
        self.crunch_sound = pygame.mixer.Sound(sound_dir + "crunch.wav") #this is the crunch sound

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):  # for block in self.body: # for every block in the body list
            # 1. create a rectangle for the positioning
            x_pos = int(block.x * cell_size)  # x position of the block
            y_pos = int(block.y * cell_size)  # y position of the block
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)  # create a rectangle

            # 2. what direction is the face and the tail heading
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = (self.body[index + 1] - block)  # take the current element and add 1 to it to get the previous block
                next_block = (self.body[index - 1] - block)  # take the current element and subtract 1 to it to get the next block
                if (
                    previous_block.x == next_block.x):  # if the snake is moving vertically
                    screen.blit(self.body_vertical, block_rect)
                elif (
                    previous_block.y == next_block.y):  # if the snake is moving horizontally
                    screen.blit(self.body_horizontal, block_rect)
                else:  # if the snake is turning
                    if (previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1):  # if the snake is turning top left
                        screen.blit(self.body_tl, block_rect)
                    elif (previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1):  # if the snake is turning down left
                        screen.blit(self.body_bl, block_rect)
                    elif (previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1):  # if the snake is turning top right
                        screen.blit(self.body_tr, block_rect)
                    elif (previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1):  # if the snake is turning bottom right
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):  # updates the head to face in the right direction
        head_relation = (self.body[1] - self.body[0])  # get the relation between the head and the second block
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):  # updates the tail to face in the right direction
        tail_relation = (self.body[-2] - self.body[-1])  # get the relation between the second to last block and the last (tail) block
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
            body_copy.insert(0, body_copy[0] + self.direction)  # insert a new element at the beginning of the list
            self.body = body_copy[:]  # copy the body_copy list to the body list

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self): #plays the crunch sound
        self.crunch_sound.play()
    
    def reset(self): #when you fail the game the snake gets the same length as at the start and is placed in the same position
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()  # call the move_snake method so every 150 milliseconds the snake moves
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass() #draws the grass from the draw_grass method
        self.draw_score() #draws the score from the draw_score method
        self.fruit.draw_fruit()  # from class FRUIT draw_fruit method in while loop
        self.snake.draw_snake()  # from class SNAKE draw_snake method in while

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # als fruit positie gelijk is aan positie 0 van snake, dus hoofd
            # print("jummie")
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound() #plays the crunch sound when the snake has a collision (eats a apple)

        for block in self.snake.body[1:]: #checks every block in the snakes body if the fruit is placed inside the body it gets a new position
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        elif not 0 <= self.snake.body[0].y < cell_number:
            # voorwaarde kan ook in de eerste "if", maar vind dit beter te lezen
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (137,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left ,apple_rect.top ,apple_rect.width + score_rect.width + 6 ,apple_rect.height)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)

pygame.mixer.pre_init(44100,-16,2,512) #preloads the sound so there is no delay
pygame.init()
pygame.mixer.init()

background_music = pygame.mixer.Sound(sound_dir + "music.wav") #this is the background music
background_music.play(loops = -1) # play the sound infinite times
background_music.set_volume(0.5) # set the volume of the sound to 0.5

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load(graphics_dir + "apple.png").convert_alpha()
game_font = pygame.font.Font(font_dir + "PoetsenOne-Regular.ttf", 25)

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
                if main_game.snake.direction.y != 1:
                    # zorgt ervoor dat je niet in tegengestelde richting kan gaan, zelfde bij andere toetsen
                    main_game.snake.direction = Vector2(0, -1)  # move up -1 in y axis
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)  # move down 1 in y axis
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)  # move left -1 in x axis
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)  # move right 1 in x axis

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
