#Import pygame & other functions
from pickletools import string4
import pygame, sys
import buttonClass
import time
from level import Level
from main import Game
from player import Player
from time import sleep

#Setup pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Gilded Grizzlies Coding Adventure GUI")
WIN_WIDTH = 1280
WIN_HEIGHT = 720
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#Set up the basic text font
basicFont = pygame.font.SysFont(None,64)
smallFont = pygame.font.SysFont(None,32) #Fits about 150 characters per line at 32 font size

#Import Images
backgroundimg = pygame.image.load(r'graphics\hud_elements\blackvectorbackground.jpg')
buttonimg = pygame.image.load(r'graphics\hud_elements\blankbutton.png')
button2img = pygame.image.load(r'graphics\hud_elements\blankbutton2.png')
oulogoimg = pygame.image.load(r'graphics\hud_elements\OULogo.png')
runCodeBtn = pygame.image.load(r'graphics\hud_elements\RunCodeButton.png')
exitGameBtn = pygame.image.load(r'graphics\hud_elements\ExitGameButton.png')
saveGameBtn = pygame.image.load(r'graphics\hud_elements\SaveGameButton.png')
stopBtn = pygame.image.load(r'graphics\hud_elements\StopButton.png')
startBtn = pygame.image.load(r'graphics\hud_elements\StartButton.png')
answer1Btn = pygame.image.load(r'graphics\hud_elements\Answer_1.png')
answer2Btn = pygame.image.load(r'graphics\hud_elements\Answer_2.png')

runCodeBtnAlt = pygame.image.load(r'graphics\hud_elements\WRun.png')
exitGameBtnAlt = pygame.image.load(r'graphics\hud_elements\WExit.png')
saveGameBtnAlt = pygame.image.load(r'graphics\hud_elements\WSave.png')
stopBtnAlt = pygame.image.load(r'graphics\hud_elements\WStop.png')
startBtnAlt = pygame.image.load(r'graphics\hud_elements\WStart.png')
answer1BtnAlt = pygame.image.load(r'graphics\hud_elements\WAnswer_1.png')
answer2BtnAlt = pygame.image.load(r'graphics\hud_elements\WAnswer_2.png')


#resize images
oulogoimg = pygame.transform.scale(oulogoimg, (250, 194))

#Create gamestate global variable
gameState = ['save1', 'start', 'right', 1, 0]
#gameState = ['Save Name', 'Menu Selector', 'Split Screen Selector', level, answer 0 = false 1 = true]
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (50,50,50)
WHITE = (250,250,250)

#####################
# F U N C T I O N S #
#####################

#get mouse position
def mouse():
    mosX, mosY = pygame.mouse.get_pos()
    #print('mosX: ', mosX, ' - ', 'mosY: ', mosY)
    return(mosX, mosY)

#get image length and height
def imgDim(img):
    imgWid = img.get_width()
    imgHei = img.get_height()
    return imgWid, imgHei

#test if mouse is hovering over a button
def imgHover(btn):
    #get mouse position
    mosX, mosY = mouse()
    #check if mouse x is within image width
    if (mosX>btn.getX()) and (mosX<btn.getX() + btn.getW()):
        insideX = True
    else:
        insideX = False
    #check if mouse y is within image height
    if (mosY>btn.getY()) and (mosY<btn.getY() + btn.getH()):
        insideY = True
    else:
        insideY = False
    #check if both x and y are true
    if (insideX == True) and (insideY == True):
        hover = True
    else:
        hover = False
    #print (hover)
    return hover 

#show end of level result
def levelCheck(passed):
    #create text
    correctMsg = basicFont.render('You Passed, Good Job!', False, (255, 255, 255))
    incorrectMsg = basicFont.render('Incorrect, Try Again', False, (255, 255, 255))

    #passed 0 = false, 1 = true
    if passed == 1:
        #Game.screen.blit(correctMsg, (300,70))
        print("level passed")
        gameState[3] = gameState[3] + 1
    else:
        #Game.screen.blit(incorrectMsg, (300,70))
        print("level failed")



