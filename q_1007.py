#(A * B - C * D)
a=int(input())
b=int(input())
c=int(input())
d=int(input())

def calcular_diferenca(a, b, c, d):
    diferenca=(a*b)-(c*d)
    return diferenca

calc=calcular_diferenca(a,b,c,d)
print(f"DIFERENCA = {calc}")