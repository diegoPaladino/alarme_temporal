# import libraries
import schedule
import pyautogui as p
import time as t
import winsound
import datetime




# declarations
def buzzer():
    winsound.Beep(500,666)
    winsound.Beep(750,666)
    winsound.Beep(1500,666)
    winsound.Beep(500,666)
    winsound.Beep(750,666)
    winsound.Beep(1500,666)

    
    
def reposicao():
    p.keyDown('win')    #pressionando windows + d para minimizar todas as janelas
    p.hotkey('d')
    p.keyUp('win')
    t.sleep(0.2)
    p.moveTo(x=222, y=-32,duration=0.2)  #mover mouse para selecionar navegador opera
    p.click()
    p.moveTo(x=333, y=-111,duration=0.2)  #mover mouse para selecionar navegador opera e a janela aberta com QUANTITATIVE
    p.click()
    t.sleep(0.2)
    p.moveTo(x=124, y=51,duration=0.2)  #mover mouse para selecionar navegador opera
    p.click()
    t.sleep(0.2)
    p.moveTo(x=560, y=-29,duration=0.2)  #mover mouse para selecionar METATRADER
    p.click()
    print(datetime.datetime.now())
    


# code execution
buzzer()
schedule.every(296).seconds.do(buzzer)
reposicao()
schedule.every(296).seconds.do(reposicao)

while 1:
    schedule.run_pending()
    t.sleep(1)