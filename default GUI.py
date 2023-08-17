# pygame for GUI
import pygame

# initialize pygame
pygame.init()

# declare the screen width and height
screenWidth = 640
screenHeight = 480

# declare the screen
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

# declare the rectangles/boxes/squares
box1 = pygame.Rect((screenWidth / 2) - 150, screenHeight / 2 - 80, 100, 40)
box2 = pygame.Rect((screenWidth / 2) + 50, screenHeight / 2 - 80, 100, 40)
box3 = pygame.Rect((screenWidth / 2) - 150, screenHeight / 2 + 80, 100, 40)
box4 = pygame.Rect((screenWidth / 2) + 50, screenHeight / 2 + 80, 100, 40)

# declare the fonts
baseFont = pygame.font.Font(None, 32)
titleFont = pygame.font.Font(None,50)

# declare the text to put inside the boxes
box1Text = baseFont.render("box1", True, (0, 0, 0))
box2Text = baseFont.render("box2", True, (0, 0, 0))
box3Text = baseFont.render("box3", True, (0, 0, 0))
box4Text = baseFont.render("box4", True, (0, 0, 0))

# declare the title text
nameText = titleFont.render("Program name here!", True, (0, 0, 0))
 
# set the window caption
pygame.display.set_caption("default caption")

# declare crashed
crashed = False

# display the gui while pygame is open
while not crashed:
    # run through every event and make sure that nothing has happened
    for event in pygame.event.get():
        # if you close pygame it will stop running
        if event.type == pygame.QUIT:
            crashed = True
        
        # if you click a mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if it's inside box 1
            if box1.collidepoint(event.pos):
                print("mouse click in box 1")

            #if it's inside box 2
            if box2.collidepoint(event.pos):
                print("mouse click in box 2")
            
            # if it's inside box 3
            if box3.collidepoint(event.pos):
                print("mouse click in box 3")
            
            # if it's inside box 4
            if box4.collidepoint(event.pos):
                print("mouse click in box 4")
    
    # fill the screen with this nice blue color
    screen.fill((18, 48, 81))

    # draw the rectangles
    pygame.draw.rect(screen, (255, 255, 255), box1)
    pygame.draw.rect(screen, (255, 255, 255), box2)
    pygame.draw.rect(screen, (255, 255, 255), box3)
    pygame.draw.rect(screen, (255, 255, 255), box4)

    # draw the text
    screen.blit(box1Text, (box1.x + box1Text.get_width() / 2, box1.y + box1Text.get_height() / 2))
    screen.blit(box2Text, (box2.x + box2Text.get_width() / 2, box2.y + box2Text.get_height() / 2))
    screen.blit(box3Text, (box3.x + box3Text.get_width() / 2, box3.y + box3Text.get_height() / 2))
    screen.blit(box4Text, (box4.x + box4Text.get_width() / 2, box4.y + box4Text.get_height() / 2))
    screen.blit(nameText, (screenWidth / 2 - nameText.get_width() / 2, 50))

    # and update the display
    pygame.display.update()