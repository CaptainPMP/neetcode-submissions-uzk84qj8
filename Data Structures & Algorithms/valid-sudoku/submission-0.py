class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                print(board[i][j], end = " ")
            print("\n")
        seen_rows = [set() for _ in range(9)]
        seen_cols = [set() for _ in range(9)]
        seen_chunk = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in seen_rows[i]:
                    return False
                seen_rows[i].add(board[i][j])

                if board[i][j] in seen_cols[j]:
                    return False
                seen_cols[j].add(board[i][j])

                calculated_index = int(i/3) * 3 + int(j/3)
                if board[i][j] in seen_chunk[calculated_index]:
                    return False
                seen_chunk[calculated_index].add(board[i][j])
        return True
        