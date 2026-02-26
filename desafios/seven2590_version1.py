n = int(input())
resultado = pow(7, n)

resto=n%4

def case_de_potencias(resto):
    elif resto==1:
        return 7
    elif resto==2:
        return 9
    elif resto==3:
        return 3
    elif resto==0:
        return 1