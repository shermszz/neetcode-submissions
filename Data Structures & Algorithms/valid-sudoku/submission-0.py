class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for i in range(9)] # hashset for 9 rows
        col_set = [set() for i in range(9)] # hashset for 9 columns
        list_of_sets = [set() for i in range(9)] # create a list of 9 hashsets for each subbox

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": continue
                global_row_set = row_set[r]
                global_col_set = col_set[c]
                if val in global_row_set or val in global_col_set:
                    return False
                else:
                    # The row and column is safe
                    global_row_set.add(val)
                    global_col_set.add(val)
                    # Next thing to check is the subbox we are in
                    row = r // 3
                    col = c // 3
                    subbox_num = (r // 3) * 3 + (c // 3)
                    set_of_concern = list_of_sets[subbox_num]
                    if val in set_of_concern:
                        # The val already exists in the subbox
                        return False
                    else:
                        set_of_concern.add(val)
        return True