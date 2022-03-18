import pygame
from random import randint
class Bird(object):  
    def __init__(self):
        self.okoshechko = pygame.Rect(65,50,50,50)
        self.birdsStatus = [pygame.image.load("assets/1.png"),pygame.image.load("assets/2.png"),pygame.image.load("assets/dead.png")]
        self.status = 0
        self.birdX = 120
        self.birdY = 350
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False
    def birdsUpdate(self):
        if self.jump:

            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
        else:
            self.gravity += 0.2
            self.birdY += self.gravity
        self.okoshechko[1] = self.birdY
        pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial",50)
w = 401
h = 706
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
bird = Bird()
score = 0
background = pygame.image.load("assets/background.png")
class  Truba(object):
    def __init__(self):
        self.trubaX = w
        self.trubaUp = pygame.image.load("assets/top.png")
        self.trubaDown = pygame.image.load("assets/bottom.png")
    def trubaUpdate(self):
        self.trubaX -= 5
        if self.trubaX < -80:
            global score
            global w
            score += 1
            self.trubaX = w
truba = Truba()
def checkDead():
    upRect = pygame.Rect(truba.trubaX,-300,truba.trubaUp.get_width()-10,truba.trubaUp.get_height())
    downRect = pygame.Rect(truba.trubaX,500,truba.trubaDown.get_width()-10,truba.trubaDown.get_height())
    if upRect.colliderect(bird.okoshechko) or downRect.colliderect(bird.okoshechko):
        bird.dead = True
    if not  0 < bird.okoshechko[1] < h:
        bird.dead = True
        return True
    else:
        return False
def createMap():
    screen.blit(background,(0,0))
    screen.blit(truba.trubaUp,(truba.trubaX,(-300)))
    screen.blit(truba.trubaDown,(truba.trubaX,(500)))
    truba.trubaUpdate()
    if bird.dead:
        bird.status = 2
    elif bird.jump:
        bird.status = 1
    screen.blit(bird.birdsStatus[bird.status],(bird.birdX,bird.birdY))
    bird.birdsUpdate()
    screen.blit(font.render('Score: '+str(score),True,(randint(0,255),randint(0,255),randint(0,255))),(100,50))
    pygame.display.update()
def getResult():
    text1 = "Game Over"
    text2 = "Your final score is " + str(score)
    font1 = pygame.font.SysFont("Arial",70)
    font2 = pygame.font.SysFont("Arial",30)
    surf1 = font1.render(text1,True,(randint(0,255),randint(0,255),randint(0,255)))
    surf2 = font2.render(text2,True,(randint(0,255),randint(0,255),randint(0,255)))
    screen.blit(surf1,[screen.get_width()/2 - surf1.get_width()/2,100])
    screen.blit(surf2,[screen.get_width()/2 - surf2.get_width()/2,200])
    pygame.display.flip()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not bird.dead:
            bird.jump = True
            bird.jumpSpeed = 10
            bird.gravity = 5
    if checkDead():
        getResult()
    else:
        createMap()

