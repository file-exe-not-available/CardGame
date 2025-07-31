import pydealer
import random

# Get number of players and their names
def setup_players():
    num_players = int(input("Enter number of players: "))
    players = {}
    for i in range(num_players):
        name = input(f"Enter name for player {i + 1}: ")
        players[name] = {"hand": [], "points": 0}
    return players

# Deal 4 cards to each player
def deal_initial_cards(deck, players):
    for _ in range(4):
        for player in players:
            card = deck.deal(1)[0]
            players[player]["hand"].append(card)

# Modify points logic for correct guesses (guess result is passed externally)
def award_point_if_correct(players, player_name, is_correct):
    if is_correct:
        players[player_name]["points"] += 1

# Updated display for player hands
def display_player_hands(players):
    for player, data in players.items():
        print(f"{player}'s hand: {', '.join(map(str, data['hand']))}")
