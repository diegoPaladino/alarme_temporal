# test-format_string-historico-tentativa_1
# source: https://stackoverflow.com/questions/53908134/what-is-20-format-string-meaning-in-python
# adaptado para os primórdios da confecção do histórico com Python.


# ANO 1
ano1 = int(input('Ano 1: '))
escola1 = (str(input('Escola que estudou em ' +str(ano1)+': ')))
if escola1 == "ESCOLA MUNICIPAL FRANCISCO RAFAEL CAMPOS":
    cidade1 = "APARECIDA DE GOIÂNIA"
    uf1 = 'GO'
    
else:
    cidade1 = str(input('Municipio da escola que estudou em ' +str(ano1)+ ': '))
    uf1 = str(input('UF da escola que estudou em: ' +str(ano1)+': '))
    
# ANO 2
pergunta1 = str(input('Ano subsequente e mesma escola no ano seguinte a ' +str(ano1)+ '? [S/N]: '))
if pergunta1 in 'Ss':
	ano2 = ano1+1
	escola2 = escola1
	cidade2 = cidade1
	uf2 = uf1
	
else:
    #  pergunta1 in 'Nn':
	pergunta1a = str(input('1. Ano seguinte nao subsequencial e mesma escola; \n2. Ano seguinte nao subsequencial e escola diferente\n \n[1/2]: '))
	if pergunta1a in '1':
		ano2 = int(input('Ano 2: '))
		escola2 = escola1
		cidade2 = cidade1
		uf2 = uf1
	if pergunta1a in '2':
		ano2 = int(input('Ano 2: '))
		escola2 = str(input('Escola que estudou em ' +str(ano2)+ ': '))
		pergunta1b = str(input('Mesmo municipio anterior? [S/N]: '))
		if pergunta1b in 'Ss':
			cidade2 = cidade1
			uf2 = uf1
		else:
			cidade2 = str(input('Municipio da escola que estudou em ' +str(ano2)+ ': '))
			uf2 = str(input('UF da escola que estudou em: ' +str(ano1)+': '))


# ANO 3
pergunta2 = str(input('Ano subsequente e mesma escola no ano seguinte a ' +str(ano2)+ '? [S/N]: '))
if pergunta2 in 'Ss':
	ano3 = ano2+1
	escola3 = escola2
	cidade3 = cidade2
	uf3 = uf2
 
else:
	pergunta2a = str(input('1. Ano seguinte nao subsequencial e mesma escola; \n2. Ano seguinte nao subsequencial e escola diferente\n \n[1/2]: '))
	if pergunta2a in '1':
		ano3 = int(input('Ano 3: '))
		escola3 = escola2
		cidade3 = cidade2
		uf3 = uf2
	if pergunta2a in '2':
		ano3 = int(input('Ano 3: '))
		escola3 = str(input('Escola que estudou em ' +str(ano3)+ ': '))
		pergunta2b = str(input('Mesmo municipio anterior? [S/N]: '))
		if pergunta2b in 'Ss':
			cidade3 = cidade2
			uf3 = uf1
		else:
			cidade3 = str(input('Municipio da escola que estudou em ' +str(ano2)+ ': '))
			uf3 = str(input('UF da escola que estudou em: ' +str(ano1)+': '))
   

# ANO 4
pergunta3 = str(input('Ano subsequente e mesma escola no ano seguinte a ' +str(ano3)+ '? [S/N]: '))
if pergunta3 in 'Ss':
    ano4 = ano3+1
    escola4 = escola3
    cidade4 = cidade3
    uf4 = uf3
    
else:
    pergunta3a = str(input('1. Ano seguinte nao subsequencial e mesma escola; \n2. Ano seguinte nao subsequencial e escola diferente\n \n[1/2]: '))
    if pergunta3a in '1':
        ano4 = int(input('Ano 4: '))
        escola4 = escola3
        cidade4 = cidade3
        uf4 = uf3
    if pergunta3a in '2':
        ano4 = int(input('Ano 4: '))
        escola4 = str(input('Escola que estudou em ' +str(ano4)+ ': '))
        pergunta3b = str(input('Mesmo municipio anterior? [S/N]: '))
        if pergunta3b in 'Ss':
            cidade4 = cidade3
            uf4 = uf1
        else:
            cidade4 = str(input('Municipio da escola que estudou em ' +str(ano3)+ ': '))
            uf4 = str(input('UF da escola que estudou em: ' +str(ano1)+': '))


