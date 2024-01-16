# Connect4

Play Connect4 against 5 different Connect4 AIs! 

## Algorithms

### StupidAI

StupidAI always try to go in the same column. Once that column is full, it switches to another column and repeats this process.

### RandomAI

RandomAI randomly selects which column to place its piece in.

### MonteCarloAI

MonteCarloAI uses Monte Carlo tree search (https://en.wikipedia.org/wiki/Monte_Carlo_tree_search) to decide which move to make. In this algorithm, for each move the AI plays 1000 random games against itself and selects the move that led to the best total outcome (+1 for win, 0 for tie, -1 for loss).

### MinimaxAI

MinimaxAI uses the minimax algorithm (https://en.wikipedia.org/wiki/Minimax) to decide which move to make. In this algorithm, for every move the AI builds out a game tree assuming that each player always makes a move to minimize their opponents best possible move. If given sufficient time, this algorithm will always lead to an optimal move. However, because of the time constraints, Minimax AI uses an evaluation function to estimate value of a move based on the number of consecutive pieces a move would lead a player or their opponent to have.

### AlphaBetaAI

AlphaBetaAI uses the minimax algorithm with alpha beta pruning (https://en.wikipedia.org/wiki/Alpha–beta_pruning). The addition of alpha beta pruning allows the algorithm to ignore branches of the game tree that it does not need to explore to find an optimal move. This leads to the algorithm being more efficient than minimax alone.

## Note

The program is currently set up with a time constraint only allowing 0.5 seconds for an AI to make its move. For the MinimaxAI and AlphaBetaAI, their performance will improve drastically if given more time and if the max depth they are set to explore increases.

## Usage

| Command | Description | Datatype | Example | Default |
|---|---|---|---|---|
| -p1 | Agent who will be acting as player 1. Name of agent eg minimaxAI | String | -p1 minimaxAI -p1 monteCarloAI | human |
| -p2 | Agent who will be acting as player 2. Name of agent eg minimaxAI | String | -p1 minimaxAI -p1 monteCarloAI | human |
| -seed | Seed for AI’s with stochastic elements | int | -seed 0 | 0 |
| -w | Rows of gameboard | int | -w 6 | 6 |
| -l | Columns of gameboard | int | -l 7 | 7 |
| -visualize | Bool to use or not use GUI | bool | -visualize True -visualize False | True |
| -verbose | Sends move-by-move game history to shell | bool |-verbose True -verbose False | False |
| -limit_players | Which agents should have time limits. Useful if you want to play an AI but don’t want to have the same time limit. In the format “x,y” where x and y are players. Values that are not 1 or 2 can be used in place of 1 or 2 if the player should not be limited | String | -limit_players 1,2 -limit_players -1,2 (player 1 is not limited) -limit_players 1,-1(player 2 is not limited) | 1,2 |
| -time_limit | Time limit for each player. No effect if a player is not limited. In the format “x,y” where x and y are floating point numbers. | String | -time_limit 0.5,0.5 | 0.5,0.5 |

