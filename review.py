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
    # Find the size of the square
    n = len(square)
    # Check rows
    for key in square:
        # Return false if using a type other than int (string or double)
        if(type(key[0]) is not int):
            return False
        # Return false if negative or zero
        if(key[0] < 1):
            return False
        # Return false if out of bounds
        if(max(key) > n):
            return False
        # Return false if duplicates
        times = (Counter(key))
        for item in times: 
            if(times[item] > 1):
                return False
    
    # Check columns
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

# An example solution for the check_sudoku() function
def check_sudoku_alternate_solution(square):
    for row in square:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        check_list = list(range(1, len(square[0]) + 1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(square[0])):
        # Checking each column in the square
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] not iin check_list:
                return False
            check_list.remove(row[n])
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