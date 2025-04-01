# Create a greeting
# Create your word list
# Randomly choose a word from the list you have created
# Ask the user to guess a letter
# bonus make the progress take the input from the suer and make it lowercase
# check if the letter is in the word

name = input("What is your name?")
def greeting(name):
    print(f"Hello, {name}\n")

    wlist = ["apple", "banana", "cherry"]
    for wordlist in wlist:
        print(wordlist)

    choice = str(input("What fruits would you like to choose?"))

greeting(name)




