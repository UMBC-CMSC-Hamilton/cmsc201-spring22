the_file = open('read_me.txt')

"""
    3 functions to read contents of a file once you've opened it...
    
    the_file.read() - read the entire file and returns a single string which is the contents
    
    the_file.readlines() - reads the entire file, splits it into a list of lines (strings)
    
    the_file.readline() - reads one line of the file at a time.  if the file has no more lines
        it returns empty string.
    
    for line in the_file:
        use a for loop to call readline
    
    none of these functions strip off the endlines. (you may have to do that)
"""

print(the_file.read())
print('lets go again')
print(the_file.read())
print('did you see anything?')
the_file.close()

the_file_again = open('read_me.txt')

print(the_file_again.readlines())
the_file_again.close()

once_more = open('read_me.txt')
print(once_more.readline())
print(once_more.readline())
print(once_more.readline())
print(once_more.readline())
print(once_more.readline())
print(once_more.readline())

once_more.close()

last_time = open('read_me.txt')

# this is probably the most useful file read operation, technically readline() but its secretly being called
for line in last_time:
    print('The line is', line)

last_time.close()
"""
    Why do we close files?

        To prevent the operating system from locking us out of a file.
            Generally only for file writes not for reads, but very important for writes.  
        There is a secret cursor in a file which does the reading.  
            To reset the read cursor is also a good reason to close a file and reopen.  
"""


"""
    How do you write to a file?
    
    You have to call open, but the second argument has to be 'w'
    
        if you use 'r' everything works as before, you get read mode.  
        
        We need to add the endlines ourselves write function won't do that.
        
        When you open a file in write mode, it deletes the contents of the file and sets the cursors
        to start of the file.  
"""
greatest_file = open('greatest_file.text', 'w')

my_string = input('Tell me something to put into the file: ')
while my_string != 'quit':
    greatest_file.write(my_string + '\n')
    my_string = input('Tell me something to put into the file: ')

greatest_file.close()

"""
    the alternative is called "append mode"
    
"""

greatest_file = open('greatest_file.text', 'a')
# sets the cursor to the end
# doesn't erase the file contents
my_string = input('Tell me something to put into the file: ')
while my_string != 'quit':
    greatest_file.write(my_string + '\n')
    my_string = input('Tell me something to put into the file: ')

greatest_file.close()


"""
    file.writelines - similar to read lines except it's writing
        instead of taking a string, it takes a list of strings
"""

new_file = open('new_file.txt', 'w')
# write lines is really more like write strings
string_list = ['able', 'baker', 'charlie', 'delta', 'echo']
for line in string_list:
    new_file.write(line + '\n')


for i in range(len(string_list)):
    string_list[i] = string_list[i] + '\n'
new_file.writelines(string_list)

new_file.close()


"""
    with statement...
"""
with open('the_new_file.txt', 'w') as the_new_file:
    # the_new_file = open('the_new_file.txt', 'w')
    my_string = input('Tell me something to put into the file: ')
    while my_string != 'quit':
        the_new_file.write(my_string + '\n')
        my_string = input('Tell me something to put into the file: ')

    # when the with statement exits, it'll close the file for you, don't have to remember.

# this will cause a ValueError (write on a closed file)
# the_new_file.write('something')

