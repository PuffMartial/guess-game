secret_word = input("enter the secret word: ")
guess_limit = int(input("enter the guess limit: "))
print("\n\n\n\n\n\n")
print("pass over the game to you friend")
guess = ""
while guess != secret_word:
    num_of_guesses += 1
    if(num_of_guesses == guess_limit):
        print("well i guess you lose")
        break
    
    if (guess != ""):
        print("try again")
        guess = input("enter the guess: ")

    if(guess == secret_word):
        print("CONGRATULATIONS YOU WIN")