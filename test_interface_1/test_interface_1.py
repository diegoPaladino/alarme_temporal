from tkinter import *
from tkinter import messagebox

class MinhaGUI:
 def __init__(self):
  # Criamos a janela principal
  self.janela_principal = Tk()
  
  # Criando o botão
  self.botao_1 = Button(self.janela_principal, text='1º ANO', command=self.hello_world)
  self.botao_2 = Button(self.janela_principal, text='2º ANO', command=self.hello_world)
  
  # Empacotando o botão na janela principal
  self.botao_1.pack()
  self.botao_2.pack()
  
  # Rodando
  mainloop()

  
 def hello_world(self):
  messagebox.showinfo('Adoro a Apostila Python Progressivo!')


gui = MinhaGUI()