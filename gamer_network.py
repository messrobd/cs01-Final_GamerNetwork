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
    user = data.pop()
    return user, attribute

def string_to_data(string):
    raw_lines = string.split('.')
    data_lines = []
    for line in raw_lines:
        data = extract_data(line, ' is connected to ') or extract_data(line, ' likes to play ')
        if data:
            data_lines.append(data)
    return data_lines
