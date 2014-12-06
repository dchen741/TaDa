TaDa
====

======================
Files and Contents
======================

Code Overview

interface.py – This file calls the desired interface module that has been set. Right now, it uses functions from textInterface.py, but the interface module could be changed to a GUI interface by only changing what file is imported. It gives a quick overview of set-up and starts the program.

puzzle.py – This file contains the body of how a puzzle is put together. Puzzles are based off this module. For example, the rendezvous puzzle (rendez vous.py) contains the puzzle information and initializes itself through the puzzle module. Each puzzle has sections such as title, lesson, hint, answer and space for code. The puzzle then has an important part and it is the start_puzzle() function. This function, when called, runs the necessary components to run the puzzle for the user. This is funneled into the interface.

simulator.py – This file works with the puzzle to actually simulate what the user puts as their answer. There is a visualizer function in this file that will allow the user to see what mistakes they made and why their solution did not pass. This file is also where the concurrency of the project comes into play because it will spawn threads to run the simulation. For example, in rendez_vous.py, it will actually have alice and bob wait for each other so if the user puts in incorrect code, they will see that they will both be waiting for each other.

textInterface.py – This file is the text portion of the project that the interface relies on. It has code relating to how the code is visualized to the user such as a welcoming screen and other sorts. This is where the puzzles are first found for the user depending on how many they want to see (between 1-3). It also allows the user to view progress and view a dictionary of helpful words/phrases about concurrency, such as what deadlocking is.

rendez_vous.py - This file contains all of the puzzle code for the specific rendez_vous 
project.


======================
How to Run
======================

Unzip the TADA_project.zip. The program can be run from any terminal with Python 2.7.6 (or higher), using the following command:

python interface.py
