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
