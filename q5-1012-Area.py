valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])


trianguleArea = (A * C) / 2

pi = 3.14159
circleArea = pi * (C ** 2)

trapeziumArea = ((A + B) * C) / 2

squareArea = B * B

retangleArea = A * B

print(f"TRIANGULO: {trianguleArea:.3f}")
print(f"CIRCULO: {circleArea:.3f}")
print(f"TRAPEZIO: {trapeziumArea:.3f}")
print(f"QUADRADO: {squareArea:.3f}")
print(f"RETANGULO: {retangleArea:.3f}")