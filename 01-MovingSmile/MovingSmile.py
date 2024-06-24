import pygame
import sys


def main():
    pygame.init()
    test = {"car" : 3}
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    deltaX = 0
    deltaY = 0
    speed = 2

    while True:
        # TODO 4: Set the clock speed to 60 fps
        dt = clock.tick(60)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            deltaY -= speed
        if pressed_keys[pygame.K_DOWN]:
            deltaY += speed
        if pressed_keys[pygame.K_LEFT]:
            deltaX -= speed
        if pressed_keys[pygame.K_RIGHT]:
            deltaX += speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 3: Make the eye pupils move with Up, Down, Left, and Right keys

        screen.fill((255, 255, 255))  # white

        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242 + deltaX, 162 + deltaY), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398 + deltaX, 162 + deltaY), 7)  # black pupil

        # TODO 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        pygame.draw.circle(screen, (0,0,0), (320, 245), 10)

        # TODO 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        pygame.draw.rect(screen, (0,0,0), (230, 320, 180, 30))

        pygame.display.update()


main()
