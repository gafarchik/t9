# T9
This program is a t9 prototype in python. It is based on a tree-like basis. All this is connected using the easy gui
## Install
To install, open the install.py file or write commands to the console
____
```
pip3 install keyboard
pip3 install tkinter
```
## Using
To run the program, open the start.py file and you will be greeted with a fairly simple interface. This program has its own dictionary for 1000 words, but if you need some other dictionary, then you can change it in the settings section, which is indicated by the corresponding button.After setting, we return to the main menu through the button that appeared instead of the settings button. In the main menu, press start and wait for a couple of seconds. Then a new window will open. After pressing the button on the keyboard, you will see tips in this window. To close it, click the red cross in the upper right corner of the application.
## libraries
This program used such libraries
```
Tkinter
Keyboard
time
threading
```
### Tkinter
Tkinter is the simplest gui library from python developers. It differs from the rest by its prostate.
### Keyboard
Keyboard is a library on which reading data from the keyboard is built. It has many advantages, it is quite easy to use and easy to write code. 3 words are enough for you to count the pressed key
```Python
keyboard.read_key()
```
### time 
standard time library in python
### threading
standard multithreading library
