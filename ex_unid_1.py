soma = cont = nota_1 = media = 0
nome = ''
boletim = []
op = 'S'

nome = str(input('Informe o nome do aluno: '))

while op == 'S':
  nota_1 = int(input(f'Insira a nota do aluno {nome}: '))
  boletim.append(nota_1)
  op = str(input('Você deseja inserir mais notas?[S/N]: ')).upper()
while nota_1 < 0:
  if nota_1 < 0:
    for c in len(boletim):
      nota_1 = float(input(f'Insira a nota {c} do aluno: '))
      boletim.append(nota_1)
      #soma = nota_1
      soma =
      media = soma/len(boletim)
    if op == 'N':
      break

print(f"""
O aluno {nome} possui as seguintes notas:
Media: {media}
Comprimento: {len(boletim)}
""")
