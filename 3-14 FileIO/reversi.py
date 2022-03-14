# we know it's a square
# black pieces, white pieces
# 'b' for a black piece, 'w' for a white piece and '-' for empty place
# size can be variable

size = 5
board = [['b', 'w', 'w', '-', '-'],
         ['w', 'b', 'w', 'b', '-'],
         ['b', 'w', 'w', '-', '-'],
         ['w', 'b', 'w', '-', 'b'],
         ['w', 'b', 'w', 'b', 'b']
]

save_name = input('What name of board do you want to save? ')
with open(save_name, 'w') as save_file:
    save_file.write(str(size) + '\n')

    for row in board:
        save_file.write(''.join(row) + '\n')


new_board = []
with open(save_name) as load_file:
    new_size = int(load_file.readline())
    for i in range(new_size):
        new_board.append(list(load_file.readline().strip()))

print(new_board)