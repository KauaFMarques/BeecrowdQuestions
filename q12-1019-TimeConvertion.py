time = int(input())

hours = time // 3600
time = time % 3600  # O que sobrou após remover as horas

minutes = time // 60
seconds = time % 60   # O que sobrou após remover os minutos

print(f"{hours}:{minutes}:{seconds}")