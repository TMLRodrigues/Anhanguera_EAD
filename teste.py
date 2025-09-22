boletim = []
op = 'S'


nome = str(input('Informe o nome do aluno: ')).upper()
nota=int(input(f'Insira a nota do aluno {nome}: '))
boletim.append(nota)
soma = sum(boletim)
media = sum(boletim)/len(boletim)
op = str(input('Deseja incluir mais notas? [S/N]: ')).upper()
if op == 'N':
    print(f'A soma das notas do aluno {nome}: \nA media foi: {media}\nO bolerim é: {boletim}\nTamanho da lista boletim: {len(boletim)}')

while op == 'S':
    while nota > 1:
        for c in range(len(boletim)):
            nota=int(input(f'Insira a nota do alUno {nome}: '))
            boletim.append(nota)
            soma = sum(boletim)
            media = soma/len(boletim)
            op = str(input(f'Deseja informar mais notas? [S/N]: ' )).upper()
        if op == 'N':
            break

print(f'A soma das notas do aluno {nome}; \nA media foi: {media}\nO bolerim é: {boletim}\nTamanho da lista boletim: {len(boletim)}')
