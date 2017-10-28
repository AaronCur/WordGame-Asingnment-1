import re
import random
import os.path
import pickle
from collections import Counter
from datetime import datetime

bigWordList = []
smallWordList = []
refinedList = []

index = 0
with open ('words.txt', errors = 'ignore') as df:
    rawdata = df.read()

words = rawdata.split()

##To get rid of all words with less than 3 letters
for i in range(len(words)):
    if(len(words[i])) >=3:
        index+=1
        refinedList.insert(index,words[i])

##Split the remaining words into two lists, one of words more than 7 letters long
##And the other one with words with 3 or more letters
for i in range(len(refinedList)):
    if(len(refinedList[i])) > 7:
        index+=1
        bigWordList.insert(index,refinedList[i])
    if(len(refinedList[i])) >=3:
        index+=1
        smallWordList.insert(index,refinedList[i])

while True:
    leaderboard = {}
    ##To check if the file exists, if not create one
    if(os.path.isfile('highscoretable.pickle') == False):
        with open('highscoretable.pickle', 'wb') as pf:
            pickle.dump(leaderboard, pf)
    else:
        #Read in the file containing the leaderboard and assign to dictionary
        with open('highscoretable.pickle', 'rb') as pf:
            leaderboard = pickle.load(pf)

    playername = input("Enter your name: ")
    starttime = datetime.now()

    ranWord = random.choice(bigWordList)
    print(ranWord)
    ranWord = ranWord.lower()
    cr = Counter(ranWord)

    guesses = []
    guessLength = 7

    #Only allow 7 guesses
    while len(guesses) < guessLength:
        guess = input("Enter a guess: ")
        guess = guess.lower()
        cg = Counter(guess)
        cg = cg - cr
        #Error checks
        if guess in smallWordList:
            if(guess in guesses):
                print('',guess,'',"Has already been guessed")
            elif(len(cg) == 0):
                if(not guess == ranWord):
                    #Append guess to the list
                    guesses.append(guess)
                    print(guesses)
                else:
                        print("You are using the same word as the random word")
            else:
                    print("You are using letters that are not in",'',ranWord,'')
        else:
            print('',guess,'' ,"Is not a word in the dictonary")
    print("No more guesses")
    print(guesses)
    endtime = datetime.now()
    resulttime = endtime - starttime
    resulttime = str(resulttime)
    print('\n')
    print('Congratulations your time is','',resulttime,'')
    print('\n')
    print("Leaderboard")
    #Assign player score and name to dictionary
    leaderboard[resulttime] = playername

    #Write the updated leaderboard back to the file
    with open('highscoretable.pickle', 'wb') as pf:
            pickle.dump(leaderboard, pf)

    #Display the leaderboard top 10
    for k in sorted(leaderboard)[:10]:
        print(leaderboard[k], '->', k)
    print("\n")

    placement = []
    #Sort through the whole dictionary and append times to list in order
    for k in sorted(leaderboard):
        placement.append(k)
    #Find the actual postion of the player
    position = placement.index(resulttime) + 1
    #Only print players postion if they are outside the top 10
    if(position > 10):
        print("You placed",'',position,'',"out of",'',len(placement) - 1)

    #To restart the game on user input
    ret = input('Play again? (y/n): ')
    print("\n")
    if ret.lower()[0] == 'n':
        break
