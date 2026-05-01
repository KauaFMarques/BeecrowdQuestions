def main():
    case_number = 1
    
    while True:
        knight_pos = input().strip()
        if knight_pos == '0':
            break
        
        knight_row = int(knight_pos[0])
        knight_col = ord(knight_pos[1]) - ord('a') + 1
        
        pawns = []
        for _ in range(8):
            pawn_pos = input().strip()
            pawn_row = int(pawn_pos[0])
            pawn_col = ord(pawn_pos[1]) - ord('a') + 1
            pawns.append((pawn_row, pawn_col))
        
        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        
        pawn_attacks = [
            (-1, -1), (-1, 1)
        ]
        
        valid_moves = 0
        
        for move in knight_moves:
            new_row = knight_row + move[0]
            new_col = knight_col + move[1]
            
            if 1 <= new_row <= 8 and 1 <= new_col <= 8:
                safe = True
                
                for pawn in pawns:
                    for attack in pawn_attacks:
                        attack_row = pawn[0] + attack[0]
                        attack_col = pawn[1] + attack[1]
                        
                        if attack_row == new_row and attack_col == new_col:
                            safe = False
                            break
                    if not safe:
                        break
                
                if safe:
                    valid_moves += 1
        
        print(f"Caso de Teste #{case_number}: {valid_moves} movimento(s).")
        case_number += 1

if __name__ == "__main__":
    main()