# test_interface_3

def tela_inicio(self):

    self.menu.destroy()
    self.menu = Tk()
    self.menu.title("Monitoramento - Sabrina")
    self.menu.geometry("1060x380+0+0")

    self.voltar = Button(self.menu, text = "Voltar", bg = "#040c31", fg = "white")
    self.voltar["command"] = self.c_menu

    self.f_dias() #Essa função me retorna os dias monitorados
    botao = list()    

    for i in range(len(self.dia)):
        #ao criar o botao o texto dele fica correto
        botao.append(Button(self.menu, text = f"{self.dia[i]}"))
        botao[i].grid()
        #A função grafico recebe o dia como argumento para plotar um grafico com os dados referente ao mesmo       
        botao[i]["command"] = lambda: self.grafico(self.dia[i])

    self.voltar.grid()
    self.menu.mainloop()