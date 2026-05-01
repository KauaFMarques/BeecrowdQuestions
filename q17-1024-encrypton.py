n = int(input())

for _ in range(n):
    linha = input()
    encrypted = []
    
    # Primeira etapa: shift 3 para a direita para letras
    for char in linha:
        if char.isalpha():
            # Desloca 3 posições na ASCII
            encrypted.append(chr(ord(char) + 3))
        else:
            encrypted.append(char)
    
    # Segunda etapa: inverte a string
    encrypted = encrypted[::-1]
    
    # Terceira etapa: shift 1 para a esquerda a partir da metade
    metade = len(encrypted) // 2
    for i in range(metade, len(encrypted)):
        encrypted[i] = chr(ord(encrypted[i]) - 1)
    
    # Converte para string final
    resultado = ''.join(encrypted)
    print(resultado)