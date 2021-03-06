from gamer_network import *
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

print extract_data(connection_string, ' is connected to ')
print extract_data(game_string, ' is connected to ')
print extract_data(connection_string, ' likes to play ')
print extract_data(game_string, ' likes to play ')

string_john = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner."

#print string_to_data(string_john)

print create_data_structure(string_john)
print create_data_structure('')

network = create_data_structure('')
network = add_new_user(network, 'Alice', [])
network = add_new_user(network, 'Bob', [])
network = add_connection(network, 'Alice', 'Bob')
print network
print get_secondary_connections(network, 'Alice')

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
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures.\
George is connected to Robin.\
George likes to play Ninja Hamsters."

network = create_data_structure(example_input)

print network
''' >>>
{'John': {
'connections': ['Bryant', 'Debra', 'Walter'],
'games': ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']},
'Freda': {
'connections': ['Olive', 'John', 'Debra'],
'games': ['Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures']},
'Ollie': {
'connections': ['Mercedes', 'Freda', 'Bryant'],
'games': ['Call of Arms', 'Dwarves and Swords', 'The Movie: The Game']},
'Robin': {
'connections': ['Ollie'],
'games': ['Call of Arms', 'Dwarves and Swords']},
'Mercedes': {
'connections': ['Walter', 'Robin', 'Bryant'],
'games': ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']},
'Levi': {
'connections': ['Ollie', 'John', 'Walter'],
'games': ['The Legend of Corgi', 'Seven Schemers', 'City Comptroller: The Fiscal Dilemma']},
'Jennie': {
'connections': ['Levi', 'John', 'Freda', 'Robin'],
'games': ['Super Mushroom Man', 'Dinosaur Diner', 'Call of Arms']},
'Olive': {
'connections': ['John', 'Ollie'],
'games': ['The Legend of Corgi', 'Starfleet Commander']},
'Debra': {
'connections': ['Walter', 'Levi', 'Jennie', 'Robin'],
'games': ['Seven Schemers', 'Pirates in Java Island', 'Dwarves and Swords']},
'George': {
'connections': ['Robin'],
'games': ['Ninja Hamsters']},
'Bryant': {
'connections': ['Olive', 'Ollie', 'Freda', 'Mercedes'],
'games': ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']},
'Walter': {
'connections': ['John', 'Levi', 'Bryant'],
'games': ['Seahorse Adventures', 'Ninja Hamsters', 'Super Mushroom Man']}} '''

print get_connections(network, 'John')
print get_connections(network, 'Paul')
print get_games_liked(network, 'John')
print get_games_liked(network, 'Paul')

print get_secondary_connections(network, 'John')
print count_common_connections(network, 'John', 'Walter')
print count_common_connections(network, 'John', 'Paul')

print find_path_to_friend(network, 'John', 'Bryant')
print find_path_to_friend(network, 'John', 'Olive')
print find_path_to_friend(network, 'John', 'Freda')
print find_path_to_friend(network, 'John', 'Levi')
print find_path_to_friend(network, 'Robin', 'George')

print most_liked_game(network)
