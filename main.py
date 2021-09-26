import pygame
import math
import random

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Loading the images
background = pygame.image.load('wepik-2021811-203039.png')
nest = pygame.image.load('nest.png')
icon = pygame.image.load('nest (1).png')

# Setting th caption and icon
pygame.display.set_caption('Save the Bird')
pygame.display.set_icon(icon)

running = True

nestX_change = 0
nestX = 370


# displaying the player
def playerNest(x):
    screen.blit(nest, (x, 480))


# Setting up falling birds
number_of_birds = 2
birdImg = pygame.image.load('bird.png')
birdX = random.randint(0, 736)
birdY = random.randint(30, 400)
birdY_change = 2.5


# display of falling bird
def bird(x, y):
    screen.blit(birdImg, (x, y))


# Variable to increase difficulty with score
level_up = 0

# Setting up score panel
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)


# Displaying the score
def display_score():
    score = font.render("Score : " + str(score_value), True, (255, 0, 0))
    screen.blit(score, (10, 10))


over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))


restart_font = pygame.font.Font('freesansbold.ttf', 24)


def restart():
    restart_text = restart_font.render("Press SPACE to restart ", True, (0, 0, 0))
    screen.blit(restart_text, (300, 10))

# function to see if player catches the bird
def catch(X, Y, prX):
    distance = math.sqrt(math.pow(X - (prX+5), 2) + math.pow(Y - 490, 2))
    if distance < 40:
        return True
    else:
        return False


while running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # moving the player if key is pressed and checking direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                nestX_change = -5
            if event.key == pygame.K_RIGHT:
                nestX_change = 5
            if event.key == pygame.K_SPACE:
                score_value = 0
                for i in range(number_of_birds):
                    birdX = random.randint(0, 736)
                    birdY = random.randint(50, 200)

        # stopping the player when key is not pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                nestX_change = 0

    # Game Over
    if birdY > 550:
        birdY = 2000
        game_over_text()
        restart()

    birdY += birdY_change

    # Catching bird
    Catch = catch(birdX, birdY, nestX)
    if Catch:
        score_value += 1
        level_up += 1
        # increasing difficulty with score
        if level_up == 10:
            level_up = 0
            birdY_change += 0.5
        birdX = random.randint(0, 736)
        birdY = random.randint(50, 150)

    bird(birdX, birdY)

    nestX += nestX_change
    if nestX <= 0:
        nestX = 0
    elif nestX >= 736:
        nestX = 736

    nestX += nestX_change

    playerNest(nestX)
    display_score()

    pygame.display.update()
