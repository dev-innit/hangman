import random
import time 

print("Welcome to Hangman Game")
name = input("Enter your name: ")

print("Hi" + name + ", Good Luck!")
time.sleep(2)
print("The game is almost commencing: v n\ Lets play Hangman ")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# a loop to re-execute the game 
def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do you want to play again? y = yes, n = no \n")
    if play_game.lower() == "y":
        main()
    elif play_game.lower() == "n":
        print("Thanks for playing! We expect you back again!")
        exit()