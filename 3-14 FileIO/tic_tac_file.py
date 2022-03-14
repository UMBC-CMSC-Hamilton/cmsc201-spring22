board = [['x', '_', 'o'],
         ['o', 'x', '_'],
         ['o', 'x', '_']]

file_name = input('What file do you want to save? ')
with open(file_name, 'w') as board_file:
    # let's use commas to separate the individual letters
    for row in board:
        board_file.write(':'.join(row) + '\n')

the_big_board = []
with open(file_name, 'r') as the_board_file:
    board_string = the_board_file.readlines()
    for line in board_string:
        the_big_board.append(line.strip().split(':'))

print(the_big_board)

"""
    
"""
