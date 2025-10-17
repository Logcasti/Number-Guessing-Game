# Guessing Game
This is an independent Python command-line utility designed to engage the user in a multi-level number guessing challenge, with a focus on robust structure and enhanced replayability.

## Key Features

* **Three Difficulty Levels:** Includes Easy, Hard, and Hardest modes, offering different number ranges and hint types (e.g., proximity hints in Level 2).
* **Post-Game Replay Menu:** Implements a continuous main loop with a menu that allows users to **selectively replay** any of the three levels, replay the entire sequence, or quit the application.
* **Clean Architecture:** Core level logic is encapsulated in dedicated functions (**`L1()`**, **`L2()`**, **`L3()`**) for better **separation of concerns** and **modularity**.
* **Total Score Tracking:** Includes a dedicated **`Total_Tries` function** to calculate and report the combined score across all levels.
* **Robust Input Validation:** Utilizes `try/except` blocks in the `Pick_Number()` and `Continue_Level()` functions to handle non-numeric input and ensure correct program flow.
* **Level Progression Control:** Includes logic to allow the player to **replay the current level** or **continue** to the next one after a successful guess.

## What I Learned

This project helped solidify understanding of essential Python principles and software design:

1. **Function Abstraction and Scope:** Mastering the use of the **`return` statement** to retrieve calculated data (total tries) from isolated level functions.
2. **Modular Design:** Successfully abstracting complex game logic (each level) into distinct functions for improved code clarity and maintenance.
3. **Application State Management:** Implemented a **top-level `while True` loop** and menu logic to control continuous application execution and provide flexible replay options.
4. **Complex Flow Control:** Effective use of **nested `while` loops** and the **`continue`** statement for reliable input prompting, continuous level execution, and state management (like resetting tries on level replay).
5. **Data Type Management:** Gained practical experience in managing inconsistent return types (string vs. integer) from different functions and ensuring safe conversion for arithmetic in the `Total_Tries` function.

## How to Run the Program

1. Run from Bash
2. Run in File Explorer
3. Run in an IDLE
