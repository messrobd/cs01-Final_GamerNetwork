from gamer_network import add_new_user, add_connection, string_to_data, extract_connections, extract_games
'''
network = {}
network_with_john = {
  'John': {}
}
network_with_beatles = {
  'John': {},
  'Paul': {},
  'George': {},
  'Ringo': {}
}

network_with_connection = {
  'John': {
    'connections': ['Paul']
  },
  'Paul': {},
  'George': {},
  'Ringo': {}
}

user_A = 'John'
user_B = 'Paul'

print add_new_user(network, 'John', ['Pokemon'])
print add_new_user(network_with_john, 'John', ['Pokemon'])
print add_connection(network, user_A, user_B)
print add_connection(network_with_beatles, user_A, user_B)
print add_connection(network_with_connection, user_A, user_B)
'''
connection_string = "John is connected to Bryant, Debra, Walter."
game_string = "John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner."

print extract_connections(connection_string)
print extract_connections(game_string)
print extract_games(connection_string)
print extract_games(game_string)

string_john = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner."

print string_to_data(string_john)

example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."
