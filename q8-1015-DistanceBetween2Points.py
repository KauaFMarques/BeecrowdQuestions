linha1 = input().split()
linha2 = input().split()

x1 = float(linha1[0])
y1 = float(linha1[1])
x2 = float(linha2[0])
y2 = float(linha2[1])

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(f"{distancia:.4f}")