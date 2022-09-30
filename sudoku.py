import numpy as np

grid = [[0,0,0,7,0,0,0,0,0],
        [0,4,0,0,5,1,0,6,0],
        [0,0,0,6,0,0,4,0,9],
        [0,0,0,0,0,0,0,1,3],
        [0,7,3,0,0,0,2,9,0],
        [4,8,0,0,0,0,0,0,0],
        [9,0,2,0,0,6,0,0,0],
        [0,6,0,2,8,0,0,5,0],
        [0,0,0,0,0,7,0,0,0],]

#print(grid)
#print(np.matrix(grid))

def possible(row, column, number):
    global grid
    for i in range (0,9):
        if grid[row][i] == number:
            return False
    for i in range (0,9):
        if grid[i][column] == number:
            return False
    x0 = (row // 3) * 3
    y0 = (column // 3) * 3 
    for i in range (0,3):
        for j in range (0,3):
            if grid[x0 + i][y0 + j] == number:
                return False

    return True

count = 0
count1 = 0

def solve():
    global grid
    global count
    global count1
    for row in range (0,9):
        for column in range (0,9):
            if grid [row][column] == 0:
                for number in range (1,10):
                    count1 = count1 + 1
                    if possible(row, column, number):
                        grid[row][column] = number
                        count = count + 1
                        solve()
                        #print(np.matrix(grid))
                        grid[row][column] = 0
                        #print(np.matrix(grid))
                return

    print(np.matrix(grid))
    #input('Are there more solutions?')

solve()
print(count)
print(count1)