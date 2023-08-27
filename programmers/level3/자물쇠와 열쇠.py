def rotate_90_degree(array):
    row_length = len(array)
    column_length = len(array[0])
    
    mat = [[0] * column_length for _ in range(row_length)]
    
    for r in range(row_length):
        for c in range(column_length):
            mat[c][row_length - 1 - r] = array[r][c]
    
    return mat

def check(mat):
    row_length = len(mat) // 3
    column_length = len(mat[0]) // 3
    
    for r in range(row_length, row_length *2,1):
        for c in range(column_length,column_length *2 , 1):
            if mat[r][c] != 1:
                return False
    
    return True
    
def solution(key, lock):
    lock_row = len(lock)
    lock_column = len(lock[0])
    
    new_lock = [[0] * lock_column * 3 for _ in range(lock_row * 3)]
    
    for r in range(lock_row):
        for c in range(lock_column):
            new_lock[lock_row + r][lock_column + c] = lock[r][c]
    
    for i in range(4):
        key = rotate_90_degree(key)
        
        for r in range(lock_row * 2):
            for c in range(lock_column * 2):
                for row in range(len(key)):
                    for column in range(len(key[0])):
                        new_lock[r+row][c+column] += key[row][column]
                if check(new_lock):
                    return True
                for row in range(len(key)):
                    for column in range(len(key[0])):
                        new_lock[r+row][c+column] -= key[row][column]
    
    return False