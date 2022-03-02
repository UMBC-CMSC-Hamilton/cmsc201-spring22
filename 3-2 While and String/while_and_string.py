"""
    Strings are immutable

"""
if False:
    # can't do this:
    my_hello_string = 'hello'
    # my_hello_string[3] = 'z'

    my_hello_string = 'another thing'
    print(my_hello_string)

    """
        How the heck can i do that?
            I want to replace a letter with the letter z, it is my only purpose
    """
    my_chars = list(my_hello_string)
    print(my_chars)
    # lists are mutable
    my_chars[5] = 'z'
    print(my_chars)

    # isnt quite right
    print(str(my_chars))

    mod_string = ' | '.join(my_chars)
    print(mod_string)

    """
        Here's how join works:
            separator (string)
            list of strings
            
            sep.join(the_list)
    """

    """
        If you want the characters out of a string, use list(that_string)
        
        If you want to put it back together, use sep.join(the_characters_from_the_string_as_a_list)
            separator (sep) must be a string
            list must be of strings
    """

    # print(', '.join([1, 2, 3, 4, 5]))

    new_list = []
    for x in [1, 2, 3, 4, 5]:
        new_list.append(str(x))

    print(new_list)
    print(': '.join(new_list))


    random_words = (' | '.join(['hello', 'goodbye', 'peace', 'stone', 'laptop', 'salmon']))
    print(random_words, len(random_words))

    """
        str.strip()
        
        Have you ever wanted a function that will remove whitespace from the start and end of your strong?
            Well, I've got one for you...
    
    """

    whitespace_string = '   hi       '
    print(whitespace_string.strip(), end=';')

    """
        What else is whitespace?
            spaces, tabs, line returns (newlines), carriage return
             , \t, \n, \r
    """

    more_whitespace = '   \t\t\t\n\n \r \r\r  \r\t   \t\t\r\r\r\r\n\n\n\n     '
    print(len(more_whitespace.strip()))


    next_test = "   how about this, what does it eliminate here?    \t\t\n"
    print(next_test)
    print(next_test.strip(), end=';\n')


    s = input(">> ")
    while s.strip().lower() != 'quit':
        s = input(">> ")

    """
        You can strip off specific characters that aren't whitespace
        Whenever you put in a string into the strip function, it considers each of the characters
            independently.
            
        If you want to strip out tabs and newlines but not spaces, 
            strip('\t\n')
            
        lstrip and rstrip
    """
    abababa = 'aaaaababababbbcdcdbababaaabbaaaaaa'
    print(abababa.strip('ab'))

    """
        Split is by far the most useful function here...
        
    """

    a_sentence = 'sentences are neither good nor evil, they just are'
    print(a_sentence.split())
    tab_split = 'does it \t\t\tsplit on tabs'
    print(tab_split.split())

    ab_split = "about table absolutely abab abacus abecederian obsequious abject"
    take_apart = ab_split.split('ab')
    """
        Because it starts with an ab it tells us that by leaving an empty string at the start
    """
    print('ab'.join(take_apart))

"""
    Slices - what is a slice?
    
    a sublist or substring
"""

my_int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_int_list[2: 5])
# a lot like range, start, stop, goes up to but doesn't include the stop
print(my_int_list[0: 7])
print(my_int_list[5: len(my_int_list)])

slicy_string = 'slice me up'
print(slicy_string[3: 8])

"""
    If the end is past the end of the string, then nothing bad happens
        takes you to the end of the string and stops. (same for lists)
"""
print(slicy_string[5:1000])
print(my_int_list[7:20005])

new_string = 'onceuponatimetherewasachicken'
print(new_string[:5])
# if there's no number here it will insert 0 by default

print(new_string[17:])
# default is to use the length of the object

new_list = ['able', 'baker', 'charlie', 'delta', 'echo']

# deep copies (true copes) real copies, not references, not shallow
newer_list = new_list[:]
print(new_list)
print(newer_list)
newer_list[2] = 'zebra'
print(new_list)
print(newer_list)

"""
Know this one by heart:

Deep Copy vs Shallow Copy (a shallow copy is not a copy)
Copy vs Reference

"""
a_list = [1, 2, 3]
b_list = list(a_list)
b_list[2] = 17
print(a_list, b_list)
