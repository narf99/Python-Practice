import pygame

pygame.init()

screenHeight = 400
screenWidth = 200

screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

trafficLightBase = pygame.Rect(screenWidth/2-50, screenHeight/2-100, 100, 200)

cycleLightButton= pygame.Rect(screenWidth/2-75, screenHeight/2+125, 150, 50)

baseFont = pygame.font.Font(None, 32)

cycleText = baseFont.render("Cycle Lights", True, (0, 0, 0))

# Lights
redLightBase = pygame.Rect(screenWidth/2-28, screenHeight/2-90, 55, 55)

yellowLightBase = pygame.Rect(screenWidth/2-28, screenHeight/2-30, 55, 55)

greenLightBase = pygame.Rect(screenWidth/2-28, screenHeight/2+30, 55, 55)

cycle = 0

redColor = (128, 128, 128)

yellowColor = (128, 128, 128)

greenColor = (128, 128, 128)

crashed = False

while not crashed:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if cycleLightButton.collidepoint(event.pos):
                cycle += 1

                if cycle == 3:
                    cycle = 0
    
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), trafficLightBase)

    pygame.draw.rect(screen, (128, 128, 128), cycleLightButton)

    screen.blit(cycleText, (cycleLightButton.x + 8, cycleLightButton.y + 15))

    if cycle == 0:
        greenColor = (128, 128, 128)
        redColor = (255, 0, 0)
    
    elif cycle == 1:
        redColor = (128, 128, 128)
        yellowColor = (255, 238, 0) 


    elif cycle == 2:
        yellowColor = (128, 128, 128)
        greenColor = (0, 255, 0)

    pygame.draw.ellipse(screen, redColor, redLightBase)

    pygame.draw.ellipse(screen, yellowColor, yellowLightBase)

    pygame.draw.ellipse(screen, greenColor, greenLightBase)

    pygame.display.update()