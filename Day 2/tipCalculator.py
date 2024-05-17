print("Welcome to the tip calculator.")

totalBill = input("What as the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15 ")
people = input("How many people to split the bill? ")

tipPercentage = "1." + str(tip)


toPay = (float(totalBill) * float(tipPercentage)) / int(people)

toPay = round(toPay ,2)

print (f"Each person should pay: ${toPay}")