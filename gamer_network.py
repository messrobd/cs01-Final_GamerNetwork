def add_new_user(network, user, games):
    if user not in network:
        network[user] = {
          'games': games
        }
    return network
