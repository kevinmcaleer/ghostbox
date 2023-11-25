# GhostBox - the Paranormal Ghost Detection kit

Built using Raspberry Pi Pico, [Pimoroni](https://www.pimoroni.com) Display Pack 2.0 and some living flame LEDs

---

There is a write-up of this project over at Kevsrobots.com - <https://www.kevsrobots.com/blog/ghostbox.html> where you can also download the STL files, and find the bill of materials.

There are 4 files that will need copying over to the Pico:

* `ghostbox.jpg`
* `ghostbox.py`
* `ghostwords.txt`
* `gui.py`

## How to copy files to a Pico using Thonny

1. Download [Thonny IDE](https://thonny.org) onto your computer.
1. Set Thonny to standard mode by clicking the `Switch to regular mode` link at the top right of the screen.
1. Quit Thonny and start it again to change it into `Regular Mode`
1. Make sure you can see the files on your computer and also on Thonny; Click the View menu and make sure `Files` option is selected.
1. Right Click the `ghostbox.py` file from the Files list and then select `upload to \` - this will copy the `ghostbox.py` module to the Pico
1. Right Click the `gui.py` file from the Files list and then select `upload to \` - this will copy the `gui.py` module to the Pico
1. Right Click the `ghostbox.jpg` file from the Files list and then select `upload to \` - this will copy the `ghostbox.jpg` module to the Pico
1. Right Click the `ghostwords.txt` file from the Files list and then select `upload to \` - this will copy the `ghostwords.txt` module to the Pico

You can make the Pico automatically launch the ghostbox.py code by renaming it to `main.py` on the Pico.

## How to rename ghostbox.py to main

1. Right Click the `ghostbox.py` file from the Files list and then select rename
2. Change the name to main.py
3. Right Click the `main.py` file from the Files list and then select `upload to \` - this will copy the `main.py` module to the Pico

You can also add more words to the `ghostwords.txt` to increase the vocabulary.ß

---

Check out more fun projects at <https://www.kevsrobots.com>
