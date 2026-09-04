import random
import time 

print("Welcome to Hangman Game")
name = input("Enter your name: ").strip()

print(f"Hello {name}! Best of Luck!")
time.sleep(1)
print("\nThe game is almost commencing.... v \n Lets play Hangman!")
time.sleep(1.5)

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

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5

    def get_valid_guess(already_guessed: list) -> str:
        while True:
            guess = input("This is the Hangman Word: " + display + " Enter your guess: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
            elif guess in already_guessed:
                print("You have already guessed that letter. Try another one.")
            else:
                return guess

    guess = get_valid_guess(already_guessed)
    already_guessed.append(guess)

    if guess in word:
        already_guessed.extend([guess])
        for index, letter in enumerate(word):
            if letter == guess:
                display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()