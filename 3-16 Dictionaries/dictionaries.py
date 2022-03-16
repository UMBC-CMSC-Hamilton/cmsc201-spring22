"""
    New data type: dictionary

        Hash Table, Hash Map, Hash

        in python: Dictionary


"""

# to access elements you need the index, 0 to len(list) - 1
my_list = [3, 5, 2, 3]
my_list[2] = 17
print(my_list)

"""
    To create an empty dictionary
"""
my_first_map = {}
my_first_map = dict()

"""
    Indices can be anything immutable
    
    ints, floats, bools, strings <-- most often (datetime)
"""
my_first_map['hello'] = 5
print(my_first_map)

my_first_map['goodbye'] = -3
my_first_map['robot'] = 17

print(my_first_map)
"""
    Key value pairs:
    
        In a dictionary the "key" is the index and the value is the value stored
        
        For every value you need a key to access it.
        
        Key: value keys -> values, but values do not give keys back... 
"""

print(my_first_map['hello'])
# print(my_first_map[5])

string_list = ['a', 'b', 'c', 'a']
# can't do this: string_list['a']

my_first_map[True] = 123
my_first_map[False] = 88
my_first_map[23] = 47
my_first_map[3.14] = 2.718
my_first_map[1.6] = 'this is a string'

print(my_first_map)

"""
    Keys have to be immutable
    
    Values can be "literally" anything.
"""

list_map = {'Eric': [1, 2, 3], 'Robert': [4, 5, 6], 'Sarah': [1, 2, 3]}
print(list_map)

"""
    values can be lists or dictionaries or dicts of dicts etc
"""

dictionary_of_dictionaries = {'Eric': {'email': 'eric8', 'sid': 123},
                              'Robert': {'email': 'robert8', 'sid': 555},
                              'Sarah': {'email': 'sarah2', 'sid': 928}}

print(dictionary_of_dictionaries['Sarah']['email'])

"""
    Why do the keys have to be immutable?
    
        Not so secret reason: if they were mutable, then they could change

one_two_three = [1, 2, 3]

sample_dict = {
    one_two_three: 'happy',
    [4, 5, 6]: 'sad'
}

one_two_three.append(4)
"""

"""
    What the heck is a tuple?
        it's an immutable version of a list
"""

one_two_three = (1, 2, 3)
print(type(one_two_three))
sample_tuple_thing = {}
sample_tuple_thing[one_two_three] = 'hello'
print(sample_tuple_thing)
one_two_three = (4, 5, 6)
print(sample_tuple_thing)

my_dict = {'a': 4, 'b': 17, 'c': 21, 'd': 8, 'e': None}
print(my_dict)
my_dict = {'a': [3, 2, 8], 'b': [1, 2, 3], 'c': [4, 5, 6]}
print(my_dict)

print(my_dict['b'])
print(my_dict['b'][1])

# maybe keep the key types and the value types the same
# my_dict['e'] = 17
print(my_dict)

for key in my_dict:
    print(key, my_dict[key])
    my_dict[key].append(4)

print(my_dict)

people = {'Alice': 5, 'Bob': 208, 'Eve': 43, 'Charlie': 89, 'Sammy': 891} #, 'Roberto': 0
total = 0
for person in people:
    total += people[person]

print(total)

"""
    One warning:
        you are not guaranteed any particular order for the keys
"""

"""
    Removal from a dictionary!
    
    del keyword
"""
del people['Eve']
del people['Sammy']
print(people)

def delete_me_please(x):
    return x + 1

my_var = 5
print(my_var)
# del my_var
# print(my_var)
# avoid this bizarreness
# del people
# print(people['Alice'])

# be very careful
# print(delete_me_please(3))
# del delete_me_please
# print(delete_me_please(3))

"""
    Don't delete functions or variables unless you really really really mean it
"""

"""
    KeyError
"""
if 'Roberto' in people:
    print(people['Roberto'])
else:
    print('Roberto is not in the dictionary')

if 5 in people:
    print('Five is in people')
else:
    print('Five is not in people')

# if the key is not in the dictionary .get will return the default value
print(people.get('Roberto', 15))
# if you don't specify a default value, it's None
print(people.get('Roberto'))

letters = {'a': 4, 'b': 0, 'c': 15, 'd': 21, 'f': 55}

list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f']

total = 0
for x in list_of_letters:
    total += letters.get(x, 0)

print(total)


print(letters.keys())
keys_list = list(letters.keys())
print(keys_list[2], keys_list[4])
print(letters.values())
"""
    don't use letters.values(): here's why:
    
        if you use dict.values() then the values are no longer associated with the keys
            ask yourself do i need a dictionary?
            if not use a list
            if so, figure out why you need to call values().  just use a for loop.  
"""

word_freqs = {}

the_story = input('tell me a story: ')

for word in the_story.lower().split():
    if word in word_freqs:
        word_freqs[word] += 1
    else:
        word_freqs[word] = 1


print(word_freqs)

"""
    be careful with floats:
        roundoff error
        
"""

my_list = [1, 2, 3]
del my_list[0]
print(my_list)
