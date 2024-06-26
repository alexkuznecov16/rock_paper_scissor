# Rock, Scissor, Paper Game

This is a simple Rock, Scissor, Paper game implemented using Python and the Tkinter library for the graphical user interface. The game allows the user to play against the computer for three rounds and displays the results of each round and the final outcome.

## Features

- Graphical User Interface (GUI) built with Tkinter
- Randomized computer choices
- Score tracking for both the user and the computer
- Displays round results and the final outcome
- Option to restart the game after completion

## Requirements

- Windows OS (for running the `.exe` file)
- Python 3.x (for running the script directly)
- Tkinter (usually comes pre-installed with Python)

## How to Run

### Using the Executable File

1. **Download the executable file:**
    - Download `main.exe` from the `./dist` directory or from the provided link.

2. **Navigate to the directory containing the executable:**
    - Open the command prompt and change to the directory containing `main.exe`:

    ```bash
    cd path\to\dist
    ```

3. **Run the executable:**
    - In the command prompt, type:

    ```bash
    main.exe
    ```

### Running from Source Code

1. **Clone the repository:**

    ```bash
    git clone https://github.com/alexkuznecov16/rock_paper_scissor.git
    ```

2. **Navigate to the directory containing the script:**

    ```bash
    cd rock_paper_scissor
    ```

3. **Run the script:**

    ```bash
    python rock_scissor_paper_game.py
    ```

## Game Instructions

1. **Start the Game:**
    - Click the "Start" button to begin the game.

2. **Make a Choice:**
    - Choose either "Rock", "Scissor", or "Paper" by clicking the respective button.

3. **Round Result:**
    - A pop-up window will display the result of each round, showing whether you won, lost, or drew, along with the current score.

4. **Next Round:**
    - After viewing the result, the next round will start automatically if the game hasn't reached the third round.

5. **Final Result:**
    - After three rounds, the final result will be displayed on the main window. It will show your score and whether you won or lost against the computer.

6. **Restart or Close:**
    - Click the "Restart" button to play again or the "Close" button to exit the game.

## Code Overview

- **main()**: Initializes the main application window and sets up the start and close buttons.
- **game(container)**: Manages the main game logic, including updating the round count and setting up the buttons for user choices.
- **result(container, user_choose=None)**: Handles the logic for determining the winner of each round, updating scores, and displaying results.
- **restart_game(container)**: Resets the game variables and starts a new game.

## Customization

- Modify the button styles and text by changing the parameters in the `Button` widgets.
- Adjust the window size by changing the `root.minsize` parameters in the `main()` function.

## Acknowledgements

- Tkinter documentation: [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Random module documentation: [Random](https://docs.python.org/3/library/random.html)

---

Feel free to fork the repository and contribute to the project by submitting pull requests. If you encounter any issues or have suggestions for improvements, please open an issue on GitHub. Enjoy the game!
