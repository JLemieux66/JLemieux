# import tkinter, pillow, and random

# name to be displayed
    # if letter is a space add 2 spaces (first name / last name)
    # if letter is guessed append letter with space after
    # anything else will be _ 

# game instance
    # instance attributes 
        # randomly selected word 
        # maximum number of attempts (6)
        # current attempts (0) 
        # guessed letters list
        # display

    #  gui 
        # bruins logo banner 
        # hangman images that change based on number of attempts
        # display of the name being guessed (c _ _ r _ _ e)
        # textbox for input
        # play again button (after game won or lost, shouldn't always show)

    # method for selecting name
        # uses random from list of roster

    # method for updating the display of the current state of the word
        # works same as function but this is specific to the instance

    # method for guessing letter is an entry to the textbox
        # has to be valid letter
        # can't be guessed already (checks guessed letters list for this)
        # if it hasn't been guessed, append to list
            # if it's in the word, append the display
            # if it's not in the word, increase max attempts and update the image
        # win if there aren't _ in the display
        # lose if max attempts reaches 6

    # method for resetting game
        # new word
        # attempts at 0
        # clear list
        # world display back to underscores
        # reset hangman images
        # hide play again button


