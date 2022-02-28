"""
    remove removes by value,
        it searches for the first time you see the value in the list, then it removes it
        shifts everything else back by one.

        It only removes the first occurrence of the value, doesn't remove all
        It gives a value error when the value isn't in the list, you should use the in keyword

"""

a_list = [1, 2, 3, 4, 5, 3, 3, 3]

a_list.remove(3)
print(a_list)

# what if we remove an element which is not in the list?
# it gives a ValueError, which is bad
# how can we avoid that?
the_number = int(input('Tell me what to remove? '))
if the_number in a_list:
    a_list.remove(the_number)
else:
    print(f'{the_number} was not in the list')

print(a_list)


new_list = [1, 2, 4, 5, 7, 4, 3, 2, 5, 6, 8, 4]
"""
for i in range(len(new_list)):
    print(new_list[i], new_list)
    if new_list[i] % 2 == 0:
        new_list.remove(new_list[i])
        
It shifts indices while it's executing this for loop, sometimes it jumps over elements
    sometimes it gets to the end of the list and doesnt know it 
    
    for each loops will fix the issue with IndexErrors, but still won't fix the jump issue.
"""

for x in new_list:
    if x % 2 == 0:
        new_list.remove(x)
print(new_list)


even_newer_list = []
for x in new_list:
    if x % 2 == 1:
        even_newer_list.append(x)
print(even_newer_list)