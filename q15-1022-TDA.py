def mdc(a, b):
    """Calcula o Máximo Divisor Comum"""
    while b:
        a, b = b, a % b
    return a

def simplificar(numerador, denominador):
    """Simplifica uma fração"""
    # Garante que o denominador seja positivo
    if denominador < 0:
        numerador = -numerador
        denominador = -denominador
    
    divisor = mdc(abs(numerador), abs(denominador))
    return numerador // divisor, denominador // divisor

# Número de casos de teste
N = int(input())

for _ in range(N):
    # Lê a expressão completa
    n1, _, d1, op, n2, _, d2 = input().split()
    
    # Converte para inteiros
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)
    
    # Calcula conforme a operação
    if op == '+':
        num = n1 * d2 + n2 * d1
        den = d1 * d2
    elif op == '-':
        num = n1 * d2 - n2 * d1
        den = d1 * d2
    elif op == '*':
        num = n1 * n2
        den = d1 * d2
    elif op == '/':
        num = n1 * d2
        den = n2 * d1
    
    # Resultado original
    resultado_original = f"{num}/{den}"
    
    # Resultado simplificado
    num_simplificado, den_simplificado = simplificar(num, den)
    resultado_simplificado = f"{num_simplificado}/{den_simplificado}"
    
    print(f"{resultado_original} = {resultado_simplificado}")