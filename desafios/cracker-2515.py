'''
# Exemplo de soma de prefixos em Python

# Vetor original
v = [2, 5, 7, 3, 4]

# Construindo o vetor de prefixos
n = len(v)
prefix = [0] * (n + 1)   # prefix[0] = 0 para facilitar cálculos

for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + v[i-1]

print("Vetor original:", v)
print("Somas de prefixo:", prefix)

# Função para responder soma em intervalo [l, r]
def soma_intervalo(l, r):
    return prefix[r] - prefix[l-1]


# Exemplos de consultas
print("Soma de v[2..4] =", soma_intervalo(2, 4))  # 5 + 7 + 3 = 15
print("Soma de v[1..5] =", soma_intervalo(1, 5))  # 2 + 5 + 7 + 3 + 4 = 21
print("Soma de v[3..3] =", soma_intervalo(3, 3))  # apenas 7


#teoria dos jogos -> equilíbrio de john nash

import numpy as np

# 1. Defina as matrizes de payoff para o Jogador A (linhas) e Jogador B (colunas)
#    Exemplo: Dilema do Prisioneiro (Cooperar=0, Trair=1)
#    Payoffs: (A, B)
A = np.array([[3, 0],   # Se A coopera: (3 se B coopera, 0 se B trai)
              [5, 1]])  # Se A trai:   (5 se B coopera, 1 se B trai)

B = np.array([[3, 5],   # Se B coopera: (3 se A coopera, 5 se A trai)
              [0, 1]])  # Se B trai:   (0 se A coopera, 1 se A trai)

# O restante do código (encontrar as estratégias) seria executado pelo script do repositório.
# O resultado esperado para este jogo é que ambos traiam: estratégia pura (0, 1) para A.



#resolução

#Corte 1: (3) | (1, 2, 3, 2) $\rightarrow$ Lados: 3 e 8. Leonardo pega 8, Marcos pega 3.
# Corte 2: (3, 1) | (2, 3, 2) $\rightarrow$ Lados: 4 e 7. Leonardo pega 7, Marcos pega 4.
# Corte 3: (3, 1, 2) | (3, 2) $\rightarrow$ Lados: 6 e 5. Leonardo pega 6, Marcos pega 5.
# Corte 4: (3, 1, 2, 3) | (2) $\rightarrow$ Lados: 9 e 2. Leonardo pega 9, Marcos pega 2.
'''
import sys

entrada = sys.stdin.read().split()

pos = 0

while pos < len(entrada):
    n = int(entrada[pos])
    pos += 1
    
    biscoitos = list(map(int, entrada[pos : pos + n]))
    pos += n
    
    soma_total = sum(biscoitos)

    soma_esquerda = 0
    melhor_marcos=0

    # 2. Loop para testar os cortes e achar o 'melhor_marcos' //soma de prefixo
    for i in range(n - 1):
        soma_esquerda += biscoitos[i]
        soma_direita = soma_total - soma_esquerda
        
        # Em cada corte, o Marcos fica com o menor pedaço
        ganho_atual_marcos = min(soma_esquerda, soma_direita)
            
        # Se esse ganho for melhor que o recorde anterior, atualizamos
        if ganho_atual_marcos > melhor_marcos:
            melhor_marcos = ganho_atual_marcos

    print(f"{melhor_marcos} {soma_total - melhor_marcos}")
