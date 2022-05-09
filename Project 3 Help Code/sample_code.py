"""
    Subway/Metro Network
    
    Goal: be able to find a path from the start of a train ride to the end.
        [if it exists]
        
    We have to track where we've been.
    
    We have to figure out a way to "represent" the network.

        [Hint: Dictionaries]

        "Design our data format"

    locations = {
        "loc1": ["dest1", "dest2", "dest3", "dest4"],
        "loc2": ["dest3", "dest5", "dest7"],
        
    }
"""


def find_path(locations, current, end_location, visited):
    print(f'finding {end_location}, current = {current}')
    if current == end_location:
        return [end_location]
    
    visited[current] = True
    
    for new_place in locations[current]:
        if new_place not in visited:
            trip_plan = find_path(locations, new_place, end_location, visited)
            if trip_plan:
                return [current] + trip_plan
    return []


def find_path_other(locations, current, end_location):
    print(f'finding {end_location}, current = {current}')
    if current == end_location:
        return [end_location]
    
    locations[current]['visited'] = True
    
    for new_place in locations[current]['connections']:
        if not locations[new_place]['visited']:
            trip_plan = find_path_other(locations, new_place, end_location)
            if trip_plan:
                return [current] + trip_plan
    return []


def add_path_helper(locations, split_command):
    loc_1 = split_command[1]
    loc_2 = split_command[2]
    locations[loc_1]['connections'].append(loc_2)
    locations[loc_2]['connections'].append(loc_1)
    

def reset_visited(locations):
    for place in locations:
        locations[place]['visited'] = False

def run_program():
    locations = {}
    
    command = input('>>> ')
    while command != 'quit':
        split_command = command.split()
        if not split_command:
            pass
        elif split_command[0] == 'add-location' and len(split_command) == 2:
            locations[split_command[1]] = {'connections': [], 'visited': False}
        elif split_command[0] == 'add-path' and len(split_command) == 3:
            add_path_helper(locations, split_command)
        elif split_command[0] == 'find-path' and len(split_command) == 3:
            loc_1 = split_command[1]
            loc_2 = split_command[2]
            visited = {}
            reset_visited(locations)
            print(find_path_other(locations, loc_1, loc_2))
        print(locations)
        
        command = input('>>> ')


run_program()
