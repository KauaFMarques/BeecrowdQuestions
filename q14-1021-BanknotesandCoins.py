valor = float(input())

print("NOTAS:")
notas = [100, 50, 20, 10, 5, 2]

for nota in notas:
    quantidade = int(valor // nota)
    valor = valor % nota
    print(f"{quantidade} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

for moeda in moedas:
    quantidade = int(valor / moeda + 0.0001)  # Pequena correção para arredondamento
    valor = valor % moeda
    print(f"{quantidade} moeda(s) de R$ {moeda:.2f}")