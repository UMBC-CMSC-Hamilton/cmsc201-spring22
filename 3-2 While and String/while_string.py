"""
    What is a while loop?
        loop that repeats while a condition is true
        if statement on repeat

    What is the biggest danger of a while loop?
        Infinite Looping
            Update variables in order to prevent the same condition from being checked infinitely
            Check to make sure the condition matches what you think it is.

    """
if False:
    print(__name__)
    my_string = input('Tell me string: ')
    index = 0
    while index < len(my_string):
        print(my_string[index])
        index += 1

    """
        any for loop can be rewritten as a while loop
        
        not every while can be made into a for loop
    """

    # what is this called? priming the input, just like priming the pump... oh no...
    s = input('Enter word: ')
    while s != 'abrogate':
        s = input('No that wasn\'t the word: ')

    """
        
    """

    """
        Secret about strings: they can basically be treated as lists
            you can get characters by index
            unfortunately you can't set by index
    """

    s = input('Tell me a string: ')
    for i in range(len(s)):
        print(s[i])

    # can't do this...
    # s[2] = 'a'

    # First fix, actually make it into a list
    my_characters = list(s)
    print(my_characters)

    # my_characters[0] = ''
    # print(my_characters)
    """
        list(string) will convert a string into a list of characters
        
        in order to convert back we need to use the join function
        
        separator.join(list_of_strings)
    
    """

    print("x".join(my_characters))
    print("".join(my_characters))
    print(" happy ".join(my_characters))
    print('\t'.join(my_characters))
    #  this function returns the string you can save it into a variable.

    my_input = input('tell me a string: ')
    # lets replace all x's with z

    char_list = list(my_input)
    for i in range(len(char_list)):
        if char_list[i] == 'x':
            char_list[i] = 'z'

    print(char_list)  # not exactly what you want as output...
    print(''.join(char_list))

    my_animals = ''.join(['lazy', 'cat', 'dog', 'fish', 'shark'])
    print(my_animals)

    my_int_list = [1, 2, 3, 4]
    my_string_list = []
    for x in my_int_list:
        my_string_list.append(str(x))

    print(''.join(my_string_list))

    """
        str.strip() - have you ever dreamed that there is a function that strips whitespace?
            well there is... it's called strip... wow
            
    """

    what_we_want = input('What do you want? ')
    print(what_we_want)
    print(what_we_want.strip(), end='//')

    """
        lstrip and rstrip exist, basically the same except they only do half the job.  
    """
    """
        One extra thing you can do with it.  you can specifically strip certain types of white space
    """

    s = input(': ').lower().strip()
    while s != 'quit':
        s = input(': ').lower().strip()

    my_whitespace_string = '    \t\t\t\n\n\n\n\n\r\r\r\r\n\n\n\n\n    \t\t\t\t'
    print(len(my_whitespace_string.strip(' ')))

    print('aabbbabbabababbaaaa'.strip('a'))

    """
        Split is just the best.
        
        
    """
    the_string = 'a string that is made of words like this separated by whitespace'
    the_list = the_string.split()
    print(the_list)

    print(' | '.join(the_list))

    new_string = 'when once i was in a place something i dont know'
    print(new_string.split('a'))

    newer_string = 'three of them went to the market of food, some call it a supermarket of things, like the internet of things'
    print(newer_string.split('of'))

"""
    slices - substring or a sublist that you can make from an original list
        notation is...
        my_string[4: 7]
"""

my_string = 'internet of things == spyware'
print(my_string[15:21])

my_other_string = 'abcdefg'
print(my_other_string[2:5])
# slices are "forgiving"
print(my_other_string[0:100])

my_list = [2, 5, 6, 4, 3, 5, 6, 5, 3, 3, 6, 6, 4]
print(my_list[4:10])

word = 'charm'

new_word = word[0:2] + 'u' + word[3:5]
print(word, new_word)

slice_string = 'slice is a drink isn\'t it?'
print(slice_string[10: len(slice_string)])
print(slice_string[10:])  # python will by default use the length of the object (str or list) as the second parameter

print(slice_string[:7])  # python by default counts the first parameter as zero

# if you want to copy a list without using list(old_list)

my_list = [1, 2, 3, 4, 5]
# is new list a copy or is it a reference?
new_list = my_list[:]
# same as doing new_list = list(my_list)

print(new_list)
new_list[2] = 17
print(my_list)

a_list = ['a', 'b', 'c']
b_list = a_list
b_list[1] = 'z'
print(a_list)

