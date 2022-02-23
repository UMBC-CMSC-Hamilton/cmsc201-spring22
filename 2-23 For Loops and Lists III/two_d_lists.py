"""
    What is a 2d-list?
        List of lists
"""
if False:
    example_list = [
        [1, 2],
        [3, 4]
    ]
    print(len(example_list))

    print(example_list[1])

    """
        To access elements you need two sets of brackets
            one for the outer list and one for inner list
    """

    new_example = [[5, 7, 6, 5, 6, 7], [2, 3, 9, 5, 2], [6, 7, 1, 11, 0]]

    print(new_example[1][2])

    # range over the first index of the list
    for i in range(len(new_example)):
        # second for loop always needs to access not the outer list
        # but the inner list to see what its length is
        for j in range(len(new_example[i])):
            print(i, j, new_example[i][j])

    """
        2d list:
            first index = "row"
            second index = "column"
        
    """

    num_rows = int(input('How many rows? '))
    num_cols = int(input('How many cols? '))
    symbol = input('What should the starting symbol be? ')
    new_big_list = []
    for i in range(num_rows):
        new_row = []
        # this new row creation is actually necessary
        for j in range(num_cols):
            new_row.append(symbol)
        new_big_list.append(new_row)

    print(new_big_list)

    for row in new_big_list:
        print(row)

    newer_bigger_list = []
    new_row = []
    # lists happen to be mutable
    # lists when you append them are appended "by reference"
    for j in range(num_cols):
        new_row.append(symbol)

    for i in range(num_rows):
        newer_bigger_list.append(list(new_row))

    print('This is a new list: ')
    for row in newer_bigger_list:
        print(row)

        newer_bigger_list[3][2] = 'a'
        print(newer_bigger_list)

    a_list = [1, 2, 3]
    # setting a reference (not a copy)
    b_list = list(a_list)
    b_list[2] = 7
    print(a_list)

    # ints, strings, floats, bools = immutable
    my_int = 17
    other_int = my_int
    # they are copied rather than referenced
    other_int = 3
    print(my_int)

    """
        If you want to actually a copy a list, use list(whatever_list)
        
        If you want to make a reference, then assignment will work
            ref_list = other_list, now they are the same underlying list
    """

    """
        Trying to modify an immutable object (int, bool, string, float)
    """
    string_happy = 'happy'
    # string_happy[2] = 'z'
    # print(string_happy)

    string_happy = 'hazpy'
    # technically we are reassigning the variable not really modifying the
    # underlying string object.

"""
    Tic Tac Toe
    
     - check rows
     - check cols
     - check diag
     - check anti-diagonal
"""


"""
    boolean flag is a variable that tracks a state change in a program
    
        if before x is not winning, after a move, x is winning, we should
            set our boolean flag to True
"""

x_victory = False


the_board = [
    ['o', 'o', 'x'],
    ['x', 'o', ''],
    ['x', 'o', '']
]

for row in the_board:
    print('The row is', row)
    if row[0] == row[1] == row[2] == 'x':
        x_victory = True


for i in range(len(the_board)):
    if the_board[0][i] == the_board[1][i] == the_board[2][i] == 'x':
        x_victory = True


if the_board[0][0] == the_board[1][1] == the_board[2][2] == 'x':
    x_victory = True

anti_diagonal_victory = True
for i in range(len(the_board)):
    if the_board[i][len(the_board) - 1 - i] != 'x':
        anti_diagonal_victory = False

if anti_diagonal_victory:
    x_victory = True

print('Did x win?', x_victory)

for symbol in ['x', 'o']:
    victory = False
    for row in the_board:
        if row[0] == row[1] == row[2] == symbol:
            victory = True

    for i in range(len(the_board)):
        if the_board[0][i] == the_board[1][i] == the_board[2][i] == symbol:
            victory = True

    if the_board[0][0] == the_board[1][1] == the_board[2][2] == symbol:
        victory = True

    anti_diagonal_victory = True
    for i in range(len(the_board)):
        if the_board[i][len(the_board) - 1 - i] != symbol:
            anti_diagonal_victory = False

    if anti_diagonal_victory:
        victory = True

    if victory:
        print(symbol, 'has won')
