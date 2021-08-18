# teste_cracha

import pyautogui as p
import time as t

#selecionando Excel
p.moveTo(x=624, y=737,duration=0.2)
p.click()
t.sleep(0.4)
#printing the screen
p.hotkey('printscreen')
# selecionando o paint
p.moveTo(x=953, y=746,duration=0.2)
p.click()
t.sleep(0.2)
#selecionando o paint certo (edição primária)
p.moveTo(x=1057, y=675,duration=0.2)
p.click()
t.sleep(0.2)
#subindo a tela no paint
p.moveTo(x=1428, y=-655,duration=0.2)
p.click()
t.sleep(0.2)
p.click()
t.sleep(0.1)
p.click()
t.sleep(0.1)

#colando no paint
p.keyDown('ctrl')
p.hotkey('v')
p.keyUp('ctrl')

#baixando a tela do paint
p.moveTo(x=1429, y=-124,duration=0.2)
p.click()
t.sleep(0.2)
p.click()
t.sleep(0.1)
p.click()

#selecionando o paint de cola
p.moveTo(x=958, y=748,duration=0.2)
p.click()
t.sleep(0.2)
p.moveTo(x=884, y=681,duration=0.2)
p.click()
t.sleep(0.2)

#selecionando ferramenta de seleção
p.moveTo(x=153, y=-822,duration=0.2)
t.sleep(0.5)
p.click()
t.sleep(0.2)
p.click()
#posicionando o mouse
p.moveTo(x=136, y=-600,duration=0.2)
t.sleep(0.2)

