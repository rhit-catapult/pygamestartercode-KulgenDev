import pygame
import time
class Hero:
    def __init__(self, screen : pygame.Surface, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
        self.x = x
        self.y = y
        self.imgUmb = pygame.image.load(with_umbrella_filename)
        self.imgNUmb = pygame.image.load(without_umbrella_filename)
        self.lastHitTime = 0

    def draw(self):
        """ Draws this sprite onto the screen. """
        currentTime = time.time()
        if currentTime > self.lastHitTime + 1:
            self.screen.blit(self.imgNUmb, (self.x, self.y))
        else:
            self.screen.blit(self.imgUmb, (self.x, self.y))

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        heroHitBox = pygame.Rect(self.x,
                                 self.y,
                                 self.imgNUmb.get_width(),
                                 self.imgNUmb.get_height())

        return heroHitBox.collidepoint(raindrop.x, raindrop.y)
