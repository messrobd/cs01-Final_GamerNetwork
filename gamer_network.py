def add_new_user(network, user, games):
    if user not in network:
        network[user] = {
          'games': games
        }
    return network

def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network:
        if 'connections' not in network[user_A]:
            network[user_A]['connections'] = []
        if user_B not in network[user_A]['connections']:
            network[user_A]['connections'].append(user_B)
        return network
    else:
        return False

def extract_data(data_line, flag):
    if flag not in data_line:
        return False
    data = data_line.split(flag)
    attribute = data.pop().split(', ')
    data.append(attribute)
    return data

def string_to_data(string):
    raw_lines = string.split('.')
    data_lines = []
    for line in raw_lines:
        data = extract_data(line, ' is connected to ') or extract_data(line, ' likes to play ')
        if data:
            data_lines.append(data)
    return data_lines

def create_data_structure(string_input):
    raw_lines = string_input.split('.')
    user_data = {}
    connections_data = []
    while raw_lines:
        line = raw_lines.pop()
        new_user = extract_data(line, ' likes to play ')
        if new_user:
            add_new_user(user_data, new_user[0], new_user[1])
        else:
            connections_data.append(line)
    while connections_data:
        line = connections_data.pop()
        connections = extract_data(line, ' is connected to ')
        if connections:
            user_A = connections[0]
            for user_B in connections[1]:
                add_connection(user_data, user_A, user_B)
    return user_data

def get_connections(network, user):
    if user not in network:
        return None
    if 'connections' not in network[user]:
        return []
    return network[user]['connections']

def get_games_liked(network, user):
    if user not in network:
        return None
    if 'games' not in network[user]:
        return []
    return network[user]['games']

def get_secondary_connections(network, user):
    if user not in network:
        return None
    if 'connections' not in network[user]:
        return []
    secondary_connections = []
    for connection in network[user]['connections']:
        secondary_connections += network[connection]['connections']
    return secondary_connections

def count_common_connections(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    common_connections = 0
    if 'connections' in network[user_A] and 'connections' in network[user_B]:
        connections_A = network[user_A]['connections']
        connections_B = network[user_B]['connections']
        for connection in connections_A:
            if connection in connections_B:
                common_connections += 1
    return common_connections

'''
find path to friend

return a list of connections starting with user_A and ending with user_B.
return None if no path is found, or if one of the users is not in the network.

connection ==> user_B
connection ==> user_A
connection ==> connection(user_B) '''

def find_path_to_friend(network, user_A, user_B, visited=[]):
    if user_A not in network or user_B not in network:
        return None
    if user_B in network[user_A]['connections']:
        return [user_A, user_B]
    if user_A in visited:
        return None
    else:
        visited.append(user_A)
    path = [user_A]
    for connection in network[user_A]['connections']:
        target_user = find_path_to_friend(network, connection, user_B)
        if target_user != None and user_B in target_user:
            del visited[:]
            return path + target_user
