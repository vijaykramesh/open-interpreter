import time

import matplotlib.pyplot as plt
import numpy as np
import pyautogui
from PIL import Image


class Mouse:
    def __init__(self, computer):
        self.computer = computer

    def move(self, *args, x=None, y=None, icon=None, index=None):
        if len(args) > 1:
            raise ValueError(
                "Too many positional arguments provided: click(*args, x=None, y=None, show=True, index=None)\n\nPlease take a computer.screenshot() to find text to click, then use computer.mouse.click(text) if at all possible. This is significantly more accurate."
            )
        elif len(args) == 1:
            text = args[0]
            try:
                x, y = self.computer.display.find_text(text, index)
            except IndexError:
                raise IndexError(
                    f"This text ('{text}') was found multiple times on screen. Please try 'click()' again, but pass in an `index` int to identify which one you want to click. The indices have been drawn on the image."
                )
            except ValueError:
                raise ValueError(f"This text ('{text}') was not found on screen.")
        elif x is not None and y is not None:
            if self.computer.display.is_retina:
                x /= 2
                y /= 2
        elif icon is not None:
            x, y = self.computer.display.find_icon(icon)
        else:
            raise ValueError("Either text, icon, or both x and y must be provided")

        pyautogui.moveTo(x, y, duration=0.5)

    def click(self, *args, **kwargs):
        if args or kwargs:
            self.move(*args, **kwargs)
        pyautogui.click()

    def down(self):
        pyautogui.mouseDown()

    def up(self):
        pyautogui.mouseUp()
