import sys

def main():
    primeira_linha = sys.stdin.readline()
    if not primeira_linha:
        return
    
    t = int(primeira_linha.strip())
    
    for _ in range(t):
        linha = sys.stdin.readline()
        if not linha:
            break
            
        n = int(linha.strip())
        
        resto = n % 4
        
        if resto == 1:
            sys.stdout.write('7\n')
        elif resto == 2:
            sys.stdout.write('9\n')
        elif resto == 3:
            sys.stdout.write('3\n')
        else:
            sys.stdout.write('1\n')

if __name__ == "__main__":
    main()