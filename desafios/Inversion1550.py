from collections import deque

def inverter_numero(n):
    """Inverte os dígitos e remove zeros à esquerda"""
    return int(str(n)[::-1])

def minimo_pressionamentos(A, B):
    # Conjunto para números já visitados
    visitados = set()
    # Fila para BFS
    fila = deque()
    
    # Começa com o número inicial e 0 pressionamentos
    fila.append((A, 0))
    visitados.add(A)
    
    while fila:
        atual, pressionamentos = fila.popleft()
        
        # Se chegou em B, retorna o número de pressionamentos
        if atual == B:
            return pressionamentos
        
        # Operação 1: Adicionar 1
        proximo1 = atual + 1
        if proximo1 not in visitados and proximo1 <= 10000:
            visitados.add(proximo1)
            fila.append((proximo1, pressionamentos + 1))
        
        # Operação 2: Inverter dígitos
        proximo2 = inverter_numero(atual)
        if proximo2 not in visitados and proximo2 <= 10000:
            visitados.add(proximo2)
            fila.append((proximo2, pressionamentos + 1))
    
    return -1  # Nunca deve acontecer dado os limites

def main():
    t = int(input())
    for _ in range(t):
        A, B = map(int, input().split())
        print(minimo_pressionamentos(A, B))

if __name__ == "__main__":
    main()