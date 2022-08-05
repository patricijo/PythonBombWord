# Settings

from pickle import FALSE, TRUE
import words
wordList = words.words.upper().split(' ')

startLifes = 5
startTimer = 20
minTimer = 7
timerDecreaseInPercent = 10
pointsIncrement = 50

# Imports 

from random import randrange

# Vars

lifes = startLifes
points = 0
timer = startTimer
currentLetters = ''

# Functions

def setLetters():

    #Buchstaben werden aus den wörtern gefiltert um sicher zu stellen das es mindestens eine richtige lösungt gibt.

    randomWord = wordList[randrange(len(wordList))]
    lettersStartPoint = randrange(len(randomWord)-3)

    global currentLetters 
    currentLetters = randomWord[lettersStartPoint:lettersStartPoint+3].upper()


def checkWord(letters, word):
    if letters not in word:
        print('wort enthält die buchstaben nicht')
    else:
        if word in wordList:
            print('gutes wort')
        else:
            print('wort gibt es nicht')
        

setLetters()



print('Willkommen zum Python Word Bomb game!')
print('')
print('#####################################')
print('')
print('Tippe ein wort ein welches folgende Buchstabenenthaelt')
print('')
print(currentLetters)
print('')
userInput = input()
checkWord(currentLetters, userInput.upper())







