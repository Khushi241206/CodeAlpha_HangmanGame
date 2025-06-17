import random
words=["apple","banana","lion","orange","purple"]
secret_guess=random.choice(words)
guessed_letters=[]
incorrect_guesses=0
max_incorrect=6

show_word=["_"for _ in secret_guess]
print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses. Try again.\n")

while incorrect_guesses<max_incorrect and "_" in show_word:
    print("Word:"," ".join(show_word))
    print(f"Incorrect guesses left : {max_incorrect-incorrect_guesses}")
    guess=input("Enter a letter:").lower()
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_guess:
        print("Good Guess\n")
        for i in range(len(secret_guess)):
            if secret_guess[i]==guess:
                show_word[i]=guess
    else:
        print("Incorrect guess\n")
        incorrect_guesses+=1

if "_" not in show_word:
    print("Congratulations, you guessed the word: ",secret_guess)
else:
    print("Game Over. The word was : ",secret_guess)