#display start menu
def startMenu(gameState):

    #Create Strings
    title = basicFont.render('Gilded Grizzlies Coding Adventure', False, (255, 255, 255))

    #create buttons (button image, image x, image y, font, string, text x offset, text y offset)
    btn1 = buttonClass.buttonClass(startBtn, (win.get_width() / 2) - 150, (win.get_height() / 2) - 75, basicFont, '', 25, 15) #'Start Game'
    btn1H = buttonClass.buttonClass(startBtnAlt, (win.get_width() / 2) - 150, (win.get_height() / 2) - 75, basicFont, '', 25, 15) #'Start Game'
    btn2 = buttonClass.buttonClass(exitGameBtn, (win.get_width() / 2) - 150, (win.get_height() / 2) + 150, basicFont, '', 25, 15) #'Exit Game'
    btn2H = buttonClass.buttonClass(exitGameBtnAlt, (win.get_width() / 2) - 150, (win.get_height() / 2) + 150, basicFont, '', 25, 15) #'Exit Game'

    #Menu Loop
    while gameState[1] == 'start':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Title
            win.blit(title, (300,70))
            #Draw Images
            win.blit(oulogoimg, (125, 225))
            win.blit(oulogoimg, (win.get_width() - 394, 225))

            #check for mouse hover
            btn1Hov = imgHover(btn1)
            btn2Hov = imgHover(btn2)

            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)
            if btn2Hov == True:
                btn2H.draw(win)
            else:
                btn2.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click save 1 btn")
                    gameState[0] = 'save1'
                    gameState[1] = 'gameLoop'
                if btn2Hov == True:
                    print("mouse click save 2 btn")
                    gameState[0] = 'save1'
                    gameState[1] = 'exit'

        pygame.display.update()
        mainClock.tick(60)

#update save file
def updateSave():
    #create variables
    save = 'needRename'

    #Rename Save File
    if save == 'needRename':
        pygame.display.update()
        renameSave()
        save = 'renamed'
            
            
#rename save file
def renameSave():
    if gameState[0] == "save1":
                #saveFile = open("saveFile.txt","r")
                #print(saveFile.readline())
                #saveFile.close()
                
                print("Enter Name For Save File")
                gameState[0] = input()
                print (gameState)
                
                saveFile = open("saveFile.txt","w")
                saveFile.write(gameState[0])
                saveFile.close()

                saveFile = open("saveFile.txt","r")
                print(saveFile.readline())
                saveFile.close()

#get save file name
# def getSaveName():
#     saveFile = open("saveFile.txt","r")
#     print(saveFile.readline())
#     saveName = saveFile.readline()
#     return saveName

#run game loop
def gameLoop(gameState):
    print('start game loop', gameState)
    #Define variables
    titleLeft = basicFont.render('Choice the code to move the bear to the tree', False, (255, 255, 255))
    answer = 0 #0=false 1=true
    #Create Buttons

    #initiale split screen update
    #if init is true, then the split screen loop will only run once to update screen
    #if init is false, then the split screen loop will run until stopped
    init = 'true'

    #Menu Loop
    while gameState[1] == 'gameLoop':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(titleLeft, (210,70))
            #Draw Images
            #check for mouse hover
            #Draw Buttons
            #if button hovered change img to hovered image
            #check for mouse click

            #run split screen loops
            gameState[2] = 'right'
            rightSplitScreen(gameState, init)
            if gameState[1] == 'start':
                break
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(titleLeft, (210,70))
            leftSplitScreen(gameState, init)
            init = 'false'



        pygame.display.update()
        mainClock.tick(60)

