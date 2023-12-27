# Mineswepper Game

## **Terminal version of mineswepper**

This interactive terminal version of Minesweeper randomly places mines on a field with a size and mine count specified by the user. The game initially displays the field without revealing its content, allowing players to navigate through squares:

- If a square has a mine, Player loses.
- If an empty square borders a mine, the game displays the number of adjacent mines.
- If an empty square doesn't border any mines, it remains visible until the entire minefield is revealed.

After the game concludes, the entire field is displayed, including error-checking. Suspected mines can be flagged. Winning is achieved by revealing all empty squares or flagging all mines. If a player steps on a mine, they are informed of the revealed mines. Players can also open flagged squares and reveal connected empty areas.

### **Running the code**
To initiate the program, use the following command:
>python mineswepper.py

### **Required libaries**
Ensure you have the required Python libraries installed:
>pip install time random

You can verify the installed version of Python with the following command:
>pip --version python 

### **Trobleshooting section**
In the rare scenario where the user sets the maximum possible number of bombs, winning becomes possible with a single flag. It is assumed that the player is aware of this process, understanding that all bombs are already identified. For an enhanced gaming experience, consider adjusting the mine count to maintain an optimal level of challenge.

[GUI version of mineswepper](https://github.com/JakubJus/Minesweeper/tree/GUI-Mineswepper)
