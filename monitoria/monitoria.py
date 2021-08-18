# monitoria

# importing libraries
import schedule as s
import pyautogui as p
import time as t
from datetime import datetime

# declarations
def ciclo():
    p.moveTo(x=815, y=-502,duration=0.3)
    t.sleep(0.3)
    p.doubleClick()
    t.sleep(0.3)
    p.keyDown('ctrl')
    p.hotkey('c')
    p.keyUp('ctrl')
    t.sleep(0.3)
    p.keyDown('alt')
    p.hotkey('tab')
    p.keyUp('alt')
    t.sleep(0.3)
    p.keyDown('ctrl')
    p.hotkey('v')
    p.keyUp('ctrl')
    t.sleep(0.3)
    p.hotkey('enter')
    t.sleep(0.2)
    
    




# abrindo e preparando o ambiente Whatsapp Web
p.moveTo(x=318, y=-27,duration=0.3)
t.sleep(1)
p.click()
t.sleep(1)
p.moveTo(x=231, y=-39,duration=0.3)
t.sleep(1)
p.click()
t.sleep(1)
p.moveTo(x=21, y=-650,duration=0.3)
t.sleep(1)
p.click()



s.every(15).seconds.do(ciclo)
while 1:
    s.run_pending()
    t.sleep(15)