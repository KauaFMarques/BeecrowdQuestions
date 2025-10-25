a=float(input())
b=float(input())
c=float(input())

def calcular_media(a, b, c):
    media_total=((a*2)+(b*3)+(c*5))/(2+3+5)
    return media_total

calc=calcular_media(a,b,c)
print(f"MEDIA = {calc:.1f}")