from math import log 
import numpy as np

def fatorial(a):
    res = 1 
    for i in range(1,a+1):
        res *= i
    return(res)
        
#%% Questao 2 
x = np.arange(10.0)
        
for i in range(len(x)):
    if(i%2==0):
        x[i] = (3.0**i+7.0*fatorial(i))
    else:
        x[i] = (2.0**i+4.0*log(i))

print(f'O maior valor do vetor está na posição {np.argmax(x)}')
print(f'A média dos elementos do vetor é {x.mean():.2f}')