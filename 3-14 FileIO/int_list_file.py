with open('int_file.txt', 'w') as int_file:
    my_string = input('Enter number or quit: ')
    while my_string != 'quit':
        int_file.write(my_string + '\n')
        my_string = input('Enter number or quit: ')

total = 0
with open('int_file.txt', 'r') as int_file:
    for line in int_file:
        print(line)
        total += int(line.strip())
    print(total)


#
s = 'False'
print(bool(s))
#
my_bool_list = []
if s == 'False':
    my_bool_list.append(False)
elif s == 'True':
    my_bool_list.append(True)