import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen : pygame.Surface):
        self.screen = screen
        self.radius = random.randint(1, 20)
        self.x = random.uniform(self.radius, screen.get_width() - self.radius)
        self.y = random.uniform(self.radius, screen.get_height() - self.radius)
        self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speedX = random.randint(1, 10)
        self.speedY = random.randint(1, 10)

    def draw(self):
        pygame.draw.circle(self.screen,
                           self.color,
                           (self.x, self.y),
                           self.radius)

    def move(self):
        if(self.x <= self.radius or self.x >= self.screen.get_width() - self.radius):
            self.speedX = -self.speedX
            self.speedX += random.uniform(-0.5, 0.5)

        if (self.y <= self.radius or self.y >= self.screen.get_height() - self.radius):
            self.speedY = -self.speedY
            self.speedY += random.uniform(-0.5, 0.5)

        self.x += self.speedX
        self.y += self.speedY


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1
    balls = []

    for i in range(10000):
        balls.append(Ball(screen))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        # TODO: Draw the ball
        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
