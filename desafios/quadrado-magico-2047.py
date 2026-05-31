n = int(input())

matriz = []
todos_numeros = set()

for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)
    for num in linha:
        todos_numeros.add(num)

e_magico = True

if len(todos_numeros) != n * n or min(todos_numeros) != 1 or max(todos_numeros) != n * n:
    e_magico = False

if e_magico:
    soma_referencia = sum(matriz[0])

    for i in range(n):
        if sum(matriz[i]) != soma_referencia:
            e_magico = False
            break

    if e_magico:
        for j in range(n):
            soma_coluna = 0
            for i in range(n):
                soma_coluna += matriz[i][j]
            if soma_coluna != soma_referencia:
                e_magico = False
                break

    if e_magico:
        soma_diagonal_principal = 0
        for i in range(n):
            soma_diagonal_principal += matriz[i][i]
        if soma_diagonal_principal != soma_referencia:
            e_magico = False

    if e_magico:
        soma_diagonal_secundaria = 0
        for i in range(n):
            soma_diagonal_secundaria += matriz[i][n-1-i]
        if soma_diagonal_secundaria != soma_referencia:
            e_magico = False

if e_magico:
    print(soma_referencia)
else:
    print(0)