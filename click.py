from pydirectinput import press
from time import sleep
from threading import Thread

class Clicker():
    """
    This class is used to simulate pressing buttons on keyboard.
    This class takes 3 parameters:
    1-but: button to press , 2-time: time between each press , 3-double: 1 or 2 clicks every ciycle (True is 2, False is 1)\n
    To start clicking use method start() , To stop clicking use method stop()
    Note: The parameter double is set by default to False 
    """
    def __init__(self, but:str, time:float, double=False):
        self.but = but
        self.time = time
        self.double = double

        self.active = True
        
    def start(self) -> None:
        def cc():
            if self.double:
                sleep(3.5)
                while self.active:
                    press(self.but)
                    press(self.but)
                    sleep(float(self.time))
            else:
                sleep(3.5)
                while self.active:
                    press(self.but)
                    sleep(float(self.time))
        Thread(target=cc).start()

    def stop(self) -> None:
        self.active = False