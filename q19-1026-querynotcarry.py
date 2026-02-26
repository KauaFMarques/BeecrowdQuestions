while True:
    try:
        a, b = map(int, input().split())
        resultado = a ^ b  # Operação XOR
        print(resultado)
    except EOFError:
        break