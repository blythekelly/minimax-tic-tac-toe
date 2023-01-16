# Minimax Tic Tac Toe

## Introduction

This project implements the Minimax artificial intelligence algorithm to produce a user vs. computer Tic Tac Toe game. The Minimax function recursively calls itself until the game reaches a terminal state, a win, draw, or loss. It determines the best possible move for the max player, the computer, to play by maximizing the opportunity that the computer wins the game and minimizing the opportunity for the user to win. The algorithm considers the current state of the game and the possible moves that could be made. It plays each of these possible moves, alternates between the min and max player, and stops once a terminal state is reached. The algorithm can also be viewed as a traversal of the Tic Tac Toe's game tree to determine the best case for the computer's play. Each node in the game tree is a representation of a state in the game, including an empty board as the root node. 




