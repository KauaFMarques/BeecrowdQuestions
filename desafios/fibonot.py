# 1 1 -> 1 1 2->
# (1+1=2)       (2-1=1) ->

"""n1,n2= 1,1

for i in range(0,20):
    temp=n1
    n2=n1+n2
    n1=temp

    if n2-n1>1:
        for j in range(n1+1,n2):
            print(i)
"""

"""
k = int(input("Digite um número k: "))

def fibonacci_iterativo(n):
    sequencia = []
    a, b = 0, 1
    while len(sequencia) < n:
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

# Gera números de Fibonacci suficientes
fibonacci = fibonacci_iterativo(k + 1000)
fibonacci_set = set(fibonacci)

def find_kth_fibonot(k):
    fibonot = []
    n = 1
    while len(fibonot) < k:
        if n not in fibonacci_set:
            fibonot.append(n)
        n += 1
    return fibonot[k-1]  # Retorna o K-ésimo elemento

resultado = find_kth_fibonot(k)
print(resultado)
"""

"""
k = int(input())

def find_kth_fibonot(k):
    fib = [0, 1]
    fibonot = []
    n = 1
    
    while len(fibonot) < k:
        if n == fib[-1]:
            next_fib = fib[-1] + fib[-2]
            fib.append(next_fib)
        else:
            fibonot.append(n)
        n += 1
    
    return fibonot[k-1]

print(find_kth_fibonot(k))
"""
k = int(input())

def find_kth_fibonot(k):
    fib = [0, 1, 1]
    fibonot = []
    current = 1
    
    while len(fibonot) < k:
        if current == fib[-1]:
            # Se é Fibonacci, calcula o próximo
            next_fib = fib[-1] + fib[-2]
            fib.append(next_fib)
        else:
            # Se não é Fibonacci, adiciona à lista
            fibonot.append(current)
        current += 1
    
    return fibonot[k-1]

print(find_kth_fibonot(k))