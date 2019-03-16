# Flat Blue
### A crappy Connect-4 AI
## Purposes:
* Learning how to create a simple adversarial AI
* Fun :)

## How it works:
### Look-Ahead
Flat Blue utilizes a simple look-ahead tree to determine optimal moves. I literally learned about this in class today, so let's see how that works out.

Given a some current state _S_, it calculates all legal moves that can be made. From there, it determines which of _S_'s children yield the most optimal worst-case scenario. In essence, it plans for the worst by assuming the opponent is competent. Flat Blue is honestly just an implementation of the [Minimax algorithm](https://en.wikipedia.org/wiki/Minimax).

### State Evaluation
To evaluate any given state, Flat Blue uses a static evaluation function. This function looks through each row/column/diagonal of length 4, checking if the pieces (if any) in the sample come from the same player. If so, DB increments a value representing that player's level of advantage. At the end of the iteration, the function returns the difference of DB's and the other player's advantage levels. Levels > 0 are considered optimal. Levels < 0 are considered suboptimal.
