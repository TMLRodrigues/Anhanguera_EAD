soma = cont = nota = media = 0
nome = ''
boletim = []
op = 'S'

nome = str(input('Informe o nome do aluno: '))

while op == 'S':
  nota = int(input(f'Insira a nota do aluno {nome}: '))
  boletim.append(nota)
  tl = len(boletim)
  op = str(input('Você deseja inserir mais notas?[S/N]: ')).upper()
while nota < 0:
  #if nota < 0:
    for c in range(tl):
      nota = float(input(f'Insira a nota {c} do aluno: '))
      boletim.append(nota)
      soma = sum(boletim)
      tl = len(boletim)
#      media = soma/len(boletim)
    if op == 'N':
      break

print(f"""
O aluno {nome} possui as seguintes notas:
Media: {media}
Comprimento: {len(boletim)}
Lista boletim: {boletim}
Soma Boletim: {soma}
""")