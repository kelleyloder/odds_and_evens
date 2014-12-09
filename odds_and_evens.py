# Kelley Loder
# Due: Friday 9/5/2014 @ 6 am
# Two player gambling game (human vs computer) where each player bets an amount
# and whether the total is odd or even decides which player gets that money

# set starting variables
import random
human_total_pennies = 100
computer_total_pennies = 100
max_allowed_bet = 10

# use input to set human to even or odd player type
human_player_type = raw_input("Would you like to be 'odd' or 'even'? ")

# continue asking until the user enters "even" or "odd"
while(human_player_type != "odd" and human_player_type != "even"):
    human_player_type = raw_input("I don't understand. Please type 'odd' or 'even' exactly as shown: ")

# set computer to even or odd based on human input
if(human_player_type == "odd"):
    print "Great! You are odd, and I am even."
else:
    print "Great! You are even, and I am odd."

print "We each start with 100 pennies"

# use input to set human bet
human_bet = input("Please enter a bet value which must be an integer between or including 1 and 10 (enter 0 to quit): ")

# keep asking for human bet until number is an integer between 0 - 10
while (human_bet < 0 or human_bet > max_allowed_bet or human_bet % 1 != 0):
    human_bet = input("Please enter a bet value which must be an integer between or including 1 and 10 (enter 0 to quit): ")

# randomly pick computer bet and calculate total bet
while(human_bet != 0):
    computer_bet = random.randint(1, 10)
    total_bet = computer_bet + human_bet
    print "I chose", computer_bet, "which gives a total of", total_bet, "pennies."

    # figure out if total bet is even or odd
    if(total_bet % 2 == 0):
        print "This means the total bet is even."
        winner = "even"
    else:
        print "This means the total bet is odd."
        winner = "odd"

    # calculate new total pennies left for computer and player 
    if(winner == human_player_type):
        human_total_pennies = human_total_pennies + total_bet
        computer_total_pennies = computer_total_pennies - total_bet
        print "You won this round! Now you have", human_total_pennies, "pennies, and I have", computer_total_pennies, "pennies!"
    else:
        human_total_pennies = human_total_pennies - total_bet
        computer_total_pennies = computer_total_pennies + total_bet
        print "You lost this round! Now you have", human_total_pennies, "pennies, and I have", computer_total_pennies, "pennies!"

    # check that each player has enough money left to keep playing
    if(human_total_pennies >= 2 * max_allowed_bet and computer_total_pennies >= 2 * max_allowed_bet):
        # use input to set human bet
        human_bet = input("Please enter a bet value which must be an integer between or including 1 and 10 (enter 0 to quit): ")
    
        # keep asking for human bet until number is between 0 - 10
        while (human_bet < 0 or human_bet > 10 or human_bet % 1 != 0):
            human_bet = input("Please enter a bet value which must be an integer between or including 1 and 10 (enter 0 to quit): ")
    # if players don't have enough left, set bet equal to 0 to end game
    else:
        human_bet = 0

# game is over, figure out who won and print 
if(computer_total_pennies < human_total_pennies):
    print "You won with a total of", human_total_pennies, "! Nice game, see you next time."
elif(computer_total_pennies > human_total_pennies):
    print "I won with a total of", computer_total_pennies, "! Nice game, see you next time."
else:
    print "We tied with a total of", computer_total_pennies, "! Nice game, see you next time."

