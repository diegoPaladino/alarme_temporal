# pandas-excel
# Python Pandas #1 - Lendo os dados do Excel
# fonte: https://www.youtube.com/watch?v=rQUYpJvMgn8

import pandas as pd

x = pd.read_excel(r"C:/Users/diego/OneDrive/Desktop/teste-leitura-excel-python/JA211-201830050-GERALD_LEVI_DE_LIMA_SANTOS.xls")

print(x['Nome do(a) aluno(a):'][1])