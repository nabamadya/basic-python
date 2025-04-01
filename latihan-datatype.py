#Data types
#1 strings
#print(type("Hello World"))
print("Hello World!"[4])

score = float(input("What is your score? "))

if score >= 90:
    age = int(input("What is your age? "))
    if age < 10:
        print("You are young.")
    else:
        print("You are older.")
elif score >= 80:
    print("You are Grade B!")
elif score >= 70:
    print("You are Grade C!")
elif score >= 60:
    print("You are Grade D!")
else:
    print("You are Grade F! :((( ")

