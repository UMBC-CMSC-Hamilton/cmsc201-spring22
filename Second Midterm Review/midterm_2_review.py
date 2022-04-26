#  not the answer
names = {}
# the answer
"Eric" in names and "George" not in names

# not the answer
my_2d_list = [[0, 0], [1, 1]]
row = 0
col = 0
# the answer
0 <= row < len(my_2d_list) and 0 <= col <= len(my_2d_list[row])

words = {'veritable': 3}
print(words.get('happy'))

abra = 'abracadabra'
print(abra.split('a'))
print("z".join(abra.split('a')))


def count_a_keys(the_dict):
    big_total = 0
    for the_key in the_dict:
        if the_key and the_key[0] == 'a':
            for val in the_dict[the_key]:
                big_total += val
    
    return big_total


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
# 5 + 7 + 8 = 20

print(sum_row_col([[1, 2, 3],
                   [2, 3, 4],
                   [3, 7, 9]], 0, 0))
# 1 + 2 + 3 + 2 + 3 = 11

print(sum_row_col([[1, 2, 3],
                   [2, 3, 4],
                   [3, 7, 9]], 2, 1))

# 3 + 7 + 9 + 2 + 3

"""
    Write a recursive function which asks how many factors of 2 are there in a number?
"""


def count_2_factors(the_number):
    if the_number == 0:
        return 0
    if the_number % 2 == 1:
        return 0
    else:
        return 1 + count_2_factors(the_number//2)
    

print(count_2_factors(32))
print(count_2_factors(12))  # 2 * 2 * 3
print(count_2_factors(85680))


def count_the_as(my_string):
    if not my_string:
        return 0
    elif my_string[0] == 'a':
        return 1 + count_the_as(my_string[1:])
    else:
        return count_the_as(my_string[1:])
        
