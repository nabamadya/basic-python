# Create a progress that can take in input of the users name
# save the name in a variable
# pass the variable trough a function and print "Hello ____"

name = input("What is your name?")
def greeting(name):
    print(f"Hello, {name}")

greeting(name)