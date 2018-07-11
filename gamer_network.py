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
