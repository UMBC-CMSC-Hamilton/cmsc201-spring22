import random

"""
    What is recursion?
        Recursion is where a function calls itself.
    
    Two different types of recursion:
        linear recursion (each function calls one other function)
        branching recursion (each function calls maybe multiple other copies of itself)
"""


def factorial(n):
    """ factorial(5) = 5 * factorial(4) = 5 * 24 = 120
        factorial(4) = 4 * factorial(3) = 4 * 6 = 24
        factorial(3) = 3 * factorial(2) = 3 * 2 = 6
        factorial(2) = 2 * factorial(1) = 2 * 1 = 2
        factorial(1) = 1 * factorial(0) = 1 * 1 = 1
        factorial(0) = 1
    """
    if n == 0:
        return 1
    else:
        # linear recursion
        return n * factorial(n - 1)


"""
    iterative vs recursive
    
        loop vs recusion
"""


def check_parens(the_string):
    level = 0
    for char in the_string:
        if char == "(":
            level += 1
        if char == ")":
            level -= 1
        if level < 0:
            return False
    
    return level == 0
    """
        if level == 0:
            return True
        else:
            return False
    """


def check_parens_rec(the_string):
    print('now checking: ', the_string)
    
    if not the_string:  # the_string == ""
        return True
    
    if the_string[0] != "(":
        return False
    # string not empty and the start == "("
    # find the matching index
    level = 0
    match_location = 0
    for i in range(len(the_string)):
        if the_string[i] == "(":
            level += 1
        elif the_string[i] == ")":
            level -= 1
        if level == 0 and match_location == 0:
            match_location = i
    # check both parts (start upto the match), (the match to the end)
    start_check = check_parens_rec(the_string[1: match_location])
    end_check = True
    if match_location < len(the_string) - 1:
        end_check = check_parens_rec(the_string[match_location + 1: len(the_string)])
    
    return start_check and end_check


# print(check_parens_rec(input('Enter a string with parentheses: ')))

PASSABLE = '_'
BLOCKED = '*'
THE_GOLD = 'G'
VISITED = 'v'


def make_grid(rows, cols):
    the_grid = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(random.choices([PASSABLE, BLOCKED], weights=[4, 1])[0])
        the_grid.append(new_row)
    
    x_gold = random.randint(0, rows - 1)
    y_gold = random.randint(0, cols - 1)
    the_grid[x_gold][y_gold] = THE_GOLD
    
    the_grid[0][0] = PASSABLE
    
    return the_grid


def display_grid(the_grid):
    for row in the_grid:
        print(' '.join(row))


def find_the_gold(current_pos, the_grid, counter):
    # current_pos = [y, x]
    y, x = current_pos
    if the_grid[y][x] == THE_GOLD:
        return [current_pos]
    
    if the_grid[y][x] != PASSABLE:
        return []
    
    the_grid[y][x] = str(counter)
    
    went_up = []
    went_right = []
    went_down = []
    went_left = []
    # go up
    if y - 1 > 0:
        went_up = find_the_gold([y - 1, x], the_grid, counter + 1)
    # go right
    if x + 1 < len(the_grid[y]):
        went_right = find_the_gold([y, x + 1], the_grid, counter + 1)
    # go down
    if y + 1 < len(the_grid):
        went_down = find_the_gold([y + 1, x], the_grid, counter + 1)
    # go left
    if x - 1 > 0:
        went_left = find_the_gold([y, x - 1], the_grid, counter + 1)
    
    if went_left:
        return went_left + [current_pos]
    if went_down:
        return went_down + [current_pos]
    if went_up:
        return went_up + [current_pos]
    if went_right:
        return went_right + [current_pos]

    # return went_down or went_up or went_right or went_left


my_grid = make_grid(10, 10)
display_grid(my_grid)
print(find_the_gold([0, 0], my_grid, 1))
display_grid(my_grid)
