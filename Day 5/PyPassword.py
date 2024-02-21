#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

Pletters = []
Psymbols = []
Pnumber = []

password = ""

for r in range(0, nr_letters):
    RLetterIndice = int(random.randint(0,len(letters)))
    Pletters.append(letters[RLetterIndice  - 1])

for r in range(0, nr_symbols):
    RSymbolIndice = int(random.randint(0,len(symbols)))
    Psymbols.append(symbols[RSymbolIndice  - 1])

for r in range(0, nr_numbers):
    RNumberIndice = int(random.randint(0,len(numbers)))
    Pnumber.append(numbers[RNumberIndice - 1])

password = Pletters + Psymbols + Pnumber

random.shuffle(password)

passString = ""
for p in password:
    passString += p

print(f"Here is your password: {passString}")