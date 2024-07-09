# manipulate the python terminal window for visual effects

# get packages
import time
import random

# for window manipulation
import pyautogui
import tkinter as tk


class WindowManipulation:

    def attach_window(self):
        """attach the window to the python script"""
        # in order of preference
        # 1 - python terminal
        # 2 - windows powershell
        # 3 - windows command prompt
        # thats it for now

        # get the terminal window
        try:
            self.app = pyautogui.getWindowsWithTitle("Python")[0]
        except IndexError:
            try:
                self.app = pyautogui.getWindowsWithTitle("Windows PowerShell")[0]
            except IndexError:
                try:
                    self.app = pyautogui.getWindowsWithTitle("Command Prompt")[0]
                except IndexError:
                    print("No terminal window found")
                    raise Exception("No terminal window found")
                
        print("Window found: ", self.app.title)

        return self.app

    def __init__(self):
        # get terminal window
        self.app = self.attach_window()
        self.screen_size = pyautogui.size()

        self.bullets = {} # dictionary to store the bullet windows
        self.root = None # root window to hold the bullet windows

    def center_window(self):
        """center the window"""
        window_width = int(self.screen_size.width/4)
        window_height = int(self.screen_size.height/4)

        print(window_width, window_height)

        self.app.moveTo(window_width, window_height)
        self.app.resizeTo(window_width*2, window_height*2)

    def shake_window(self, intensity = 150, intensity_drop = 0.96, ilterations = 100):
        """shake the window by a certain intensity for a certain number of ilterations"""
    
        # intensity = the intensity of the shake by pixel movement
        # intensity_drop = the amount the intensity drops each ilteration in percentage
        # ilterations = the number of ilterations the shake will last

        x_current, y_current = self.app.left, self.app.top

        for i in range(ilterations):
            int_intensity = int(intensity)
            x_offset = random.randint(-int_intensity, int_intensity)
            y_offset = random.randint(-int_intensity, int_intensity)

            self.app.moveTo(x_current + x_offset, y_current + y_offset)

            time.sleep(0.01)
            intensity = intensity * intensity_drop