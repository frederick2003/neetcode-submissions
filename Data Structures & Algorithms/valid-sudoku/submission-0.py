class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Iterate across rows
        for row_i in range(9):
            elements = set()
            for col_i in range(9):
                current_element = board[row_i][col_i]
                if current_element == ".":
                    continue
                if current_element in elements:
                    return False          
                elements.add(current_element)

        # Iterate down columns
        for col_i in range(9):
            elements = set()
            for row_i in range(9):
                current_element = board[row_i][col_i]
                if current_element == ".":
                    continue
                if current_element in elements:
                    return False
                elements.add(current_element)

        # Interate across the 3 x 3 Boxes
        for box_num in range(9):
            start_row = (box_num // 3) * 3
            start_col = (box_num % 3) * 3
            elements = set()
            for k in range(9):
                cur_row = start_row + (k // 3)
                cur_col = start_col + (k % 3)
                current_element = board[cur_row][cur_col]
                if current_element == ".":
                    continue
                if current_element in elements:
                    return False
                elements.add(current_element)
        return True



        