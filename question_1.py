#%% Questao 1
cont = 0
lim_sup = 5000000

for i in range(1,lim_sup+1):
    if(i%2==0 and i%37==0 and i%49==0):
        cont += 1

print(f'Existem {cont} que sao pares e, ao mesmo tempo, multiplos de 37 e 49 entre 1 e {lim_sup}')