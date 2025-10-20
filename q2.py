def factorial(n):
    """Calcula o fatorial de um número"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

while True:
    try:
        data = input().split()
        if not data:
            continue
            
        M = int(data[0])
        N = int(data[1])
        
        fact_M = factorial(M)
        fact_N = factorial(N)
        
        result = fact_M + fact_N
        print(result)
        
    except EOFError:
        break