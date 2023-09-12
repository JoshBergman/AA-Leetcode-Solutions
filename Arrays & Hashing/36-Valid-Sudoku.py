# notes from this problem:
# list comrehensions
# use enumerate to get index and value
# // operator for integer division (floor)


def isValidSudoku(self, board) -> bool:
    columnSets = [set() for _ in range(9)]
    boxSets = [[set() for _ in range(3)] for _ in range(3)]

    for i, row in enumerate(board):
        rowSet = set()
        for j, val in enumerate(row):
            if val == ".":
                continue  # Skip "." values
            if val in rowSet or val in columnSets[j] or val in boxSets[i // 3][j // 3]:
                return False
            rowSet.add(val)
            columnSets[j].add(val)
            boxSets[i // 3][j // 3].add(val)

    return True
