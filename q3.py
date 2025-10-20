def factorial(n):
    """Calcula o fatorial de um número"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("=== CALCULADORA DE SOMA DE FATORIAIS ===")
print("Instruções:")
print("- Digite dois números separados por espaço (ex: '4 4')")
print("- Digite 'sair' para encerrar o programa")
print("- Valores válidos: 0 ≤ M ≤ 20 e 0 ≤ N ≤ 20")
print("=" * 50)

while True:
    try:
        entrada = input("\nDigite M e N: ").strip()
        
        # Verifica se o usuário quer sair
        if entrada.lower() == 'sair':
            print("Programa encerrado. Até mais!")
            break
            
        # Verifica se a entrada está vazia
        if not entrada:
            print("Erro: Digite dois números separados por espaço")
            continue
            
        # Divide a entrada e verifica se tem dois valores
        data = entrada.split()
        if len(data) != 2:
            print("Erro: Digite exatamente dois números separados por espaço")
            continue
            
        # Converte para inteiro e verifica intervalo
        try:
            M = int(data[0])
            N = int(data[1])
        except ValueError:
            print("Erro: Certifique-se de digitar apenas números inteiros")
            continue
            
        if M < 0 or M > 20 or N < 0 or N > 20:
            print("Erro: Os números devem estar entre 0 e 20")
            continue
            
        # Calcula os fatoriais
        fact_M = factorial(M)
        fact_N = factorial(N)
        result = fact_M + fact_N
        
        # Exibe o resultado com detalhes
        print(f"\n→ {M}! = {fact_M}")
        print(f"→ {N}! = {fact_N}")
        print(f"→ SOMA: {fact_M} + {fact_N} = {result}")
        
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário. Até mais!")
        break
    except Exception as e:
        print(f"Erro inesperado: {e}")