def gray_to_binary(gray):
    """Converte Gray code para binário (LSB first)"""
    binary = [gray[0]]
    for i in range(1, len(gray)):
        binary.append(binary[i-1] ^ gray[i])
    return binary

def binary_to_gray(binary):
    """Converte binário para Gray code (LSB first)"""
    gray = [binary[0]]
    for i in range(1, len(binary)):
        gray.append(binary[i-1] ^ binary[i])
    return gray

def solve():
    n = int(input().strip())
    for _ in range(n):
        data = input().strip().split()
        P = data[0]
        C = int(data[1])
        
        # Converter string para lista de bits (LSB first)
        # X=0, O=1, primeira lâmpada = LSB
        gray_bits = [1 if ch == 'O' else 0 for ch in P]
        
        # Converter Gray para binário
        binary_bits = gray_to_binary(gray_bits)
        
        # Converter lista de bits para número inteiro (LSB first)
        num = 0
        for i, bit in enumerate(binary_bits):
            num |= (bit << i)
        
        # Somar C
        num = (num + C) % (1 << len(P))
        
        # Converter número de volta para lista de bits (LSB first)
        new_binary = []
        for i in range(len(P)):
            new_binary.append((num >> i) & 1)
        
        # Converter binário para Gray
        new_gray = binary_to_gray(new_binary)
        
        # Converter bits de volta para string
        result = ''.join('O' if bit else 'X' for bit in new_gray)
        
        print(result)

if __name__ == "__main__":
    solve()