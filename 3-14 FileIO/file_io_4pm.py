"""
    file input output (file io)

        read() reads the entire file and returns it as a single string.

            read is somewhat dangerous becaues you're reading the entire file.
            Small text files (great), bigger file (be careful)

        readline() - reads a single line of text out of the file.
            Doesn't remove the endlines from the file contents


        readlines() - reads the entire file, splits it into lines
            doesn't remove the endlines from the line strings
            almost the same as read().split() that would remove the endlines.


"""
read_me_file = open('read_me.txt')
print(read_me_file.read())
print('go again!')
print(read_me_file.read())  # reads from the "cursor" to the end of the file, already there.
print('what happened?')
read_me_file.close()

read_me_file = open('read_me.txt')
print(read_me_file.read())
read_me_file.close()

read_me_again = open('read_me.txt')
print(read_me_again.readline())
print(read_me_again.readline())
print(read_me_again.readline())
print(read_me_again.readline())
print(read_me_again.readline())
print(read_me_again.readline())
read_me_again.close()

"""
    When you call read() or readline() on an empty file or file where the cursor is at the end
    it will give you back empty string.
"""
open_again = open('read_me.txt')
print(open_again.readlines())
open_again.close()


one_more_time = open('read_me.txt')
for line in one_more_time:
    print('The line in the file is: ', line.strip())
"""
    Not an infinite loop, for loop will exit at the end of the file.  
"""

filename = input('what do you want the file to be called? ')
my_file = open(filename, 'w')

my_string = input('What do you want to put into the file? ')
while my_string != 'quit':
    my_file.write(my_string + '\n')  # if you want an endline, you must do this.
    my_string = input('What do you want to put into the file? ')

my_file.close()

"""
    BIGGEST WARNING EVER: write mode will zero out your file, 
        if you care even 1% about anything in that file, do not use 'w' to open it.  

    Why do you want to close files?
        If you open a file in write mode, only your program has access to that file (to write stuff)
        If you don't close the file, 99% of the time, the OS will close the file for you.
            In the 1% case, the OS will forget to close your file, you can't open it again.
            Generally until you restart the computer or something similar.  
            
        When you're writing, the closing of the file clears the buffer.  
"""

"""
    Read mode - 'r' or just unfilled open(filename), open(filename, 'r')
    Write mode - 'w' open(filename, 'w')
    Append mode - 'a' open(filename, 'a')
        Opens the file, puts the cursor at the end of the file, sets you to write mode.
        Allows you to append ot the file without deleting it, etc.  
"""

animal_file = open(filename, 'a')

my_string = input('What do you want to put into the file? ')
while my_string != 'quit':
    animal_file.write(my_string + '\n')  # if you want an endline, you must do this.
    my_string = input('What do you want to put into the file? ')

animal_file.close()


# no such thing as writeline (same as write)
# but there is a writelines <- plural

new_file = open('my_new_file.awesome', 'w')
# the last thing here is called the file extension
# back in the mega-old-days files could be 8 character long in name extensions were 3 chars..
# jpg, mp3, mp4, txt, png, pdf, pds, stl, bat, obj, gif graphical
# make up my own file extension, it doesn't matter.  game1.board game1.txt

new_file.writelines(['hearty\n', 'fasten\n', 'capture\n', 'loosen\n', 'verbs\n'])
new_file.close()

def really_writelines(the_file, the_lines):
    for line in the_lines:
        the_file.write(line + '\n')


with open('read_me.txt') as read_file:
    # read_file = open('read_me.txt')
    print(read_file.read())
    # you're good to read or write (if you open in write mode)
    # you don't need to close the file, with does that for you.

# Causes a ValueError (reading a closed file)
# read_file.readline()


