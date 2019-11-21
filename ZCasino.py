# This file houses the code of ZCasino, a game of adapted roulette
import os 
from random import randrange
from math import ceil

# Declaration of the starting variables
Cash = 1000 # We have $ 1000 at the beginning of the game
continue_part = True # Boolean which is true as long as we have to continue the game

print("You sit at the roulette table with", Cash, "$.")

while continue_part:  # As long as we have to continue the game we ask the user to enter the number on which he will bet
    number_put = -1
    while number_put < 0 or number_put > 49:
        number_put = input("Type the number you want to bet on (between 0 and 49) : ")
        # We convert the number wagered
        try:
            number_put = int(number_put)
        except ValueError:
            print("You have not entered a number")
            number_put = -1
            continue
        if number_put < 0:
            print("This number is negative")
        if number_put > 49:
            print("Ce nombre est supérieur à 49")

    # Now we select the amount to bet on the number
    bet = 0
    while bet <= 0 or bet > Cash:
        bet = input("Enter the amount of your bet : ")
        # We convert the bet
        try:
            bet = int(bet)
        except ValueError:
            print("You did not enter a number")
            bet = -1
            continue
        if bet <= 0:
            print("The entered stake is negative or zero.")
        if bet > Cash:
            print("You can only bet so much, you only have", Cash, "$")

    # The number bet and bet have been selected by
    # the user, we spin the roulette wheel
    winning_number = randrange(50)
    print("The roulette turns ... ... and stops on the number", winning_number)

    # We establish the player's win
    if winning_number == number_put:
        print("Congratulations, you get", bet * 3, "$ !")
        Cash += bet * 3
    elif winning_number % 2 == number_put % 2: #  they are the same color
        bet = ceil(bet * 0.5)
        print("You bet on the right color, you get", bet, "$")
        Cash += bet
    else:
        print("Sorry the friend, it's not for this time, you lose your bet.")
        Cash -= bet

    # Interrupt the game if the player is ruined
    if Cash <= 0:
        print("You're ruined! It's the end of the game.")
        continue_part = False
    else:
        # We display the player's Cash
        print("You have now", Cash, "$")
        quitter = input("Do you want to leave the casino (yes / no)? ")
        if quitter == "yes" or quitter == "YES":
            print("You leave the casino with your winnings.")
            continue_part = False

# We pause the system
os.system("pause")