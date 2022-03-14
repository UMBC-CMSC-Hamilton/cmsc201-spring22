"""

    What is a function?
        Ways to encapsulate a piece of code that you can run whenever you call the function.

        Very similar to the concept of functions in mathematics.
        Same notation for the most part.

    Returning Values

"""


def my_function():
    print('hello')


result = my_function()
print(result)


# a variable that is defined in the function definition is called a parameter
def increment(x):
    """
    :param x: there is a variable now that we can use as "input" into the function
    :return: returns x + 1
    """
    print(x + 1)
    return x + 1


# 7 would be called an argument
output = increment(7)
print(output)


# functions can have multiple parameters
def add_two_things(x, y):
    return x + y


print(add_two_things(3, 5))
print(add_two_things("red", "light"))
# print(add_two_things("red", 7))
"""
    In order to remember the returned result, you must save it into a variable
"""
result = add_two_things(21, 57)
add_two_things(43, 81)


def even_or_odd(number):
    if number % 2 == 0:
        return 'The number is even'
    else:
        # elif number % 2 == 1:
        return 'The number is odd'
    # this code is still unreachable
    print('end of function')


"""
    return is not the same as print
    
"""
print(even_or_odd(15))
print(even_or_odd(18))


def is_prime(test_number):
    if test_number <= 1:
        return False

    for x in range(2, test_number):
        if test_number % x == 0:
            return False

    return True


def test_is_prime():
    num = int(input('Tell me a number to prime test: '))
    while num != 0:
        print(is_prime(num))
        num = int(input('Tell me a number to prime test: '))


"""
    Let's make a new function...
        count all the p's in a string
"""


def count_the_p(the_string):
    count = 0
    for c in the_string:
        if c == 'p':
            count += 1

    return count


print(count_the_p('pupper'))
# this is weird ...
print(print('Hello there'))

# print(count)
"""
    Local scope 
        Any variable declared inside of a function is considered local
        A local variable has a "lifetime" it only lives as long as the function 
            is running.  
        Local variables are lost whenever a function returns or exits
        
        If you want to save a value from a function, that's why you have to 
            return it.  
            
        But returning doesnt give you the variable name, just the value.
        Only accessible in the function that declared them.
        
    Global Scope
        Any variable declared outside of a function (class) is considered global
        
        Global variables dont really have a lifetime (other than the length of the program)
        Global variables are accessible from anywhere, inside functions, outside functions, etc
        
"""

the_count = count_the_p('polyphemus')
print(the_count)


def count_the_sevens(number):
    count = 0
    while number > 0:
        if number % 10 == 7:
            count += 1

        number //= 10
    return count


"""
    We have two separate functions with two count variables (both called the same name)
    
"""

print(count_the_sevens(717))
print(count_the_p('preparation prospector'))

"""
    Mutability - basic data types:
        int, float, string, bool - immutable
        
        When it gets passed into a function it gets passed "by value"
        A new copy is made that you can modify, but it doesnt change the original.
        
    "everything else"*** - mutable
        lists, dictionaries (dict), classes
        
        Mutable objects pass by reference
        
        
"""


def change_int(x):
    x = x + 17


def change_list(my_list):
    my_list.append(17)


number = 5
change_int(number)
print(number)

the_list = [1, 2, 3, 4, 5]
change_list(the_list)
print(the_list)

"""
    What is a palindrome?
    
    a set of characters that is the same forwards and reversed/backwards
    racecar
    tacocat
    
"""


def is_palindrome(word):
    for i in range(len(word)):
        if word[i] != word[len(word) - 1 - i]:
            return False
    word = 'turnip'
    return True


def test_is_palindrome():
    word = input('Tell me a word: ')
    while word != 'quit':
        print(is_palindrome(word))
        print(word)
        word = input('Tell me a word: ')


test_is_palindrome()
