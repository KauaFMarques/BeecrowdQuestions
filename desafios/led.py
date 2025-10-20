def gray_to_binary(gray):
    """Converte Gray code para binário (MSB first)"""
    binary = [gray[0]]
    for i in range(1, len(gray)):
        binary.append(binary[i - 1] ^ gray[i])
    return binary

def binary_to_gray(binary):
    """Converte binário para Gray code (MSB first)"""
    gray = [binary[0]]
    for i in range(1, len(binary)):
        gray.append(binary[i - 1] ^ binary[i])
    return gray

def solve():
    n = int(input().strip())
    for _ in range(n):
        P, C = input().split()
        C = int(C)

        print("\n==============================")
        print(f"Configuração inicial: {P}, C = {C}")

        # 1) String -> lista de bits Gray
        gray_bits = [1 if ch == 'O' else 0 for ch in P]
        print(f"Gray inicial bits   = {gray_bits}")

        # 2) Gray -> Binário
        binary_bits = gray_to_binary(gray_bits)
        print(f"Binário convertido  = {binary_bits}")

        # 3) Binário -> número inteiro
        num = 0
        n_bits = len(binary_bits)
        for i, bit in enumerate(binary_bits):
            num |= (bit << (n_bits - 1 - i))
        print(f"Número inteiro      = {num}")

        # 4) Soma C (mod 2^n_bits)
        num = (num + C) % (1 << n_bits)
        print(f"Número após soma    = {num}")

        # 5) Número inteiro -> lista de bits binário
        new_binary = []
        for i in range(n_bits):
            new_binary.append((num >> (n_bits - 1 - i)) & 1)
        print(f"Novo binário bits   = {new_binary}")

        # 6) Binário -> Gray
        new_gray = binary_to_gray(new_binary)
        print(f"Novo Gray bits      = {new_gray}")

        # 7) Bits -> String 'O'/'X'
        result = ''.join('O' if bit else 'X' for bit in new_gray)
        print(f"Resultado final     = {result}")

"""
3
XOXXO 1
XOXXO 2
XOXXO 13
"""

if __name__ == "__main__":
    solve()