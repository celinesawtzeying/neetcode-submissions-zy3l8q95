class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current == '.':
                    continue

                box_id = (i//3) * 3 + (j//3)
                if current in cols[j] or current in rows[i] or current in boxes[box_id]:
                    return False
                cols[j].add(current)
                rows[i].add(current)
                boxes[box_id].add(current)
        return True