# ANO 5
pergunta4 = str(input('Ano subsequente e mesma escola no ano seguinte a ' +str(ano4)+ '? [S/N]: '))
if pergunta4 in 'Ss':
    ano5 = ano4+1
    escola5 = escola4
    cidade5 = cidade4
    uf5 = uf4
    
else:
    pergunta4a = str(input('1. Ano seguinte nao subsequencial e mesma escola; \n2. Ano seguinte nao subsequencial e escola diferente\n \n[1/2]: '))
    if pergunta4a in '1':
        ano5 = int(input('Ano 5: '))
        escola5 = escola4
        cidade5 = cidade4
        uf5 = uf4
    if pergunta4a in '2':
        ano5 = int(input('Ano 5: '))
        escola5 = str(input('Escola que estudou em ' +str(ano5)+ ': '))
        pergunta4b = str(input('Mesmo municipio anterior? [S/N]: '))
        if pergunta4b in 'Ss':
            cidade5 = cidade4
            uf5 = uf1
        else:
            cidade5 = str(input('Municipio da escola que estudou em ' +str(ano4)+ ': '))
            uf5 = str(input('UF da escola que estudou em: ' +str(ano1)+': '))


# ANO 6
pergunta5 = str(input('Ano subsequente e mesma escola no ano seguinte a ' +str(ano5)+ '? [S/N]: '))
if pergunta5 in 'Ss':
    ano6 = ano5+1
    escola6 = escola5
    cidade6 = cidade5
    uf6 = uf5
    
else:
    pergunta5a = str(input('1. Ano seguinte nao subsequencial e mesma escola; \n2. Ano seguinte nao subsequencial e escola diferente\n \n[1/2]: '))
    if pergunta5a in '1':
        ano6 = int(input('Ano 6: '))
        escola6 = escola5
        cidade6 = cidade5
        uf6 = uf5
    if pergunta5a in '2':
        ano6 = int(input('Ano 6: '))
        escola6 = str(input('Escola que estudou em ' +str(ano6)+ ': '))
        pergunta5b = str(input('Mesmo municipio anterior? [S/N]: '))
        if pergunta5b in 'Ss':
            cidade6 = cidade5
            uf6 = uf1
        else:
            cidade6 = str(input('Municipio da escola que estudou em ' +str(ano5)+ ': '))
            uf6 = str(input('UF da escola que estudou em: ' +str(ano1)+': '))


# ANO 7
pergunta6 = str(input('Ano subsequente e mesma escola no ano seguinte a ' +str(ano6)+ '? [S/N]: '))
if pergunta6 in 'Ss':
    ano7 = ano6+1
    escola7 = escola6
    cidade7 = cidade6
    uf7 = uf6
    
else:
    pergunta6a = str(input('1. Ano seguinte nao subsequencial e mesma escola; \n2. Ano seguinte nao subsequencial e escola diferente\n \n[1/2]: '))
    if pergunta6a in '1':
        ano7 = int(input('Ano 7: '))
        escola7 = escola6
        cidade7 = cidade6
        uf7 = uf6
    if pergunta6a in '2':
        ano7 = int(input('Ano 7: '))
        escola7 = str(input('Escola que estudou em ' +str(ano7)+ ': '))
        pergunta6b = str(input('Mesmo municipio anterior? [S/N]: '))
        if pergunta6b in 'Ss':
            cidade7 = cidade6
            uf7 = uf1
        else:
            cidade7 = str(input('Municipio da escola que estudou em ' +str(ano5)+ ': '))
            uf7 = str(input('UF da escola que estudou em: ' +str(ano1)+': '))

    
            
