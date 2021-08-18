# planilha-excel-python-xlrd

# from xlrd import open_workbook, cellname

# workbook = open_workbook('Pasta1_teste.xls')
# sheet = workbook.sheet_by_index(0)

# for row_index in range(sheet.nrows):       
#     for col_index in range(sheet.ncols):
    
#     print cellname(row_index,col_index),'-',    
#     print sheet.cell_value(row_index,col_index)

import xlrd
book = xlrd.open_workbook("Pasta1_teste.xls")
print ("Número de abas: ", book.nsheets)
print ("Nomes das Planilhas:", book.sheet_names())
sh = book.sheet_by_index(0)
print(sh.name, sh.nrows, sh.ncols)
print("Valor da célula D1 é ", sh.cell_value(rowx=0, colx=1))
for rx in range(sh.nrows):
    print(sh.row(rx))