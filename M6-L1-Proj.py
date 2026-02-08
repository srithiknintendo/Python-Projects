import pygame
import sys

# Initialize pygame
pygame.init()

# 1. Set window size (500, 500)
screen = pygame.display.set_mode((500, 500))

# 2. Set caption
pygame.display.set_caption("My first game screen")

# 4. Set background color - Grey (58, 58, 58)
background_color = (58, 58, 58)

# 3. Load and resize image to (300, 300)
# Replace 'image.png' with your image file name
image = pygame.image.load("image.png")
image = pygame.transform.scale(image, (300, 300))

# Get rectangle of image and set it to center
image_rect = image.get_rect(center=(250, 250))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(background_color)

    # Draw image at center
    screen.blit(image, image_rect)

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()