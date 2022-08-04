# Settings

import words
wordList = words.words.split(' ')

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


def getLetters():
    #Buchstaben werden aus den wörtern gefiltert um sicher zu stellen das es mindestens eine richtige lösungt gibt.
    randomWord = wordList[randrange(len(wordList))]

    
    print(randomWord)


getLetters()



print('Willkommen zum Python Word Bomb game!')

print(wordList[4])

