def crivo_eratostenes(limite):
    primos = [True] * (limite + 1)
    
    primos[0] = primos[1] = False
    
    # A otimização é ir apenas até a raiz quadrada do limite
    for numero in range(2, int(limite**0.5) + 1):
        # Se o número for True (ainda não foi marcado como composto)
        if primos[numero]:
            # Marca todos os múltiplos desse número como False (composto)
            # Começa do quadrado do número e vai de passo em passo, 
            # onde o passo é o próprio número.
            for multiplo in range(numero*numero, limite + 1, numero):
                primos[multiplo] = False
    
    # Retorna a lista de todos os números primos encontrados
    return [i for i, is_prime in enumerate(primos) if is_prime]

limite_desejado = 100
numeros_primos = crivo_eratostenes(limite_desejado)
print(f"Os números primos até {limite_desejado} são: {numeros_primos}")
