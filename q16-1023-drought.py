def main():
    cidade_num = 0
    
    while True:
        n = int(input())
        if n == 0:
            break
            
        cidade_num += 1
        if cidade_num > 1:
            print()
        
        total_pessoas = 0
        total_consumo = 0
        consumos = {}
        
        # Processa cada propriedade
        for _ in range(n):
            x, y = map(int, input().split())
            consumo_por_pessoa = y // x  # Arredonda para baixo
            
            # Agrupa por consumo por pessoa
            if consumo_por_pessoa in consumos:
                consumos[consumo_por_pessoa] += x
            else:
                consumos[consumo_por_pessoa] = x
                
            total_pessoas += x
            total_consumo += y
        
        # Ordena por consumo por pessoa
        consumos_ordenados = sorted(consumos.items())
        
        # Formata a saída
        resultado = []
        for consumo, pessoas in consumos_ordenados:
            resultado.append(f"{pessoas}-{consumo}")
        
        print(f"Cidade# {cidade_num}:")
        print(" ".join(resultado))
        
        # Calcula consumo médio (com 2 casas decimais)
        consumo_medio = total_consumo / total_pessoas
        print(f"Consumo medio: {consumo_medio:.2f} m3.")

if __name__ == "__main__":
    main()