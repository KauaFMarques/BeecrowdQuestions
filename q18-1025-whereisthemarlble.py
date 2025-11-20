case_num = 0

while True:
    n, q = map(int, input().split())
    
    # Condição de parada
    if n == 0 and q == 0:
        break
    
    case_num += 1
    marbles = []
    
    # Lê os números dos mármores
    for _ in range(n):
        marbles.append(int(input()))
    
    # Ordena os mármores
    marbles.sort()
    
    print(f"CASE# {case_num}:")
    
    # Processa cada consulta
    for _ in range(q):
        x = int(input())
        
        # Busca binária para encontrar a primeira ocorrência
        left, right = 0, n - 1
        position = -1
        
        while left <= right:
            mid = (left + right) // 2
            if marbles[mid] == x:
                position = mid
                right = mid - 1  # Continua buscando à esquerda
            elif marbles[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        
        if position != -1:
            print(f"{x} found at {position + 1}")  # +1 porque posições começam em 1
        else:
            print(f"{x} not found")