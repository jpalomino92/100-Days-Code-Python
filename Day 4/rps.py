import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if option == 0:
    print(rock)
elif option == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose: ")

computerChoice = random.randint(0,2)

if computerChoice == 0:
    print(rock)
elif computerChoice == 1:
    print(paper)
else:
    print(scissors)

if option == 0 and computerChoice == 1:
    print("You lose")
elif option == 0 and computerChoice == 2:
    print("You win")
elif  option == 0 and option == computerChoice:
    print("It's a tie!")

if option == 1 and computerChoice == 2:
    print("You lose")
elif option == 1 and computerChoice == 0:
    print("You win")
elif option == 1 and option == computerChoice:
    print("It's a tie!")

if option == 2 and computerChoice == 0:
    print("You lose")
elif option == 2 and computerChoice == 1:
    print("You win")
elif  option == 2 and option == computerChoice:
    print("It's a tie!")







