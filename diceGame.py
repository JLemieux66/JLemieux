#Import die
from die import Die

#Rolling 2 dice and returning values 1 through 6
def roll_dice(die1, die2):
    return die1.roll(), die2.roll()

#The game
def play_game():
    # starting with 100 points
    points = 100
    # die variables using class for 6 sided die
    die1 = Die(6)
    die2 = Die(6)

    # loop of playing the game
    while points > 0 and points < 1000:
        print("Lemieux's High Rolling 7/11 Casino")
        print(f'Points: {points}')
        #Defines wager as the user input
        wager = input(f'Enter a wager (1-{points}), or type "EXIT" to cash out: ')
        
        if wager.upper() == "EXIT":
            break
        
        #Converts wager to an integer so it can be added/subtracted from points
        wager = int(wager)
        
        #Can't be 0 or more than the amount of points you have
        if wager < 1 or wager > points:
            print("Invalid wager. Please enter a valid wager.\n")
            continue
        
        #The two numbers from randomization become both dice rolls. Sets variables
        dice1, dice2 = roll_dice(die1, die2)
        #Total adds both rolls
        total = dice1 + dice2
        print(f'\nDice rolls: {dice1}, {dice2}\n')
        if total in [7, 11]:
            #Adds wager to point total
            points += wager
            print(f'You won with {total}! Points +{wager}\n')
        elif total in [2, 3, 12]:
            #Subtracts wager from total
            points -= wager
            print(f'You lost with {total}! Points -{wager}\n')
        else:
            print(f'You rolled {total}... Nothing. Roll again!\n')
    #If you win, breaks loop because you won
    if points >= 1000:
        print(f'Congratulations! You won with {points} points.\n')
    #If you exit the game, breaks loop because you walked away
    elif wager.upper() == "EXIT":
        print(f'\nYou walked away with {points} points\n')
    #If you have 0 points and lose, breaks the loop because you lost
    else:
        print(f'You lost with {points} points.')

# main function that allows you to enter back into the game loop after winning, losing, quitting
def main():
    while True:
        play_game()
        choice = input('Do you want to play again? (yes/no): ')
        #If no is entered, break. If yes is entered then the while loop keeps running and plays again
        if choice.lower() != 'yes':
            break

main()