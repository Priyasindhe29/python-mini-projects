print("WELCOME TO TIP CALCULATOR!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 , or 15?"))
no_of_persons = int(input("How many people to split the bill?"))
tip_percent = tip /100
tip_amount = bill * tip_percent
Bill_with_tip = bill + tip_amount
final_amount = round((Bill_with_tip / no_of_persons),2)
print(f"Each person should pay: ${final_amount}")