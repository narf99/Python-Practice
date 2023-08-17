# import modules
import glob # glob is to collect all the .wavs in the folder that we store the sounds in
import pygame # this plays the sounds and also creates the gui
import random # this selects a random song to play
import time # this makes sure that we can wait for the sound to end

# declare the variable to store the song options in
soundOptions = []

# add the wav files to the array
wavs = glob.glob("english final\marvinLines\*.wav")
for i in range(len(wavs)):
    soundOptions.append(wavs[i])

# initialize pygame
pygame.init()

# declare the screen width and height
screenWidth = 200
screenHeight = 100

# declare the screen
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

# declare the rectangles/boxes/squares
box1 = pygame.Rect(screenWidth / 2 - 50, screenHeight / 2 - 20, 100, 40)

# declare the fonts
baseFont = pygame.font.Font(None, 32)
titleFont = pygame.font.Font(None, 50)

# declare the text to put inside the boxes
box1Text = baseFont.render("Speak", True, (0, 0, 0))

# set the window caption
pygame.display.set_caption("Marvin Voice Handler")

# declare crashed
crashed = False

# declare the variable to store the song in
sound = " "

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
                # pick the line to play
                sound = random.choice(soundOptions)
                
                # load the line to memory
                pygame.mixer.music.load(sound)

                # play the line
                pygame.mixer.music.play()

                # get the length of the line
                lengthOfSound = pygame.mixer.Sound(sound)
                lengthOfSound = int(lengthOfSound.get_length()) + 1

                # handle events while waiting for the line to play
                for i in range(lengthOfSound):
                    for event in pygame.event.get():
                        # if you close pygame it will stop running
                        if event.type == pygame.QUIT:
                            crashed = True
                    # stop wait a second
                    time.sleep(1)
                # unload the line from memory
                pygame.mixer.music.unload()
    
    # fill the screen with this nice blue color
    screen.fill((18, 48, 81))

    # draw the rectangles
    pygame.draw.rect(screen, (255, 255, 255), box1)

    # draw the text
    screen.blit(box1Text, (box1.x + box1Text.get_width() / 2 - 20, box1.y + box1Text.get_height() / 2))

    # and update the display
    pygame.display.update()