# not part of the answer
names = {}
# the answer
"Eric" in names and "George" not in names
# if you wanted to search values: (never be a question)
"Eric" in names.values() and "George" not in names.values()

"""
Write a boolean expression that returns True when row is a
legal index for my_2d_list and col is a legal index for my_2d_list[row].
Only use non-negative indices, assume that my_2d list is in fact a 2d list.
"""
my_2d_list = [[0, 0], [1, 1]]
row = 0
col = 0
# the answer
0 <= row < len(my_2d_list) and 0 <= col < len(my_2d_list[row])
my_2d_list[row][col]

test_string = "abracadabra"
split_list = test_string.split("a")
print('z'.join(split_list))


def count_a_keys(d):
    total = 0
    for key in d:
        if key and key[0] == 'a':
            for val in d[key]:
                total += val
    
    return total


def sum_row_col(grid, row, col):
    total = 0
    for x in grid[row]:
        total += x
    
    for j in range(len(grid)):
        if j != row:
            total += grid[j][col]
    
    return total



def sum_row_col(grid, row, col):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[row])):
            if i == row or j == col:
                total += grid[i][j]
                
    return total

print(sum_row_col([[8, 2],
                   [5, 7]], 1, 0))
print(sum_row_col([[1, 2, 3],
                   [2, 3, 4],
                   [3, 7, 9]], 0, 0))
print(sum_row_col([[1, 2, 3],
                   [2, 3, 4],
                   [3, 7, 9]], 2, 1))
