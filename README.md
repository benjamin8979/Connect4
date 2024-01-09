# Connect4
Play Connect4 Against 5 different levels of AI!

## Stupid AI

This AI always goes in the middle column until the middle column is full and then repeats this pattern in the next column working its way from the inner columns outward.

## Random AI

This AI randomly selects which column to drop its next piece in.

## MonteCarlo AI

This AI uses Monte Carlo tree search(https://en.wikipedia.org/wiki/Monte_Carlo_tree_search) to decide which move to make. In this algorithm, for each possible move the AI can make, it simulates playing 1000 random games with that starting move and tallies the results (+1 for win, -1 for loss, 0 for tie). After running the simulation for every move, the AI chooses the move that had the best result. 

## Minimax AI

This AI uses the minimax algorithm(https://en.wikipedia.org/wiki/Minimax) to decide which move to make. The minimax algorithm works off of the assumption that each player is always going to make the best move for themselves, and then calculates what the best move to make would be if the assumption were to hold. When given enough time to build a complete game tree, minimax returns an optimal move. However, in this project there is a 0.5 second time limit per move, so minimax uses an evaluation function to estimate the value of a move at a certain depth instead of only returning results at the bottom of the game tree based on wins, losses, and ties.

## AlphaBeta AI

This AI uses the minimax algorithm with alpha-beta pruning(https://en.wikipedia.org/wiki/Alpha–beta_pruning) to decide which move to make. Alpha-beta pruning is an efficiency improvement to the minimax algorithm that eliminates nodes that do not need to be visited to find the optimal move.

## Evaluation Function

Both Minimax AI and AlphaBeta AI rely on the following evaluation function to calculate the value of a move when running the minimax algorithm.

Let A<sub>R</sub> = number of spaces in a row where AI has only 1 consecutive piece\
Let B<sub>R</sub> = number of spaces in a row where AI has 2 consecutive piece\
Let C<sub>R</sub> = number of spaces in a row where AI has 3 consecutive piece\

Let X<sub>R</sub> = number of spaces in a row where opponent has only 1 consecutive piece\
Let Y<sub>R</sub> = number of spaces in a row where opponent has 2 consecutive piece\
Let Z<sub>R</sub> = number of spaces in a row where opponent has 3 consecutive piece\

Let A<sub>C</sub> = number of spaces in a row where AI has only 1 consecutive piece\
Let B<sub>C</sub> = number of spaces in a row where AI has 2 consecutive piece\
Let C<sub>C</sub> = number of spaces in a row where AI has 3 consecutive piece\

Let X<sub>C</sub> = number of spaces in a row where opponent has only 1 consecutive piece\
Let Y<sub>C</sub> = number of spaces in a row where opponent has 2 consecutive piece\
Let Z<sub>C</sub> = number of spaces in a row where opponent has 3 consecutive piece\

f(board<sub>AI</sub>) = ∑<sub>(R=0 to 5)</sub> 2 * A<sub>R</sub> + 20 * B<sub>R</sub> + 200 C<sub>R</sub> +  ∑<sub>(C=0 to 6)</sub> 2 * A<sub>C</sub> + 20 * B<sub>C</sub> + 200 C<sub>C</sub>

f(board<sub>Opponent</sub>) = ∑<sub>(R=0 to 5)</sub> X<sub>R</sub> + 10 * Y<sub>R</sub> + 100 Z<sub>R</sub> +  ∑<sub>(C=0 to 6)</sub> X<sub>C</sub> + 10 * Y<sub>C</sub> + 100 Z<sub>C</sub>

f(board<sub>Total</sub>) = f(board<sub>AI</sub>) - f(board<sub>Opponent</sub>)


