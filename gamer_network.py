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

def extract_connections(data_line):
    flag = ' is connected to '
    if flag not in data_line:
        return False
    connections = data_line.split(flag)
    connected_to = connections.pop().split(', ')
    connections.append(connected_to)
    return connections

def extract_games(data_line):
    flag = ' likes to play '
    if flag not in data_line:
        return False
    games = data_line.split(flag)
    games_liked = games.pop().split(', ')
    games.append(games_liked)
    return games

def string_to_data(string):
    raw_lines = string.split('.')
    data_lines = []
    for line in raw_lines:
        if extract_connections(line):
            data_lines.append(extract_connections(line))
        elif extract_games(line):
            data_lines.append(extract_games(line))
    return data_lines
