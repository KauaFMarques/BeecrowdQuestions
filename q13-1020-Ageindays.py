days = int(input())

# Anos
years = days // 365
days = days % 365  # Dias que sobraram após remover os anos

# Meses (cada mês tem 30 dias)
months = days // 30
days = days % 30   # Dias que sobraram após remover os meses

print(f"{years} ano(s)")
print(f"{months} mes(es)") 
print(f"{days} dia(s)")