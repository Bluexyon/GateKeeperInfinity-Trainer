# Gatekeeper: Infinity Game Trainer

This is a quick and dirty game trainer (cheating tool) made for the game Gatekeeper: Infinity on Steam. This tool was made for the Python Course during my Cybersecurity course.

## Installation
To install this Program simply download the main.py Script and install the necessary libaries or download the Executable.
#### Libraries and Dependencies
- PySimpleGUI
- pymem

## Usage

To run the Program through the Script first install the dependencies
```bash
pip install Pymem
pip install pysimplegui
```
then simply type the following in your Terminal while the Game Gatekeeper: Infinity is running, which you can get for free on Steam.

```bash
python main.py
```

or run the pre-compiled Executable File while the Game is running.

Afterwards change what ever value you want to a desired value and click on Set.

For Attack Speed depending on the chosen Character I recommend 70 for Hybrid and 20 for Nidium so that the Game Mechanics don't break.

## Possible Errors

If the Game Process is not found at execution the Program shows an Error Window.

If a value can not be modified this can happen because the calculated Pointer was not pointing to the right value at that given time so please restart the game. 
