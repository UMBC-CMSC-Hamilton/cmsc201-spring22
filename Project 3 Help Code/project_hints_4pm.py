"""
    1) Visited lists..
    2) Visited Dictionaries
    3) Add visited into the station data <--
    

"""

def find_path(locations, current, destination, current_line, visited):
    
    print(f'finding {destination}, current = {current}')
    if current == destination:
        return [destination]
    
    if current in visited:
        return []
    
    visited[current] = True
    # if you can get this working you're 75% on the way.
    

    # hint1: you can check in the new_place[1] == current_line
    # hint2: run this loop twice
    for new_place in locations[current]:
        # if you find a way to get to the answer, return that
        # otherwise keep going and searching more.
        the_path = find_path(locations, new_place[0], destination, current_line, visited)
        if the_path:
            return [current] + the_path

    # second time you'd have to modify current_line to be something else...
    # we looked everywhere we promise there's no where left to go
    return []


def find_path_intrinsic(locations, current, destination, current_line):
    print(f'finding {destination}, current = {current}')
    if current == destination:
        return [destination]
    
    if locations[current]['visited']:
        return False
    
    locations[current]['visited'] = True
    # if you can get this working you're 75% on the way.
    
    # hint1: you can check in the new_place[1] == current_line
    # hint2: run this loop twice
    for new_place in locations[current]['connections']:
        # if you find a way to get to the answer, return that
        # otherwise keep going and searching more.
        the_path = find_path_intrinsic(locations, new_place[0], destination, current_line)
        if the_path:
            return [current] + the_path
    
    # second time you'd have to modify current_line to be something else...
    # we looked everywhere we promise there's no where left to go
    return []


def reset_visited(locations):
    for location in locations:
        locations[location]['visited'] = False


def run_program():
    locations = {}
    
    command = input('>>> ')
    while command != 'quit':
        split_command = command.split()
        if not split_command:
            pass
        elif split_command[0] == 'add-location' and len(split_command) == 2:
            name_of_location = split_command[1]
            locations[name_of_location] = {'connections': [], 'visited': False}
        elif split_command[0] == 'add-connection' and len(split_command) == 4:
            location_1 = split_command[1]
            location_2 = split_command[2]
            line_name = split_command[3]
            locations[location_1]['connections'].append([location_2, line_name])
            locations[location_2]['connections'].append([location_1, line_name])
        elif split_command[0] == 'find-path' and len(split_command) == 3:
            start_location = split_command[1]
            end_location = split_command[2]
            # visited = {}
            print(find_path_intrinsic(locations, start_location, end_location, ''))
            reset_visited(locations)
        print(locations)
        command = input('>>> ')

run_program()