"""
    Reversing examples
"""

a_list = [1, 4, 5, 8, 6, 3, 9]

# new_list = [9, 3, 6, 8, 5, 4, 1]
# how do we do that?

new_list = []
for i in range(len(a_list) - 1, -1, -1):
    new_list.append(a_list[i])

print(new_list)

newer_list = []
for i in range(len(a_list)):
    newer_list.append(a_list[len(a_list) - i - 1])

print(newer_list)

"""
    a_list = [1, 4, 5, 8, 6, 3, 9]
    Even indices = 0, 2, 4, 6, 8, 10...
"""
for i in range(len(a_list)):
    if i % 2 == 0:
        print(i, a_list[i])

for i in range(0, len(a_list), 2):
    print(i, a_list[i])

"""
    if you wanted to look at odd indices you'd change the 0->1, thats it
"""
"""
    range(stop) start = 0 step = 1
    range(start, stop), step = 1
    range(start, stop, step)
"""

"""
    1 - dimensional list = list
    [4, 5, 6, 7, 1, 2, 3]
    ['hello', 'party', 'hat']
    
    2 - dimensional list = list of 1-d lists
"""

my_grid = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

print(my_grid[0])
print(my_grid[2])  # use one set of brackets, you get the list at that index
# if you want an element you need two sets of brackets
print(my_grid[2][2])
print(my_grid[0][2])

total = 0
# i goes through the "rows" or the outer lists
for i in range(len(my_grid)):
    # j iterates through the columns or the elements within the inner lists
    for j in range(len(my_grid[i])):
        total += my_grid[i][j]

print(total)

new_2d_list = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3],
    [1, 2]
]

for i in range(len(new_2d_list)):
    # j iterates through the columns or the elements within the inner lists
    for j in range(len(new_2d_list[i])):
        total += new_2d_list[i][j]

bad_2d_list = [
    [1, 2, 3, 4 ,5, 6],
    [76, 4, 23]
]

for i in range(len(bad_2d_list)):
    # j iterates through the columns or the elements within the inner lists
    for j in range(len(bad_2d_list[i])):
        # remember to check the length of the inner list
        # len(2d_list[row]) or len(2d_list[i])
        print(bad_2d_list[i][j])

square_list = [
    [0, 1, 1, 0],
    [2, 1, 0, 1],
    [5, 7, 3, 2],
    [2, 3, 4, 5]
]
print('Diagonal elements')
for i in range(len(square_list)):
    for j in range(len(square_list[i])):
        if i == j:
            print(square_list[i][j])

# I want to print out the diagonal elements

print('One loop diagonal')
for i in range(len(square_list)):
    print(square_list[i][i])

"""
    How many loops do you need?
    
        I'm just looking up a single element in the grid - 0 loops?
        Diagonal, scanning just one row, -> 1 loop
        scanning through every element -> 2 loops
"""

board = [
    ['o', 'x', 'x'],
    ['o', 'o', 'o'],
    ['x', '', 'o']
]

"""
    Check to see if a row matches
    Check to see if a column matches
    Check Diagonal
    Check Anti-diagonal
"""

# they are boolean flags, monitor state in a program, wait for a condition to be true
# once set they "lock on"
x_victory = False

for row in board:
    if row[0] == row[1] == row[2] == 'x':
        x_victory = True


for i in range(len(board)):
    if board[0][i] == board[1][i] == board[2][i] == 'x':
        x_victory = True

if board[0][0] == board[1][1] == board[2][2] == 'x':
    x_victory = True

if board[0][2] == board[1][1] == board[2][0] == 'x':
    x_victory = True

print(x_victory)

for player in ['x', 'o']:
    victory = False
    for row in board:
        if row[0] == row[1] == row[2] == player:
            victory = True

    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] == player:
            victory = True

    if board[0][0] == board[1][1] == board[2][2] == player:
        victory = True

    if board[0][2] == board[1][1] == board[2][0] == player:
        victory = True

    if victory:
        print(player, 'has won')