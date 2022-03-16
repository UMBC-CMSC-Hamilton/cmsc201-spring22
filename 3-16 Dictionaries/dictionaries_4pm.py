"""
    Dictionaries - most similar to lists.

        Hash Table, Hash Map

"""
my_list = ['a', 'b', 'c']
print(my_list[1])

my_dict = {}
my_other_dict = dict()

my_dict['hello'] = 5
print(my_dict['hello'])

letters = {'a': 5, 'b': -2, 'c': 14}
print(letters['a'], letters['c'])
# x: y
# x is the "key" which is the thing we plug into the dictionary to get the value
# y is the "value"

# this will generate a KeyError because 'd' is not in the dictionary.
# print(letters['d'])

letters['w'] = 54
letters['q'] = 17
print(letters)
"""
    Ints, floats, bools, strings, None

    immutable (primitive data types + None)
    Anything immutable can be used as an key
        datetime, tuples
    
    Not Immutable (mutable):
        Lists, dictionaries, "everything else"
"""

letters[True] = 15
letters[False] = 12
print(letters)
letters[5] = 123
letters[15] = 74
print(letters)
letters[3.14159] = 89
letters[2.718] = 44
print(letters)
"""
    Round-off error
        floats can only store a finite number of "binary digits / bits"
        and that means there may be inaccuracies 
"""

# can't use a list as a key
# letters[[1, 2, 3]] = 14
"""
    Tuple - list but immutable
    parentheses instead of brackets and you get a tuple. 
"""
letters[(1, 2, 3)] = 4
my_tuple = (1, 2, 3)

# this does'nt exist
# my_tuple.append(5)
print(my_tuple[2])
# my_tuple[2] = 15

# my_list = [1, 2, 3]
# letters[my_list] = 5
# my_list.append(4)

"""
    Values can be anything. 
"""

new_dict = {'a': [1, 2, 3], 'b': [4, 8], 'c': [1, 3, 6]}
print(new_dict)

"""
    When you iterate over a dictionary, you get the keys not the values.
    But that's ok because you can get the values yourself.
"""
for x in new_dict:
    print(x, new_dict[x])

"""
    Two ways to avoid a KeyError
"""

key = input('Tell me a key: ')
if key in new_dict:
    print(new_dict[key])
else:
    print(key, 'was not in there')

print(new_dict.get(key))  # when the key exists it gives you the same result as brackets
# when the key doesn't exist, it will return None
print(new_dict.get(key, "The key did not exist."))
"""
    You can't tell the difference between an item being in the dictionary with that value
    or not being in the dictionary and just returning the default

    Use the in keyword to figure out which is which.  
"""
print(new_dict.get(key, [1, 2, 3]))

sample_dict = {'a': 4, 'b': 21, 'c': 8, 'd': 34, 'e': 81}
# if we want to add up all the values, then what do we do?
total = 0
for key in sample_dict:
    total += sample_dict[key]
print('The total is', total)

"""
    Removal from dictionaries
        del keyword
"""

del sample_dict['c']
del sample_dict['d']
# delete something not in the dictionary and you get another key error
if 'r' in sample_dict:
    del sample_dict['r']

print(sample_dict)

"""
Space inefficient, use a list instead

Very time efficient read and write times that are O(1) - constant time.  
"""

my_var = 123
print(my_var)
# del my_var
# print(my_var)


def delete_me(x):
    return x + 1

# dont delete functions, why are you doing that?
print(delete_me(5))
# del delete_me
# print(delete_me(5))

# if you ever need the number of things in a dictionary, you can use len to get it.
print(len(sample_dict))

students = {
    'Eric': {
        'student_id': 12345,
        'gpa': 3.5
    },
    'Sammie': {
        'student_id': 23451,
        'gpa': 4.0
    },
    'Sarah': {
        'student_id': 223432,
        'gpa': 2.5
    },
    'Bob': {
        'student_id': 232323,
        'gpa': 3.8
    }
}

average_gpa = 0
for student in students:
    average_gpa += students[student]['gpa']
    # average_gpa += students[student].get('gpa', 0)

if len(students) > 0:
    average_gpa /= len(students)
    print(average_gpa)


"""
    You want all the keys in a dictionary as a list

    list(dict.keys())
"""
print(list(students.keys()))

"""
    You want all the values in a dictionary as a list:
    
    list(dict.values())
"""
print(list(students.values()))

