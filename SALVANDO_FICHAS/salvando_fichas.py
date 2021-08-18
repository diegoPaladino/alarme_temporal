# salvando_fichas

import pyautogui as p
import time as t
from datetime import datetime
import tkinter as tk


# executando
# selecionando nome do aluno
p.moveTo(x=522, y=-405,duration=0.1)
t.sleep(0.5)
# indo até o final do campo de nome do aluno
p.dragTo(x=846, y=-405,duration=0.2)
t.sleep(0.2)
# copiando o nome do aluno
p.keyDown('ctrl')
t.sleep(0.1)
p.hotkey('c')
t.sleep(0.1)
p.keyUp('ctrl')
t.sleep(0.1)
# salvando o PDF
p.keyDown('ctrl')
t.sleep(0.1)
p.hotkey('p')
t.sleep(0.1)
p.keyUp('ctrl')
t.sleep(1.5)
p.hotkey('enter')
t.sleep(1.5)
p.moveTo(x=152, y=-142,duration=0.1)
p.doubleClick()
t.sleep(1)
# colando o nome do aluno
p.keyDown('ctrl')
t.sleep(0.1)
p.hotkey('v')
t.sleep(0.1)
p.keyUp('ctrl')
t.sleep(0.5)
p.hotkey('enter')
t.sleep(0.5)
# fechando a janela da salvando_ficha
p.keyDown('ctrl')
t.sleep(0.1)
p.hotkey('w')
t.sleep(0.1)
p.keyUp('ctrl')
t.sleep(0.5)

# p.keyDown('ctrl')
# t.sleep(0.1)
# p.hotkey('w')
# t.sleep(0.1)
# p.keyUp('ctrl')
# t.sleep(0.5)

root = tk.Tk()
root.withdraw()
c = root.clipboard_get()
print(c)
# print(datetime.now(), ' - clipboard copiado')