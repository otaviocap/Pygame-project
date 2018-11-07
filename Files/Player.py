import pygame

class Player():
    def __init__(self, x=0, y=0, sizeX=10, sizeY=10):
        self.direction = 'right'
        self.size = (sizeX, sizeY)
        self.rect = pygame.Rect(x, y, sizeX, sizeY)
        self.cooldown = 0
        self.image = pygame.image.load('../assets/character.png')
        self.image = pygame.transform.scale(self.image, (self.getSize()[0]**2, self.getSize()[1]**2))
        self.original = pygame.image.load('../assets/character.gif')
        self.original = pygame.transform.scale(self.original, (self.getSize()[0] ** 2, self.getSize()[1] ** 2))
        self.transformImgSide()
        self.gunBarrel = [100, 100]
        # self.gunBarrel = [X , Y]

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def getPos(self):
        return (self.rect.x, self.rect.y)

    def checkCooldown(self):
        if self.cooldown == 0:
            return True

    def setCooldown(self, n):
        self.cooldown = n

    def getCooldown(self):
        return self.cooldown

    def goCooldown(self):
        if self.cooldown == 0:
            pass
        else:
            self.cooldown -= 1

    def getSize(self):
        return self.size

    def setSize(self, size, screen):
        self.size += size
        pygame.transform.scale(screen, self.size)

    def getImg(self):
        return self.image

    def transformImgSide(self):
        self.image = self.original
        if self.direction == "down":
            self.image = pygame.transform.rotate(self.image, -90)
        elif self.direction == "up":
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.direction == "right":
            self.image = pygame.transform.flip(self.image, False, False)

    def setDirection(self, direction):
        if not self.direction == direction:
            self.direction = direction
            self.transformImgSide()
        else:
            pass

    def getGunBarrel(self):
        return self.gunBarrel