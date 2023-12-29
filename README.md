# Mineswepper Game

## **Graphical interface version of mineswepper**

Experience the classic Minesweeper game in an interactive graphical user interface (GUI) that adds an extra layer of excitement. This version allows users to specify the field size and mine count before diving into the challenging minefield. Here's how the game unfolds:

- The initial display conceals the field's content, prompting players to navigate through the squares.
- Stepping on a square with a mine results in a loss for the player.
- An empty square next to a mine reveals the number of adjacent mines.
- Empty squares without neighboring mines stay visible until the entire minefield is uncovered.

Once the game concludes, the entire field is revealed, including error-checking for flagged mines. Players can mark suspected mines with flags. Winning is achieved by either revealing all empty squares or correctly flagging all mines. In the event of stepping on a mine, players are informed about the revealed mines. Additionally, players can open flagged squares to uncover connected empty areas.

### **Running the code**
To initiate the program, use the following command:
>python mineswepper.py

### **Required libaries**
Ensure you have the required Python libraries installed:
>pip install time random os tkinter


You can verify the installed version of Python with the following command:
>pip --version python 

### **Trobleshooting section**
In a rare scenario where the user sets the maximum possible number of bombs, it becomes possible to win with just a single flag. It is assumed that players are aware of this, recognizing that all bombs are already identified. For an enhanced gaming experience, consider adjusting the mine count to maintain an optimal level of challenge.

The button background is determined by the reset image for a visually appealing interface.

[Terminal version of mineswepper](https://github.com/JakubJus/Minesweeper/tree/Terminal-Mineswepper)
