import pydealer

def setup_players():
    num_players = int(input("Enter number of players: "))
    players = {}
    for i in range(num_players):
        name = input(f"Enter name for player {i + 1}: ")
        players[name] = {"hand": [], "points": 0}
    return players

def deal_initial_cards(deck, players):
    for _ in range(4):
        for player in players:
            card = deck.deal(1)[0]
            players[player]["hand"].append(card)

def display_player_hands(players):
    print("\n--- Players' Hands ---")
    for player, data in players.items():
        print(f"{player}: {', '.join(map(str, data['hand']))}")

def award_point_if_correct(players, player_name, is_correct):
    if is_correct:
        players[player_name]["points"] += 1

def display_points(players):
    print("\n--- Current Points ---")
    for player, data in players.items():
        print(f"{player}: {data['points']} point(s)")
