valor = int(input())

print(valor)

# Notas disponíveis em ordem decrescente
notas = [100, 50, 20, 10, 5, 2, 1]

valor_restante = valor

for nota in notas:
    quantidade = valor_restante // nota  # Divisão inteira
    valor_restante = valor_restante % nota  # Resto da divisão
    
    print(f"{quantidade} nota(s) de R$ {nota},00")