import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Square test")


player = pygame.Rect((300, 250, 50, 50))

# Game loop
running = True
while running:


    pygame.draw.rect(screen, (255, 230, 80), player)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    #update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()