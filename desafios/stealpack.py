import sys

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    results = []
    
    while idx < len(data):
        N = int(data[idx])
        idx += 1
        if N == 0:
            break
            
        cards = list(map(int, data[idx:idx + N]))
        idx += N
        
        pack = []
        stolen_sum = 0
        
        for card in cards:
            while pack and pack[-1] >= card:
                stolen_sum += pack.pop()
            pack.append(card)
            
        results.append(str(stolen_sum))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()