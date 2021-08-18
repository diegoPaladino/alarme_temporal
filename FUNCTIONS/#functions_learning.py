#functions_learning

#I learned westerday the functions in python, and i'm very happy because this
#in this exemple, the simple opening of any window with pyautogui it was repeated several times.
#with this soluction, just create a function that will be called whenever it is necessary to open any window.

import pyautogui
import time

def select_excel():
    pyautogui.moveTo(246,-25)
    pyautogui.click()
    time.sleep(0.2)

select_excel()
