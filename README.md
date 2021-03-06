# 4-in-a-row game (also called connect-4)
Implementing the board game connect-4

## Update
As of the latest commit, 2 player mode is already implemented, and works as intended. AI not yet implemented.

## Update 2
An AI has been implemented, which uses the Minimax algorithm with a depth of 3. Increasing the depth to 4 results in a delay of a little less than a second (which may or may not be tolerable, depending on the circumstances), and depth of 3 is good enough to beat casual players (like myself).

## Files
- main.py: 2 player mode
- single_player_mode.py: single player mode against AI

## Additional info
The game is made using Python's Pygame library, with Numpy arrays used for storing board states for efficiency. 

## Possible improvements (might implement these in the future)
- Graphics aren't exactly the best and there's definitely room for improvement
- I didn't use alpha-beta pruning so the AI isn't the most efficient (not really a problem for depth <=4)
- Could add some more things to scoring function
- Bundling both single player and 2 player modes into a single executable
