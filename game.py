### Settings

import words
wordList = words.words.upper().split(' ')

startLife = 5
startTimer = 20
minTimer = 5
timerDecreaseInSec = 1
pointsIncrement = 50

### Imports 

from random import randrange
import time
from os import system, name

### Global Vars

life = startLife
points = 0
timer = startTimer
currentLetters = ''
randomWord = ''

### SCREENS

#startScreen
def startScreen():
    clear()
    print('')
    print('')
    print('###################################')
    print('#                                 #')
    print('#          Willkommen zum         #')
    print('#      Python Word Bomb Game!     #')
    print('#                                 #')
    print('#    siehe Regeln mit: "regeln"   #')
    print('#     ueberspringe mit: "skip"    #')
    print('###################################')
    print('')

#statusScreen
def statusScreen():
    clear()
    print('')
    print('')
    print('###################################')
    print('#                                 #')
    print('#    LEBEN:' + str(life) + '       PUNKTE:' + str(format(points, '05d')) + '   #')
    print('#                                 #')
    print('#      DEINE BUCHSTABEN: ' + currentLetters + '      #')
    print('#                                 #')
    print('#                                 #')
    print('###################################')
    print('')

#rulesScreen
def rulesScreen():
    clear()
    print('')
    print('')
    print('###################################')
    print('#                                 #')
    print('#      1.Dein Wort muss die       #')
    print('# Buchstabenkombination enthalten #')
    print('#                                 #')
    print('#     2. Nur Deutsche Woerter     #')
    print('#                                 #')
    print('###################################')
    print('')

#gameOverScreen
def gameOverScreen():
    clear()
    print('')
    print('')
    print('###################################')
    print('#                                 #')
    print('#          GAME OVER!!!           #')
    print('#                                 #')
    print('#                                 #')
    print('#          PUNKTE:' + str(format(points, '05d')) + '           #')
    print('#                                 #')
    print('###################################')
    print('')
 
### FUNCTIONS

# runGame
def runGame():
    startScreen()
    print('')
    userInput = input('Starte das Spiel mit Enter: ')
    if userInput == 'regeln':
        rulesScreen()
        print('')
        input('Starte das Spiel mit Enter: ')
        runRound()
    else:    
        runRound()

# runRound
def runRound():
    setLetters()
    start = time.time()
    while time.time() - start < timer:
      
        timeLeft = timer - int(time.time() - start)
        
        statusScreen()
        print('Du hast noch ' + str(timeLeft) + ' sekunden zeit.')
        userInput = input('Dein Wort mit '+ currentLetters +': ')
        if userInput == 'skip': break
        if userInput == 'regeln': 
            rulesScreen()        
            print('')
            input('fortfahren mit Enter: ')
        timeLeft = timer - int(time.time() - start) 
        checkWord(currentLetters, userInput.upper(), timeLeft)

    toLate()

# setLetters
def setLetters():

    global currentLetters 
    global randomWord

    randomWord = wordList[randrange(len(wordList) -1)]
    if len(randomWord) < 3:setLetters
    if len(randomWord) == 3:lettersStartPoint = 0 
    else:
        lettersStartPoint = randrange(len(randomWord)-3)
    currentLetters = randomWord[lettersStartPoint:lettersStartPoint+3].upper()

# checkWord
def checkWord(letters, word, timeLeft):

    
    global points
    global timer

    if letters not in word:

        statusScreen()
        print(word + ' enthaelt die Buchstabenkombination ' + letters + ' nicht!')
        input('fortfahren mit Enter: ')
    
    else:
        if word in wordList:
            if timeLeft > 0:

                pointsToAdd = pointsIncrement * (startTimer - timer + timeLeft)
                points = points + pointsToAdd
                statusScreen()

                if timer > minTimer:
                    timer = timer-timerDecreaseInSec
           
                print(word + ' ist Richtig! Dir werden ' + str(pointsToAdd) + ' Punkte gutgeschrieben. Du hast jetzt ' + str(points) + ' Punkte')
              
                input('Starte die naechste Runde mit Enter: ')
                runRound()
            
            
        else:
            
            statusScreen()
            print('Wir konnten kein Wort namens ' + word + ' finden')
            input('fortfahren mit Enter: ')

# toLate
def toLate():

    global life 
    global points 
    global timer 
    global currentLetters 

    life = life - 1

    


    if life > 0:
        statusScreen()
        print('Du warst zu langsahm!')
        print(randomWord + ' waere eine möglichkeit gewesen.')
        input('Beginne die nächste Runde mit Enter')
        runRound()
    else:

        gameOverScreen()
        print('Du warst zu langsahm!')
        print(randomWord + ' waere eine möglichkeit gewesen.')
        input('Starte das Spiel mit Enter: ')
        life = startLife
        points = 0
        timer = startTimer
        currentLetters = ''
        runGame()

#clear
def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
    _ = system('clear')

###############

runGame()



















