print("welcome to SP pizza!!!")
size = input("what size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on ypur pizza? y or n : ")
extra_cheese = input("do you want extra cheese? y or n : ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you have entered wrong input.")

if pepperoni == "y":
    if size =="S":
        bill += 2
    else:
        bill +=3
if extra_cheese =="y":
    bill += 1

print(f"your final bill is: ${bill}")

