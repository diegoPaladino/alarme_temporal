# Imprimindo_notas

import pyautogui as p
import time as t

count=35
x=1
count = int(count)

# selecionar excel
p.moveTo(x=316, y=-30,duration=0.2)
p.click()
t.sleep(0.3)

while x <= count:
    

    # selecionar número de matrícula
    p.moveTo(x=1011, y=-720,duration=0.2)
    p.doubleClick()
    t.sleep(0.3)

    # copiar número de matrícula
    p.keyDown('ctrl')
    p.hotkey('c')
    p.keyUp('ctrl')
    t.sleep(0.3)

    # mover para o navegador para colar o número de matrícula
    p.moveTo(x=176, y=-587,duration=0.2)
    p.doubleClick()
    t.sleep(0.3)
    p.hotkey('backspace')

    # colar o numero de matricula
    p.keyDown('ctrl')
    p.hotkey('v')
    p.keyUp('ctrl')
    t.sleep(0.3)
    p.hotkey('tab')
    t.sleep(2)

    # selecionar checkbox do aluno
    p.moveTo(x=66, y=-146,duration=0.2)
    p.click()
    t.sleep(0.3)

    # desmarcar checkboxs (2) ("mostrar resultados" e "resultado definitivo")
    p.moveTo(x=155, y=-381,duration=0.2)
    p.click()
    t.sleep(0.3)
    p.moveTo(x=155, y=-354,duration=0.2)
    p.click()
    t.sleep(0.3)

    # clicar em "gerar relatório"
    p.moveTo(x=91, y=-205,duration=0.2)
    p.click()
    t.sleep(0.5)

    # copiando o nome do aluno
    p.moveTo(x=100, y=-682,duration=0.2)
    p.dragTo(x=502, y=-680,duration=0.4)
    p.keyDown('ctrl')
    p.hotkey('c')
    p.keyUp('ctrl')
    t.sleep(0.3)

    # salvar boletim na pasta adequada
    p.keyDown('ctrl')
    p.hotkey('p')
    p.keyUp('ctrl')
    t.sleep(4)
    p.hotkey('enter')
    t.sleep(3)
    p.keyDown('ctrl')
    p.hotkey('v')
    p.keyUp('ctrl')
    t.sleep(2)
    p.hotkey('enter')
    t.sleep(3)

    # voltando página
    p.moveTo(x=56, y=-840,duration=0.2)
    p.click()
    t.sleep(0.3)

    # voltando para o excel
    p.moveTo(x=316, y=-30,duration=0.2)
    p.click()
    t.sleep(0.3)

    # mudando a célula para próxima matrícula
    p.hotkey('esc')
    t.sleep(0.2)
    p.hotkey('down')
    
    x+=1
