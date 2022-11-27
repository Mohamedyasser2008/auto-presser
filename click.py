from pydirectinput import press
from time import sleep


class Click():
    def __init__(self, x):
        """
        This takes a string contains button name, time between each click and single or double click
        Separated by spaces.
        Ex: "capslock 20 yes"
        yes can be replaced with (repeat, double, true, r, t, d, y)   Note:doesn't matter lower or upper case.
        """

        self.active = True

        self.x = x.split(" ")
        try:self.x[2] = (
        self.x[2].lower() == "repeat" or 
        self.x[2].lower() == "yes" or
        self.x[2].lower() == "double" or 
        self.x[2].lower() == "d" or 
        self.x[2].lower() == "true" or 
        self.x[2].lower() == "t" or 
        self.x[2].lower() == "y" or 
        self.x[2].lower() == "r"
        )
        except:pass

        def clicker(button, timebet, double=False):
            sleep(4)
            if double:
                while True:
                    press(button)
                    press(button)
                    sleep(float(timebet))
                    if not self.active:
                        break
                    
            else:
                while True:
                    press(button)
                    sleep(float(timebet))
                    if not self.active:
                        break

        try:clicker(self.x[0], self.x[1], self.x[2])
        except:clicker(self.x[0], self.x[1])