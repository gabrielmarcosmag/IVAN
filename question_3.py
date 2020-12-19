n_alunos = input('Insira o número de alunos: ')
alunos={}
for i in range(int(n_alunos)):
    nome = input(f'\n\nEntre com o nome do aluno {i+1}: ')
    nota = input(f'Entre com a nota de {nome}: ')
    alunos[nome]=float(nota)
    
nota_max = alunos[max(alunos, key=alunos.get)]
print(f'\n\nA maior nota foi de {nota_max} pontos, obtida pelo(s) aluno(s):')
for nome in alunos:
    if(alunos[nome] == nota_max):
        print(nome)