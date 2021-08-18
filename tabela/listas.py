# listas
# Exercício Python #089​ - Boletim com listas compostas
# https://www.youtube.com/watch?v=7xrCJnniqMw


import pyautogui as p
import time as t


ficha1 = list()

nome_aluno = str(input('Nome do(a) aluno(a): '))


while True:
    ano1 = int(input('Ano: '))
    resp = str(input('Quer continuar adicionando ANO?[S/N]'))
    if resp in 'Nn':
        break

while True:
    materia1 = str(input('Matéria 1 : '))
    nota1= float(input('nota 1: '))
    ficha1.append([materia1,nota1])

    resp = str(input('Quer continuar adicionando MATÉRIA?[S/N]'))
    if resp in 'Nn':
        break

print(ficha1)

# p.moveTo(x=674, y=747,duration=0.2)
# p.click()
# t.sleep(1)
# p.write(nome_aluno)
# p.hotkey('enter')
# t.sleep(0.1)
# p.write(ano)
# p.hotkey('enter')
# t.sleep(0.1)
# p.write(materia1)
# p.hotkey('enter')
# t.sleep(0.1)
# p.write(nota1)
# p.hotkey('enter')