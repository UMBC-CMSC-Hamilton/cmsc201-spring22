"""
    What is a while loop?

        a for loop iterates over some kind of range object, or items in a list
            "next thing" or we're at the end

        A while loop is different in the sense that it's more an if statement on repeat.

"""

s = input(':? ')
while s != 'stop':
    s = input(':? ')


i = 0
while i < 10:
    print('in the while loop', i)
    # i = i + 1
    i += 1
print('after the while loop', i)


"""

    Infinite loop
        with a while loop to get an infinite loop the most common issues are:
            1) not updating the variables that are checked
            2) update the variables so that they are always true again
            3) check the logic of the loop
                
"""
my_choice = int(input('Enter an integer between 1 and 5'))
while my_choice < 1 or my_choice > 5:
    print(my_choice, 'is invalid please retry between 1 and 5')
    my_choice = int(input('Enter an integer between 1 and 5'))

"""
    Why do you need while loops?
        for loops run a specific number of times
        a while loop runs as many times as you want, until you give it some stop condition
"""

the_list = []
for i in range(3):
    the_list.append(input('Tell me element: '))

"""
    Want instead is to let the user determine when the list is done
"""

favorite_foods = []
food = input('Tell me a favorite food (or terminate): ')
# priming the input
while food != 'terminate':
    favorite_foods.append(food)
    food = input('Tell me a favorite food (or terminate): ')


"""
     Reasons for while loops:
        1) give the user the opportunity to enter as many elements as they want to a list
        2) game loops, while not check_mate()
        3) prime use (80% of the while loops) check user input
        4) Modern server and GUI applications (not in this class) 
"""

"""
while True:
    print('hi')

How do you get out? break, what is that? no don't tell me, .. .it's banned.

    continue... also banned
"""


"""
while not exit_1 and not exit_2:
    # pass is legal
    # it doesn't do anything, but it does placehold that tab level, so that's why it exists
    pass
"""

# nested while loop
s = input('continue?')
while s == 'yes':
    x = 1
    y = int (input('Tell me a number'))

    while x < y:
        print(x)
        x = x * 2
        # x *= 2
    print(f'The power of two greater than or equal to {y} is', x)

    s = input('continue?')

"""
    Sentinel / Sentinel Value
        an input that will tell the loop to terminate.
        sentinel - watchman (someone who looks out for something)
        "stop", "terminate", -1
"""

if __name__ == '__main__':
    # your code here
    pass
