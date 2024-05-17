import random
from replit import clear
from art import logo

dealerCards = []
playerCards = []
playing = True

y
def pickUpFirstHand():
    dealerCards.append(pickUpCard())
    playerCards.append(pickUpCard())

    dealerCards.append(pickUpCard())
    playerCards.append(pickUpCard())


def pickUpCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def printPoints(dealerPoint,playerPoint):
    print(f"Dealer points: {dealerPoint}, Player points: {playerPoint}")


def checkBlackJack(dealer,player):

    if (dealerCards[0] + dealerCards[1]) == 21 and (dealerCards[0] == 11 or dealerCards[1] == 11):
        print("dealer blackjack")
        print("Player loses")
        printPoints(dealerPoint,playerPoint)
        exit()

    if (playerCards[0] + playerCards[1]) == 21 and (playerCards[0] == 11 or playerCards[1] == 11):
        print("player blackjack")
        printPoints(dealerPoint,playerPoint)
        if (dealerCards[0] + dealerCards[1]) == 21 and (dealerCards[0] == 11 or dealerCards[1] == 11):
            print("dealer blackjack")
            print("Draw")
            printPoints(dealerPoint,playerPoint)
            exit()

        print("Player Wins")
        printPoints(dealerPoint,playerPoint)
        exit()


def countPoints(dealer,player):
    dealerCount = 0
    playerCount = 0

    for card in dealer:
        dealerCount += card

    for card in player:
        playerCount += card

    if 11 in dealer:
        if dealerCount > 21:
            dealerCount -= 10

    if 11 in player:
        if playerCount > 21:
            playerCount -= 10

    return dealerCount,playerCount


while playing:
    print(logo)

    pickUpFirstHand()

    dealerPoint,playerPoint = countPoints(dealerCards,playerCards)


    print(f"First dealer card is: {dealerCards[0]}")
    print(f"Players cards are: {playerCards}")

    checkBlackJack(dealerCards,playerCards)

    otherCard = input("Do you want another card? Y/N ").lower()

    while otherCard == "y":
        playerCards.append(pickUpCard())
        dealerPoint,playerPoint = countPoints(dealerCards,playerCards)
        checkBlackJack(dealerCards,playerCards)

        if playerPoint > 21:
            print("Player loses")
            printPoints(dealerPoint,playerPoint)
            break

        print(playerCards)
        otherCard = input("Do you want another card? Y/N ").lower()

    while dealerPoint < 16:
        dealerCards.append(pickUpCard())
        dealerPoint,playerPoint = countPoints(dealerCards,playerCards)
        checkBlackJack(dealerCards,playerCards)

        if dealerPoint > 21:
            print("Dealer loses")
            printPoints(dealerPoint,playerPoint)

        printPoints(dealerPoint,playerPoint)

    if dealerPoint > playerPoint:
        print("Player loses")
        printPoints(dealerPoint, playerPoint)
    elif dealerPoint == playerPoint:
        print("It's a draw!")
        printPoints(dealerPoint, playerPoint)
    else:
        print("Player wins")
        printPoints(dealerPoint, playerPoint)

    continuePlaying = input("Would you like to play again? Y/N: ").lower()
    if continuePlaying == "y":
        clear()
        playing = True
        dealerCards = []
        playerCards = []
    else:
        playing = False