#right split screen loop
def rightSplitScreen(gameState, init):
    print('start right Split Screen', gameState)
    #Create Variables
    level1Title = basicFont.render('Level 1', False, (255, 255, 255))
    level2Title = basicFont.render('Level 2', False, (255, 255, 255))
    level3Title = basicFont.render('Level 3', False, (255, 255, 255))
    correctResult = basicFont.render('Correct', False, (255, 255, 255))
    incorrectResult = basicFont.render('Incorrect', False, (255, 255, 255))
    color = 0
    exit = 'false'
    seconds = time.time()
    #gameState[4] 0 = false 1 = true
    #lvl1 left is true(1)
    #lvl2 
    #lvl3 


    #import images
    choiceRightImg = pygame.image.load(r'graphics\questions\lvl1false.PNG')
    choiceLeftImg = pygame.image.load(r'graphics\questions\lvl1true.PNG')
    choiceRightImg2 = pygame.image.load(r'graphics\questions\lvl2false.PNG')
    choiceLeftImg2 = pygame.image.load(r'graphics\questions\lvl2true.PNG')
    #choiceRightImg3 = pygame.image.load(r'graphics\questions\lvl3false.PNG')
    #choiceLeftImg3 = pygame.image.load(r'graphics\questions\lvl3true.PNG')
    lvlOneImg = pygame.image.load(r'graphics\questions\lvl1Map.PNG')
    lvlTwoImg = pygame.image.load(r'graphics\questions\lvl2Map.PNG')
    lvlThreeImg = pygame.image.load(r'graphics\questions\lvl3Map.PNG')
    
    #Create Buttons
    btn1 = buttonClass.buttonClass(runCodeBtn, (win.get_width() / 2) + 300, (win.get_height() / 2) + 250, basicFont, '', 35, 15) #'Run Code'
    btn1H = buttonClass.buttonClass(runCodeBtnAlt, (win.get_width() / 2) + 300, (win.get_height() / 2) + 250, basicFont, '', 35, 15) #'Run Code'
    btn2 = buttonClass.buttonClass(saveGameBtn, (win.get_width() / 2) - 150, (win.get_height() / 2) + 250, basicFont, '', 35, 15) #'Save Game'
    btn2H = buttonClass.buttonClass(saveGameBtnAlt, (win.get_width() / 2) - 150, (win.get_height() / 2) + 250, basicFont, '', 35, 15) #'Save Game'
    btn3 = buttonClass.buttonClass(answer1Btn, (win.get_width() / 2) + 300, (win.get_height() / 2) + 125, basicFont, '', 35, 15) #'choice right lvl1'
    btn3H = buttonClass.buttonClass(answer1BtnAlt, (win.get_width() / 2) + 300, (win.get_height() / 2) + 125, basicFont, '', 35, 15) #'choice right lvl1'
    btn4 = buttonClass.buttonClass(answer2Btn, (win.get_width() / 2) - 150, (win.get_height() / 2) + 125, basicFont, '', 35, 15) #'choice left lvl1'
    btn4H = buttonClass.buttonClass(answer2BtnAlt, (win.get_width() / 2) - 150, (win.get_height() / 2) + 125, basicFont, '', 35, 15) #'choice left lvl 1'
    #Menu Loop
    while gameState[2] == 'right':
        for event in pygame.event.get():
            print ('Right Split Screen Running')
            seconds = seconds + 1
            print ('time: ', seconds)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Draw Images and strings
            if gameState[3] == 1: #if level == 
                win.blit(level1Title, (175,140))
                win.blit(choiceRightImg, (win.get_width() - 394, 225))
                win.blit(choiceLeftImg, (win.get_width() - 800 , 225))
                win.blit(lvlOneImg, (50 , 225))
            if gameState[3] == 2: #if level == 2
                win.blit(level2Title, (175,140))
                win.blit(choiceRightImg2, (win.get_width() - 394, 225))
                win.blit(choiceLeftImg2, (win.get_width() - 800 , 225))
                win.blit(lvlTwoImg, (50 , 225))



            #check for mouse hover
            btn1Hov = imgHover(btn1)
            btn2Hov = imgHover(btn2)
            btn3Hov = imgHover(btn3)
            btn4Hov = imgHover(btn4)
            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)
            if btn2Hov == True:
                btn2H.draw(win)
            else:
                btn2.draw(win)
            if btn3Hov == True:
                btn3H.draw(win)
            else:
                btn3.draw(win)
            if btn4Hov == True:
                btn4H.draw(win)
            else:
                btn4.draw(win)
            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click run code btn")
                    gameState[2] = 'left'
                if btn2Hov == True:
                    print("mouse click start menu btn")
                    gameState[1] = 'start'
                    gameState[2] = 'stop'
                if btn3Hov == True:
                    print("mouse click choice right btn")
                    if gameState[3] == 1:
                        gameState[4] = 0 #0 = false 1 = true
                        win.blit(incorrectResult, (950,150))
                    if gameState[3] == 2:
                        gameState[4] = 0 #0 = false 1 = true
                        win.blit(incorrectResult, (950,150))
                if btn4Hov == True:
                    print("mouse click choice left btn")
                    if gameState[3] == 1:
                        gameState[4] = 1 #0 = false 1 = true
                        win.blit(correctResult, (560,150))
                    if gameState[3] == 2:
                        gameState[4] = 1 #0 = false 1 = true
                        win.blit(correctResult, (560,150))
            print (gameState)
            #check init state
            if init == 'true':
                print ('break right split screen loop')
                break

        pygame.display.update()
        mainClock.tick(60)

