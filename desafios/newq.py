def verificadorPrimo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

while True:
    try:
        numero = int(input())
        numero_str = str(numero)
        
        # Verifica se é primo
        primo = verificadorPrimo(numero)
        
        # Verifica se todos os dígitos são primos
        digitos_primos = True
        for digito in numero_str:
            if digito not in ['2', '3', '5', '7']:
                digitos_primos = False
                break
        
        if primo and digitos_primos:
            print("Super")
        elif primo:
            print("Primo")
        else:
            print("Nada")
            
    except EOFError:
        break