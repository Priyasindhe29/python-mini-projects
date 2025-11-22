print("WELCOME TO THE ROLLERCOASTER")
height = int(input("What is your height in cm? "))
age = int(input("Enter your age: "))
bill = 0

if height > 120:
    if age <= 12:
        bill = 5
        print("You can ride, your ticket price is $5")
    elif age <= 18:
        bill = 7
        print("You can ride, your ticket price is $7")
    elif age >=45 and age <=55:
        bill = 0
        print("You can ride, your ticket price is $0")
    else:
        bill = 12
        print("You can ride, your ticket price is $12")

    want_photo = input("Do you want photos? (y/n): ")
    if want_photo == "y":
        bill += 3

    print(f"Your total bill is: ${bill}")

else:
    print("You can't ride")
