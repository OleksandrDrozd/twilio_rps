# These two functions translate value from integer to string and vice versa.

# Possible human player moves.
rock = ['Rock', 'rock', 'ROCK']
paper = ['Paper', 'paper', 'PAPER']
scissors = ['Scissors', 'scissors', 'SCISSORS']
all_moves = rock + paper + scissors


# From string to integer.
def from_string_to_integer(string):
    if string in rock:
        return 1
    elif string in paper:
        return 2
    elif string in scissors:
        return 3


# From integer to string.
def from_integer_to_string(integer):
    if integer == 1:
        return 'Rock'
    elif integer == 2:
        return 'Paper'
    elif integer == 3:
        return 'Scissors'
