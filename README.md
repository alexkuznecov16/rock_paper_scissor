Rock, Scissor, Paper Game

This is a simple Rock, Scissor, Paper game implemented using Python and the Tkinter library for the graphical user interface. The game allows the user to play against the computer for three rounds and displays the results of each round and the final outcome.
Features

    Graphical User Interface (GUI) built with Tkinter
    Randomized computer choices
    Score tracking for both the user and the computer
    Displays round results and the final outcome
    Option to restart the game after completion

Requirements

    Python 3.x
    Tkinter (usually comes pre-installed with Python)

How to Run

    Clone the repository or download the script file:

    bash

git clone https://github.com/yourusername/rock-scissor-paper-game.git

or download the rock_scissor_paper_game.py file directly.

Navigate to the directory containing the script:

bash

cd rock-scissor-paper-game

Run the script:

bash

    python rock_scissor_paper_game.py

Game Instructions

    Start the Game:
        Click the "Start" button to begin the game.

    Make a Choice:
        Choose either "Rock", "Scissor", or "Paper" by clicking the respective button.

    Round Result:
        A pop-up window will display the result of each round, showing whether you won, lost, or drew, along with the current score.

    Next Round:
        After viewing the result, the next round will start automatically if the game hasn't reached the third round.

    Final Result:
        After three rounds, the final result will be displayed on the main window. It will show your score and whether you won or lost against the computer.

    Restart or Close:
        Click the "Restart" button to play again or the "Close" button to exit the game.

Code Overview

    main(): Initializes the main application window and sets up the start and close buttons.
    game(container): Manages the main game logic, including updating the round count and setting up the buttons for user choices.
    result(container, user_choose=None): Handles the logic for determining the winner of each round, updating scores, and displaying results.
    restart_game(container): Resets the game variables and starts a new game.

Customization

    Modify the button styles and text by changing the parameters in the Button widgets.
    Adjust the window size by changing the root.minsize parameters in the main() function.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    Tkinter documentation: https://docs.python.org/3/library/tkinter.html
    Random module documentation: https://docs.python.org/3/library/random.html

Feel free to fork the repository and contribute to the project by submitting pull requests. If you encounter any issues or have suggestions for improvements, please open an issue on GitHub. Enjoy the game!
