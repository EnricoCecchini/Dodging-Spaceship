# Import libraries
import pygame
import random
import math

# Initialize pygame
pygame.init()

# Creates screen and background image
screen = pygame.display.set_mode((600, 800))
background = pygame.image.load("background.png")

# Creates game name and icon on window
pygame.display.set_caption("Falling Sky")
icon = pygame.image.load("asteroid.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 300
playerY = 700
playerX_change = 0

# Meteorites
meteorImg = []
meteorX = []
meteorY = []
meteorX_change = []
meteorY_change = []
num_of_enemies = 8
# Creates 8 meteorites in random locations
for i in range(num_of_enemies):
    meteorImg.append(pygame.image.load("asteroid.png"))
    meteorX.append(random.randint(0, 600))
    meteorY.append(random.randint(0, 150))
    meteorY.append(0)
    meteorX_change.append(0)
    meteorY_change.append(7)

# Score counter
score_value = 0
# Creates a text with font and size
font = pygame.font.Font('freesansbold.ttf', 32)
# Text location coordinates
scoreX = 10
scoreY = 10

# Lives counter
lives = 3
# Creates a text with font and size
lives_font = pygame.font.Font('freesansbold.ttf', 32)
# Text location coordinates
livesX = 10
livesY = 40

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)


# Show score on screen
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Show lives counter on screen
def show_lives(x, y):
    lives_left = font.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(lives_left, (x, y))


# Show game over text and final score
def game_over_text():
    over_text = over_font.render("Game Over", True, (255, 255, 255))
    screen.blit(over_text, (100, 300))
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (200, 370))


# Show player on screen
def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


# Show meteors on screen
def meteor(x, y, i):
    screen.blit(meteorImg[i], (x, y))


# Checks the distance between meteor and player and determines if there is a collision
def isCollision(meteorX, meteorY, playerX, playerY):
    distance = math.sqrt((math.pow((meteorX - playerX), 2)) + (math.pow((meteorY - playerY), 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    # RGB background color
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for arrow location and move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -8
            if event.key == pygame.K_RIGHT:
                playerX_change = 8
        # Stops player movement when no key is pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 536:
        playerX = 536

    # meteor movement
    for i in range(num_of_enemies):
        if meteorY[i] > 800:
            meteorX[i] = random.randint(0, 535)
            meteorY[i] = random.randint(50, 150)
            score_value += 10
            # print(score_value)
            # print(lives)
        if lives <= 0:
            lives = 0
        # Ends game if player runs out of lives
        if lives == 0:
            game_over_text()
            break

        # Meteor movement
        meteorY[i] += meteorY_change[i]

        # Collision
        collision = isCollision(meteorX[i], meteorY[i], playerX, playerY)
        if collision:
            # explosion_sound = mixer.Sound("explosion.wav")
            # explosion_sound.play()
            playerY = 700
            # Increases score and prints it in terminal
            score_value -= 10
            if score_value < 0:
                score_value = 0
            lives -= 1
            # Respawns meteor in random location
            meteorX[i] = random.randint(0, 535)
            meteorY[i] = random.randint(50, 150)

        # Calls enemy function to display enemies on screen
        meteor(meteorX[i], meteorY[i], i)

    player(playerX, playerY)

    # Show score and lives
    show_score(scoreX, scoreY)
    show_lives(livesX, livesY)

    pygame.display.update()
