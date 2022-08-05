# Settings

import words
wordList = words.words.upper().split(' ')

startLifes = 5
startTimer = 20
minTimer = 7
timerDecreaseInSec = 1
pointsIncrement = 50

# Imports 

from random import randrange
import time

# Global Vars

lifes = startLifes
points = 0
timer = startTimer
currentLetters = ''
randomWord = ''

# Functions

def setLetters():
    global currentLetters 
    global randomWord
    randomWord = wordList[randrange(len(wordList))]
    lettersStartPoint = randrange(len(randomWord)-3)

    
    currentLetters = randomWord[lettersStartPoint:lettersStartPoint+3].upper()


def checkWord(letters, word, timeLeft):

    global points
    global timer

    if letters not in word:
        print('')
        print(word + ' enthaelt die Buchstabenkombination ' + letters + ' nicht')
    
    else:
        if word in wordList:
            if timeLeft > 0:
                points = points + pointsIncrement * timeLeft
                if timer > minTimer:
                    timer = timer-timerDecreaseInSec
                print('')
                print(word + ' ist Richtig! Dir werden ' + str(pointsIncrement * (startTimer - timeLeft)) + ' Punkte gutgeschrieben. Du hast jetzt ' + str(points) + ' Punkte')
                input('Starte die naechste Runde mit Enter')
                runRound()
            
            
        else:
            print('')
            print('Wir konnten kein Wort namens ' + word + ' finden')
   
        

def runGame():
    print('')
    print('Willkommen zum Python Word Bomb game!')
    print('')
    print('Finde ein Wort welches die Buchstabenkombination enthält.')
    print('')
    input('Starte das Spiel mit Enter')
    while lifes > 0:
        runRound()

def runRound():
    setLetters()
    start = time.time()
    print('')
    while time.time() - start < timer:
      
        timeLeft = timer - int(time.time() - start)
        
        print('Du hast noch ' + str(timeLeft) + ' sekunden zeit.')
        userInput = input('Dein Wort mit '+ currentLetters +': ')
        timeLeft = timer - int(time.time() - start) #muss gemacht werden um die time nach dem input zu erfassen
        checkWord(currentLetters, userInput.upper(), timeLeft)

    toLate()


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
        print('')
        print('GAMEOVER du hast ' + str(points) +' Punkte erreicht.')
        input('Starte das Spiel mit Enter')
        lifes = startLifes
        points = 0
        timer = startTimer
        currentLetters = ''
        runGame()

runGame()



















