import random

# Create a greeting
name = str(input("Siapa namamu? "))
print(f"Hello {name}")

# Create your word list
words = ["apple", "banana", "pinapple"]

# create an empty list
# For each letter in the secret_word add a "_" that will be
# printed to the console
# Example if the word apple "_","_","_","_"
# Randomly choose a word from the list you have created
secret_word = random.choice(words)
print(f"The word is: {secret_word}")
print("You have just 3 guesses left")

display_word = []

for letter in secret_word:
    display_word += "_"
print(display_word)


# Loop trough each of the letters in the chosen word
num = 3
game_over = False
while not game_over:
    # Minta tebak huruf
    guess_word = input("Tebak huruf ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess_word:
            display_word[position] = letter
    if guess_word not in secret_word:
        num += 1
        guesses_left = 3 - num
        print(f"Kamu punya {guesses_left} tebakan lagi")
        if num >= 3:
            print("Tebakan salah semua")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print("Benar Semua!!!")
        game_over = True






