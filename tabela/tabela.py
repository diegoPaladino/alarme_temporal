# tabela

# declarando
nome1 = "Paula"
nome2 = "Bianca"
nome3 = "Eloisa"


def criarTabela():
    print("Nome do aluno\t\tNota")
    print("-------------------------------------------")
    print("%s:\t\t\t%f"% (nome1,7.8))
    print("%s:\t\t\t%f"% (nome2,4.5))
    print("%s:\t\t\t%f"% (nome3,9.6))
    print("-------------------------------------------")

criarTabela()