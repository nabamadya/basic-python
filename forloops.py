#fruits = ["apple", "banana", "cherry"]

#for fruit in fruits:
#    print(fruit + " pie")

for num in range(1, 100):
    if num% 3 == 0 and num % 5 == 0:
        print(f"{num} fizzbuzz")
    elif num % 3 == 0:
        print(f"{num} fizz")
    elif num % 5 == 0:
        print(f"{num} buzz")
    else:
        print(num)