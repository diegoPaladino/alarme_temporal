#CÓDIGO DA INTERFACE
from tkinter import *

janela = Tk()
janela.title("Move&Renomeia")
janela["bg"] = "wheat"
janela.geometry('500x450+800+100')



#título da interface
rotulo = Label(janela,
               font="Arial 16 bold",
               text='Programa Move e Renomeia Arquivos',
               bg="wheat")
rotulo.pack(side=TOP)

#rótulo da caixa de texto, campo endereço de origem
rotulo = Label(janela,
               font="Arial 12 bold",
               text='Pasta origem:',
               bg="wheat")
rotulo.place(x=10, y=100)

#rótulo da caixa de texto, campo endereço de destino
rotulo = Label(janela,
               font="Arial 12 bold",
               text='Pasta destino:',
               bg="wheat")
rotulo.place(x=10, y=150)

#Caixa de texto para colocar o caminho de origem
cxtexto1 = Entry(janela,
                 width=40,
                 font="Arial 12 bold")
cxtexto1.place(x=125, y=100)

#Caixa de texto para colocar o caminho de destino
cxtexto2 = Entry(janela,
                 width=40,
                 font="Arial 12 bold")
cxtexto2.place(x=125, y=150)

#Texto de orientação ao usuário
rotulo = Label(janela,
               font="Arial 10",
               text=' Como fazer:\n'
                    ' 1) Crie duas pastas:\n'
                    '    a) na primeira, coloque os arquivos a serem renomeados; \n'
                    '    b) na segunda, crie um arquivo no bloco de notas e coloque os nomes; \n'
                    ' 2) copie o endereço das pastas e cole no campo respectivo; \n'
                    ' 3) INVERTA as barras do endereço e acrescente uma barra no final; ',
               justify=LEFT,
               bd=2,
               relief=GROOVE,
               bg="wheat")
rotulo.place(x=50, y=200)


#botão para renomear o arquivo
bt1 = Button(janela,
             width=10,
             text="Renomear",
             font="Arial 12 bold",
             command='AQUI VAI ENTRAR A CHAMADA A FUNÇÃO')
bt1.place(x=200, y=310)



janela.mainloop()