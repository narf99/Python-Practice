import pygame
import random

class Card:
    def __init__(self, frontImage:pygame.image, backImage:pygame.image, displayRect:pygame.rect, imageNumber:int):
        self.frontImage = frontImage
        self.backImage = backImage
        self.displayImage = backImage
        self.rect = displayRect
        self.fliped = False
        self.imageNumber = imageNumber
    
    def flip(self, user = True):
        if self.displayImage == self.backImage:
            self.displayImage = self.frontImage
            self.fliped = True
        
        elif self.displayImage == self.frontImage and user == False:
            self.displayImage = self.backImage
            self.fliped = False
    
    def __str__(self):
        return str(self.imageNumber)

def randomizeImages():
    images = [
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\cat1.jpg"), (160, 160)), 1), 
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\cat1.jpg"), (160, 160)), 1), 
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\cat2.jpg"), (160, 160)), 2),
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\cat2.jpg"), (160, 160)), 2),
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\cat3.jpg"), (160, 160)), 3),
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\cat3.jpg"), (160, 160)), 3),
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\cat4.jpg"), (160, 160)), 4),
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\cat4.jpg"), (160, 160)), 4),
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\cat5.jpg"), (160, 160)), 5),
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\cat5.jpg"), (160, 160)), 5),
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\city1.jpg"), (160, 160)), 6),
        (pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\city1.jpg"), (160, 160)), 6)
    ]

    imageLocations = [ # we use this to detect which image is clicked and as a place to place the images
        pygame.Rect(5, 25, 160, 160), pygame.Rect(170, 25, 160, 160), pygame.Rect(340, 25, 160, 160), pygame.Rect(510, 25, 160, 160),
        pygame.Rect(5, 195, 160, 160), pygame.Rect(170, 195, 160, 160), pygame.Rect(340, 195, 160, 160), pygame.Rect(510, 195, 160, 160),
        pygame.Rect(5, 365, 160, 160), pygame.Rect(170, 365, 160, 160), pygame.Rect(340, 365, 160, 160), pygame.Rect(510, 365, 160, 160)
    ]

    backImage = pygame.transform.scale(pygame.image.load("BPA C# State 2019\Images\BPAlogo.jpg"), (160, 160))

    fullImages = []
    
    random.shuffle(images)

    for i in range(len(images)):

        fullImages.append(Card(images[i][0], backImage, imageLocations[i], images[i][1]))
        
    return fullImages

def drawRectWBorder(display, color, rect, borderWidth, borderColor):
    pygame.draw.rect(display, color, rect)
    pygame.draw.rect(display, borderColor, rect, borderWidth)

def popUpWindow(baseText, baseTextPos:tuple, option1Text, option1Pos:tuple, option2Text, option2Pos:tuple):
    global screen
    global mediumFont
    global baseFont
    global popUpWindowRects

    drawRectWBorder(screen, (196, 196, 196), popUpWindowRects[0], 2, (0, 0, 0))
    screen.blit(mediumFont.render(baseText, True, (0, 0, 0)), (popUpWindowRects[0].x+baseTextPos[0], popUpWindowRects[0].y+baseTextPos[1]))
        
    drawRectWBorder(screen, (255, 255, 255), popUpWindowRects[1], 2, (0, 0, 0))
    screen.blit(baseFont.render(option1Text, True, (0, 0, 0)), (popUpWindowRects[1].x+option1Pos[0], popUpWindowRects[1].y+option1Pos[1]))
        
    drawRectWBorder(screen, (255, 255, 255), popUpWindowRects[2], 2, (0, 0, 0))
    screen.blit(baseFont.render(option2Text, True, (0, 0, 0)), (popUpWindowRects[2].x+option2Pos[0], popUpWindowRects[2].y+option2Pos[1]))

pygame.init()

screenWidth = 675
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

score = 0

baseFont = pygame.font.Font(None, 22)

bigFont = pygame.font.Font(None, 44)

mediumFont = pygame.font.Font(None, 33)

scoreText = baseFont.render("Score: " + str(score), True, (0, 0, 0))

popUpWindowRects = [    
    pygame.Rect(screenWidth/2-150, screenHeight/2-100, 300, 200),
    pygame.Rect(screenWidth/2-105, screenHeight/2+40, 100, 50),
    pygame.Rect(screenWidth/2+5, screenHeight/2+40, 100, 50)
]

restartRect = pygame.Rect(screenWidth/2-105, screenHeight-60, 100, 50)

exitRect = pygame.Rect(screenWidth/2+5, screenHeight-60, 100, 50)

fullImages = randomizeImages()

pygame.display.set_caption("Matching Game")

flipedCards = []
totalFlipedCards = 0
restartConfirm = False
exitConfirm = False
crashed = False
wait = False

while not crashed:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if totalFlipedCards < 12:
                if restartRect.collidepoint(event.pos):
                    restartConfirm = True
                
                elif exitRect.collidepoint(event.pos):
                    exitConfirm = True
                
                elif restartConfirm == True:
                    if popUpWindowRects[1].collidepoint(event.pos):
                        totalFlipedCards = 0
                        fullImages = randomizeImages()
                        score = 0
                        restartConfirm = False
                        wait = True
                    
                    elif popUpWindowRects[2].collidepoint(event.pos):
                        restartConfirm = False
                
                elif exitConfirm == True:
                    if popUpWindowRects[1].collidepoint(event.pos):
                        crashed = True
                    
                    elif popUpWindowRects[2].collidepoint(event.pos):
                        exitConfirm = False
                
                elif restartConfirm == False and exitConfirm == False:
                    for i in fullImages:
                        if i.rect.collidepoint(event.pos) and len(flipedCards)<2 and i.fliped == False:
                            i.flip()
                            flipedCards.append(i)
                            totalFlipedCards += 1
            
            elif totalFlipedCards >= 12:
                if popUpWindowRects[1].collidepoint(event.pos):
                    totalFlipedCards = 0
                    fullImages = randomizeImages()
                    score = 0
                    
                
                elif popUpWindowRects[2].collidepoint(event.pos):
                    crashed = True
            
    scoreText = baseFont.render("Score: " + str(score), True, (0, 0, 0))
    
    screen.fill((255, 255, 255))

    screen.blit(scoreText, (5, 5))

    for i in fullImages:
        screen.blit(i.displayImage, i.rect)
    
    drawRectWBorder(screen, (196, 196, 196), restartRect, 2, (0, 0, 0))
    screen.blit(mediumFont.render("Restart", True, (0, 0, 0)), (restartRect.x+10, restartRect.y+13))

    drawRectWBorder(screen, (196, 196, 196), exitRect, 2, (0, 0, 0))
    screen.blit(mediumFont.render("Exit", True, (0, 0, 0)), (exitRect.x+27, exitRect.y+13))

    if restartConfirm == True:
        popUpWindow("Restart?", (105, 20), "Yes", (37, 18), "No", (37, 18))

    if exitConfirm == True:
        popUpWindow("Exit?", (125, 20), "Yes", (37, 18), "No", (37, 18))
    
    if totalFlipedCards >= 12:
        popUpWindow("Final Score: "+str(score), (35, 10), "Play Again?", (7, 18), "Exit", (33, 18))

    pygame.display.update()

    if wait == True:
        pygame.time.wait(480)
        wait = False
    
    if len(flipedCards) == 2:
        if flipedCards[0].imageNumber == flipedCards[1].imageNumber:
            flipedCards = []
            score += 100
            scoreText = baseFont.render("Score: " + str(score), True, (0, 0, 0))
        
        elif flipedCards[0].imageNumber != flipedCards[1].imageNumber:
            pygame.time.wait(480)
            flipedCards[0].flip(False)
            flipedCards[1].flip(False)
            flipedCards = []
            totalFlipedCards -= 2
            score -= 50
            scoreText = baseFont.render("Score: " + str(score), True, (0, 0, 0))
    