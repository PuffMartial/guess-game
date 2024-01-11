secret_word = input("enter the secret word")
print("pass over the game to you friend")

guess = ""
while guess != secret_word:
    if (guess != ""):
        print("try again")
        guess = input("enter the guess")
        print("CONGRATULATIONS YOU WIN")