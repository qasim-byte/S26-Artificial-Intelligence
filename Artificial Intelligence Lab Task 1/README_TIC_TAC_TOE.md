# TIC TAC TOE GAME — Documentation ✅

**Author:** Muhammad Qasim Ashfaq  
**Roll No:** SU92-BSAIM-S25-030  
**Section:** BSAI-3A  
**Lab:** Lab Task 1 — Artificial Intelligence Subject  
**Date:** January 30, 2026

---

## 🔧 Project Overview
A simple two-player Tic Tac Toe console game implemented in Python. The program lets two players take turns (decided by a random toss) to place ❌ and ⭕ on a 3x3 board by entering a number between 0 and 8.

## ✨ Features
- Console-based interactive Tic Tac Toe game
- Random toss to decide who starts
- Clear board display using positions 0–8
- Win/draw detection and end-of-game messages
- No external libraries required (pure Python)

## 🧾 Files
- `TIC TAC TOE GAME.py` — main game script
- `README_TIC_TAC_TOE.md` — this documentation

## 🖥️ Requirements
- Python 3.8+ (most Python 3.x versions will work)
- Works on Windows, macOS, and Linux consoles

## ▶️ How to run
Open a terminal, change to the directory containing the script, and run:

```
python "TIC TAC TOE GAME.py"
```

(Use quotes because the file name contains spaces.)

## 🎮 How to play
1. Run the script. A random toss decides who starts.
2. Players enter a number between 0 and 8 to place their mark on the board.
   - Board positions mapping:

```
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

3. The game displays the board after each move and announces a winner or a draw.

## 🧩 Code Structure (key functions)
- `custom_sum(a, b, c)` — helper that returns the sum of 3 values (used in win checking)
- `printboard(first_player, second_player)` — prints the current board state
- `checkwin(first_player, second_player)` — checks all win conditions and announces the winner
- Game loop — handles toss, player input, move validation, win/draw checks

> Note: board state is stored using two lists, `first_player` and `second_player`, with 1 indicating a move at that index.

## ✅ Example Output (snippet)
```
		 | Welcome To Tic Tac Toe! |
		 | Player 1 is '❌' and Player 2 is '⭕' |
Player 1 --> '❌' wins the toss ✨ and will start first

   0     |  1    |   2
---------|-------|-------
   3     |  4    |   5
---------|-------|-------
   6     |  7    |   8

		|  ❌'s Turn !   |
Please Enter any Value :
```

## 💡 Possible Improvements
- Add input prompt validation with clearer messages and retries
- Implement a single-board list with symbols instead of two lists
- Add computer (AI) opponent using Minimax
- Add GUI with Tkinter, Pygame, or a web-based UI

## 📌 Notes
- The script prints a friendly message when the match ends: "Match Over ! Game made with ❤ by Qasim"
- The program uses simple integer-based move mapping for console input.



**Status:** Documentation created — file saved as `README_TIC_TAC_TOE.md` ✅
