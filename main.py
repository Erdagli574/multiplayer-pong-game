import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 100, 0)
BLUE = (0, 128, 255)
GRAY = (224, 224, 224)

scoreLeft = 0
scoreRight = 0

velocity = 15

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BALL_SIZE = 10


class Ball:

    def __init__(self):
        self.x = 500
        self.y = 300
        self.change_x = 10
        self.change_y = 10
        self.accelerate = 60
        self.projectile = False


def change():
    ball.x = 500
    ball.y = 300
    ball.change_y = 10

    ball.projectile = False
    ball.accelerate = 60


def rotate():
    ball.projectile = True

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

ball = Ball()

pygame.init()

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
gameDisplay = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

PaddleL_x = 40
PaddleL_y = 250
PaddleR_x = 950
PaddleR_y = 250

run = True
final = False

clock = pygame.time.Clock()

while True:

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        Ly = [PaddleL_y, PaddleL_y + 120]
        Ry = [PaddleR_y, PaddleR_y + 120]

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_w]) and (PaddleL_y >= 0):
            PaddleL_y -= velocity
        if (keys[pygame.K_s]) and (PaddleL_y <= 475):
            PaddleL_y += velocity

        if (keys[pygame.K_UP]) and (PaddleR_y >= 0):
            PaddleR_y -= velocity
        if (keys[pygame.K_DOWN]) and (PaddleR_y <= 475):
            PaddleR_y += velocity

        ball.x += ball.change_x
        if ball.projectile:
            ball.y -= ball.change_y

        if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
            ball.change_y *= -1
        if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
            if ball.x == 0:
                scoreRight += 1
            if ball.x == 1000:
                scoreLeft += 1
            change()
        if ((Ry[0] - 5 < ball.y) and (ball.y < Ry[1])) and (ball.x + 10 == PaddleR_x):
            rotate()
            ball.change_x *= -1
            if ((Ry[0] + 32 < ball.y) and (ball.y < Ry[1] - 25)) and (ball.x + 10 == PaddleR_x):
                ball.change_y -= 7
        if ((Ly[0] - 5 < ball.y) and (ball.y < Ly[1])) and (ball.x - 10 == PaddleL_x + 10):
            rotate()
            ball.accelerate += 5
            ball.change_x *= -1
            if ((Ly[0] + 32 < ball.y) and (ball.y < Ly[1] - 25)) and (ball.x + 10 == PaddleL_x):
                ball.change_y -= 7

        gameDisplay.fill(GREEN)

        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreLeft), 1, GRAY)
        gameDisplay.blit(text, (187, 10))
        text = font.render(str(scoreRight), 1, GRAY)
        gameDisplay.blit(text, (734, 10))

        pygame.draw.line(gameDisplay, BLACK, (500, 0), (500, 600), 3)  # Center line
        pygame.draw.line(gameDisplay, GRAY, (0, 0), (0, 600), 8)  # Border left
        pygame.draw.line(gameDisplay, GRAY, (1000, 0), (1000, 600), 12)  # Border right
        pygame.draw.circle(gameDisplay, BLACK, (500, 300), 150, 3)  # Middle circle

        pygame.draw.rect(gameDisplay, BLUE, (PaddleL_x, PaddleL_y, 10, 126))  # Paddle left
        pygame.draw.circle(gameDisplay, WHITE, [ball.x, ball.y], BALL_SIZE)
        pygame.draw.rect(gameDisplay, RED, (PaddleR_x, PaddleR_y, 10, 126))  # Paddle right

        clock.tick(ball.accelerate)

        pygame.display.flip()

        if scoreRight == 10 or scoreLeft == 10:
            final = True
            run = False

    while final:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                final = False

        gameDisplay.fill(GREEN)

        font = pygame.font.Font(None, 170)
        text = font.render(str(scoreLeft), 1, BLUE)
        gameDisplay.blit(text, (187, 270))
        text = font.render(str(scoreRight), 1, RED)
        gameDisplay.blit(text, (734, 270))

        pygame.draw.line(gameDisplay, BLACK, (500, 0), (500, 600), 3)  # Center line
        pygame.draw.line(gameDisplay, GRAY, (0, 0), (0, 600), 8)  # Border left
        pygame.draw.line(gameDisplay, GRAY, (1000, 0), (1000, 600), 12)  # Border right
        pygame.draw.circle(gameDisplay, BLACK, (500, 300), 150, 3)  # Middle circle

        pygame.display.flip()

    pygame.quit()