# ANO 8
pergunta6 = str(input('Ano subsequente e mesma escola no ano seguinte a ' +str(ano7)+ '? [S/N]: '))
if pergunta6 in 'Ss':
    ano8 = ano7+1
    escola8 = escola7
    cidade8 = cidade7
    uf8 = uf7
    
else:
    pergunta6a = str(input('1. Ano seguinte nao subsequencial e mesma escola; \n2. Ano seguinte nao subsequencial e escola diferente\n \n[1/2]: '))
    if pergunta6a in '1':
        ano8 = int(input('Ano 8: '))
        escola8 = escola7
        cidade8 = cidade7
        uf8 = uf7
    if pergunta6a in '2':
        ano8 = int(input('Ano 8: '))
        escola8 = str(input('Escola que estudou em ' +str(ano8)+ ': '))
        pergunta6b = str(input('Mesmo municipio anterior? [S/N]: '))
        if pergunta6b in 'Ss':
            cidade8 = cidade7
            uf8 = uf1
        else:
            cidade8 = str(input('Municipio da escola que estudou em ' +str(ano5)+ ': '))
            uf8 = str(input('UF da escola que estudou em: ' +str(ano1)+': '))


# ANO 9
pergunta6 = str(input('Ano subsequente e mesma escola no ano seguinte a ' +str(ano8)+ '? [S/N]: '))
if pergunta6 in 'Ss':
    ano9 = ano8+1
    escola9 = escola8
    cidade9 = cidade8
    uf9 = uf8
    
else:
    pergunta6a = str(input('1. Ano seguinte nao subsequencial e mesma escola; \n2. Ano seguinte nao subsequencial e escola diferente\n \n[1/2]: '))
    if pergunta6a in '1':
        ano9 = int(input('Ano 9: '))
        escola9 = escola8
        cidade9 = cidade8
        uf9 = uf8
    if pergunta6a in '2':
        ano9 = int(input('Ano 9: '))
        escola9 = str(input('Escola que estudou em ' +str(ano9)+ ': '))
        pergunta6b = str(input('Mesmo municipio anterior? [S/N]: '))
        if pergunta6b in 'Ss':
            cidade9 = cidade8
            uf9 = uf1
        else:
            cidade9 = str(input('Municipio da escola que estudou em ' +str(ano5)+ ': '))
            uf9 = str(input('UF da escola que estudou em: ' +str(ano1)+': '))


            

escolas = [[ano1, escola1, cidade1, uf1],[ano2, escola2, cidade2, uf2],[ano3, escola3, cidade3, uf3],[ano4, escola4, cidade4, uf4],
           [ano5, escola5, cidade5, uf5],[ano6, escola6, cidade6, uf6],[ano7, escola7, cidade7, uf7],[ano8, escola8, cidade8, uf8],
           [ano9, escola9, cidade9, uf9]]
format_string = "{:<6} {:<50} {:<30} {:<4} "

# imprimindo a relação de escolas que estudou (na respectiva ordem: ano, escola, município e uf):
for l in escolas: print(format_string.format(*l))

# finaliza aqui a parte de alimentar o programa com os dados de ano, nome da escola, município, e uf.


historico = [['Ano', ano1, ano2, ano3, ano4, ano5, ano6, ano7, ano8, ano9],
['Artes', 1, 2, 3, 4, 5, 6, 7, 8, 9],
['Ciências', 1, 2, 3, 4, 5, 6, 7, 8, 9],
['Educação Física', 1, 2, 3, 4, 5, 6, 7, 8, 9],
['Ensino Religioso', 1, 2, 3, 4, 5, 6, 7, 8, 9],
['Geografia', 1, 2, 3, 4, 5, 6, 7, 8, 9],
['História', 1, 2, 3, 4, 5, 6, 7, 8, 9],
['Língua Portuguesa', 1, 2, 3, 4, 5, 6, 7, 8, 9],
['Matemática', 1, 2, 3, 4, 5, 6, 7, 8, 9]]

format_string = "{:<20}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}"







# Imprimindo as notas (anos, matérias e notas):
for l in historico: print(format_string.format(*l))

