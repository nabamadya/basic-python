
import time
choice = int(input("What number would you like to choose?"))
def forloops(choice):
    for num in range(1, choice):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{num} fizzbuzz")
        elif num % 3 == 0:
            print(f"{num} fizz")
        elif num % 5 == 0:
            print(f"{num} buzz")
        else:
            print(num)
print("about to run the progress..")
time.sleep(3)
forloops(choice)