#left split screen loop
def leftSplitScreen(gameState, init):
    print('start left Split Screen', gameState)
    #Define Variables
    passed = 0
    clock = pygame.time.Clock()

    level1 = Level('level1')
    level2 = Level('level2')
    level3 = Level('level3')
    dt = clock.tick() / 20

    #Create Buttons
    btn1 = buttonClass.buttonClass(stopBtn, (win.get_width() / 2) - 500, (win.get_height() / 2) + 200, basicFont, '', 35, 15) #'stop'
    btn1H = buttonClass.buttonClass(stopBtnAlt, (win.get_width() / 2) - 500, (win.get_height() / 2) + 200, basicFont, '', 35, 15) #'stop'
    #Menu Loop
    while gameState[2] == 'left':
        for event in pygame.event.get():
            print ('Left Split Screen Running')
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #level one loop
            if gameState[3] == 1: #check which level player is on
                if gameState[4] == 1: #true
                    level1.run(dt)
                    level1.player.move_up()
                    level1.player.move_up()
                    passed = 1

                if gameState[4] == 0: #false
                    level1.run(dt)
                    level1.player.move_up()
                    level1.player.move_down()
                    passed = 0


            #level two loop
            if gameState[3] == 2: #check which level player is on
                if gameState[4] == 1: #true
                    level2.run(dt)
  
                    passed = 1

                if gameState[4] == 0: #false
                    level2.run(dt)

                    levelCheck(passed)
            #
            #
            #

            #Draw Images
            #check for mouse hover
            btn1Hov = imgHover(btn1)
            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)
            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click stop btn")
                    gameState[2] = 'right'
                    #levelCheck
                    if gameState[4] == 1:
                        gameState[3] = gameState[3] + 1
            #check init state
            if init == 'true' or gameState[1] == 'start':
                break

        pygame.display.update()
        mainClock.tick(60)

#main
def main(gameState):
    #sets default gamestate ['save file', 'current menu']
    print(gameState)

    #update gamestate save name
    #gameState[0] = getSaveName()
    print(gameState)
    

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Displays current menu
        if gameState[1] == 'exit':
            print('exit')
            exit()
        if gameState[1] == 'start':
            print('run start menu')
            startMenu(gameState)
            print('exit start menu')
        if gameState[1] == 'gameLoop':
            gameLoop(gameState)
            print('exit game loop')

        pygame.display.update()
        mainClock.tick(60)

main(gameState)

