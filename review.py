from collections import Counter

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

# Define a function check_sudoku() here:
def check_sudoku(square):
    n = len(square)
    for key in square:
        if(type(key[0]) is not int):
            return False
        if(key[0] < 1):
            return False
        if(max(key) > n):
            return False
        times = (Counter(key))
        for item in times: 
            if(times[item] > 1):
                return False
    
    i = 0
    while(i < len(square)):
        column = []
        for key in square:
            column.append(key[i])
        i+=1
        if(max(column) > n):
            return False
        cTimes = Counter(column)
        for cItem in cTimes: 
            if(cTimes[cItem] > 1):
                return False
    return True

print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False