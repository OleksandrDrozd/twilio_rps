# Function compare_moves takes player and computer moves, compares them and determines the result of the game.


def compare_moves(player, computer):
        if (player == 1 and computer == 1) or (player == 2 and computer == 2) or (
                player == 3 and computer == 3):
            return "It's a tie."

        elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (
                    player == 3 and computer == 2):
            return "You win the round!"

        else:
            return "You lose the round :("

