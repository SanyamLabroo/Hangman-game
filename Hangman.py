#Downloading the libraries/modules
from itertools import chain, repeat
import random
import time
import os
import json

#For taking the name of the player
name = input("Enter your name: ")

#For clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

clear()

#Initializing the initial tries to 0
tries = 0

time.sleep(1)
print("Welcome to Hangman game" , name , "\n")

#Instructions of the game
rules = ["The rules of this game is very simple!", "You will be Shown some words & You have to remember them!",
        "Then a file in the blanks will appear & you have to fill them with the right word.",
        "You will be given 3 chances to guess the word right.", "If you guess the right word within the limit, You Win!",
        "And You will save a man from getting Hanged.", "And If you lose, The man dies!", 
        "I hope you understood the Instructions!", "So lets start the game!"]

#For printing the Instructions
for i in chain.from_iterable(repeat(rules, 1)):
    time.sleep(3)
    print(i, "\n")

#Function for showing the Man which the palyer has to save
def man_help():
    
    time.sleep(1)
    print("      O  -save me please!   ")
    print("    / | \   ")
    print("     / \    ")

#Function for showing that the player has lost the game and the man is dead
def man_dead():
    
    print("You Lost!\nAs You are out of guesses!\n\n")
    time.sleep(2)
    print("     O_|    ")
    print("    /|\      ")
    print("    / \     ")
    time.sleep(1)
    print("\nYou just killed the Man!", name, "\n")
    exit()
    
#Function for showing that the player has won the game and he saved the man
def man_save():
    
    print("\nYou Won!\n\n")
    time.sleep(1)
    print("      O  -Thank You So Much!   ")
    print("    / | \   ")
    print("     / \    ")
    time.sleep(1)
    print("\nCongractulations! You saved the man.", name, "\n")
    exit()

#For execution of the man function
print("\nHere is The Man You have to save!")
time.sleep(2)
man_help()

time.sleep(3)
clear()

print("Now, The words which you have to remember are: ")

#For loading the words which are in a json file
Words = json.load(open("C:\\Users\\HP\\OneDrive\\Desktop\\Python\\Projects\\Hangman\\Words.json"))

#For loading the words 
for i in Words:
    print(i)
    time.sleep(2)

clear()

#For selecting a random word
word = random.choice(Words)

correct = word
length = len(word)
length = str(length)

#For showing a hint to player
hint = random.choice(length)

#For playing the game until the tries are over
while True:
    
    #For printing the Hint
    print("Hint is, that the word is " + hint + " letters long")
    time.sleep(1)
    
    #For making a guess
    guess = input("Guess the Word: ")
    
    #If the guessed word is not in the words then this condition will execute
    if guess not in Words:
        
        print("Word is not in list!\nTry Again!")
        continue
    
    #Tries increases with each guess made
    tries = tries + 1
    
    #If the guesses exceed 3 then this condition will execute
    if tries > 2:
        
        man_dead()
    
    #If the player has guessed the right word then this will execute
    if guess == word:
        
        man_save()
        
    #If the player has guessed wrong word then this will execute
    elif guess != word:
        
        print("OOPS Wrong guess!\nTry again...")
        continue
    
    #If the user inputs something else then this will be executed
    else:
        print("Wrong Input!\nTry again later!")
        exit()

