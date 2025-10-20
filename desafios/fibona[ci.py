MOD = 1000007

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    idx = 1
    
    for _ in range(T):
        k = int(data[idx]); idx += 1
        n = int(data[idx]); idx += 1
        
        if n < k:
            results.append(str(n - 1))
            continue
        
        fib = [0] * (n + 1)
        for i in range(k):
            fib[i] = i
        
        current_sum = sum(fib[:k]) % MOD
        
        for i in range(k, n):
            fib[i] = current_sum
            current_sum = (current_sum + fib[i] - fib[i - k]) % MOD
        
        results.append(str(fib[n - 1] % MOD))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()