print("welocme to tressure island")
direction=input("Your at a cross road. where do you want to go? left or right\n")
if direction == "left":
    decision = input("You want to swim or wait?\n")
    if decision == "wait":
        door = input("which door you want? red , yellow , blue?\n")
        if door == "yellow":
            print("you win")
        else:
            print("Game over")
    else:
        print("game over")

else:
    print("game over")        