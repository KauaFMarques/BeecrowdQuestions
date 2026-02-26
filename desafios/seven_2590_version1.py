def ultimo_digito_7n(n):
    resto = n % 4
    
    if resto == 1:
        return 7
    elif resto == 2:
        return 9
    elif resto == 3:
        return 3
    else:
        return 1

t = int(input())
for _ in range(t):
    n = int(input())
    resultado = ultimo_digito_7n(n)
    print(resultado)