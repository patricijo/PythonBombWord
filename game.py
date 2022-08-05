### Settings

import words
wordList = words.words.upper().split(' ')

startLifes = 5
startTimer = 20
minTimer = 5
timerDecreaseInSec = 1
pointsIncrement = 50

### Imports 

from random import randrange
import time

### Global Vars

lifes = startLifes
points = 0
timer = startTimer
currentLetters = ''
randomWord = ''

### Functions

# runGame
def runGame():
    print('')
    print('Willkommen zum Python Word Bomb Game!')
    print('')
    print('Finde ein Wort welches die Buchstabenkombination enthält.')
    print('')
    input('Starte das Spiel mit Enter')

    runRound()

# runRound
def runRound():
    setLetters()
    start = time.time()
    print('')
    while time.time() - start < timer:
      
        timeLeft = timer - int(time.time() - start)
        
        print('Du hast noch ' + str(timeLeft) + ' sekunden zeit.')
        print('')
        userInput = input('Dein Wort mit '+ currentLetters +': ')
        if userInput == 'skip': break
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
        print('')
        print(word + ' enthaelt die Buchstabenkombination ' + letters + ' nicht')
    
    else:
        if word in wordList:
            if timeLeft > 0:
                points = points + pointsIncrement * (startTimer - timer + timeLeft)
                if timer > minTimer:
                    timer = timer-timerDecreaseInSec
                print('')
                print(word + ' ist Richtig! Dir werden ' + str(pointsIncrement * (startTimer - timer + timeLeft)) + ' Punkte gutgeschrieben. Du hast jetzt ' + str(points) + ' Punkte')
                print('')
                input('Starte die naechste Runde mit Enter')
                runRound()
            
            
        else:
            print('')
            print('Wir konnten kein Wort namens ' + word + ' finden')

# toLate
def toLate():

    global lifes 
    global points 
    global timer 
    global currentLetters 

    lifes = lifes - 1

    print(randomWord + ' waere eine möglichkeit gewesen.')

    if lifes > 0:
        print('')
        
        print('Du warst zu langsahm und hast noch ' + str(lifes) +' leben.')
        print('')
        input('Beginne die nächste Runde mit Enter')
        runRound()
    else:

        print('')
        print('GAMEOVER du hast ' + str(points) +' Punkte erreicht.')
        print('')
        input('Starte das Spiel mit Enter')
        lifes = startLifes
        points = 0
        timer = startTimer
        currentLetters = ''
        runGame()

###############

runGame()



















