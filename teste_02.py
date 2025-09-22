#Função para apresentar a mensagem REPROVADO
def np():                                                      
    print('='*40)
    print(f'Infelizmente o aluno {nome}, não passou')
    print('='*40)
  
#Função para apresentar a mensagem ARPOVADO
def sp():                                                      
    print('='*40)
    print(f'Parabéns o aluno {nome} passou de ano')
    print('='*40)
#Função que apresenta o resumo do BOLETIM    
def resumo():                                                  
    print(f'A media para ser APROVADO é apartir de 7 (sete)')
    print(f'A media calculada foi: {media:.2f}')
    print(f'O foram feitas {len(boletin)} entradas de notas')
    print(f'O soma das notas informadas é: {sum(boletin):.2f}')
    print('== '*40)

#Declaração de variáveis e listas
boletin=[]
op = 'S'
#===============================================================================
#Programa principal

#Solicitação do nome do aluno
nome = str(input('Informe o nome do aluno: '))

#Laço de reptição já começa com TRUE
while True:
    #Usuário fornece a nota e o valor é guardado na variável NOTA
    nota = float(input('Informe a nota: '))
    #A lista BOLETIN, armazena o valor de nota
    boletin.append(nota)
    #A variável MEDIA calcula a média do aluno com o (SOMA_LISTA / COMPRIMENTO_LISTA)
    media = sum(boletin)/len(boletin)
    #É perguntado ao usuário se deseja adicionar mais uma nota no sistema e a resposta é armazenado em OP
    op = str(input('Deseja adicionar outra nota: [S/N] ')).upper()
    #Por padrão a variável OP já armazena S
    
    #Condição se o usuário digitar NÃO
    if op == 'N':
        #Ponto de saída do laço.
        break
    #Laço de repetição se o usuário digitar qualquer coisa diferente de S ou N.
    while op != 'S' and op != 'N':
        #Mensagem de erro
        op = str(input('Opção inválida, utilize S = SIM ou N = NÃO ')).upper()
#Condição SE caso a média (função NP) for menor do que 7 (sete)
if media < 7:
    #Chamada de duas funções NP e RESUMO
    np()
    resumo()
#Condição OUTRO caso a média (função SP) for maior do que 7 (sete)
else:
    #Chamada de duas funções SP e RESUMO
    sp()
    resumo()