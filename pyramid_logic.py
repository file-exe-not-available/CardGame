import pydealer

def build_pyramid(deck):
    pyramid = []
    total_rows = 5
    for row in range(1, total_rows + 1):
        pyramid_row = [deck.deal(1)[0] for _ in range(row)]
        pyramid.append(pyramid_row)
    return pyramid

def display_pyramid(pyramid, revealed=None):
    if revealed is None:
        revealed = set()

    for i, row in enumerate(pyramid):
        indent = " " * (5 - i)
        display_row = []
        for j, card in enumerate(row):
            if (i, j) in revealed:
                display_row.append(str(card))
            else:
                display_row.append("XX")
        print(indent + "  ".join(display_row))

def get_card_point(row_index):
    return row_index + 1

def reveal_pyramid_and_score(pyramid, players, revealed, points):
    for i, row in enumerate(pyramid):
        for j, card in enumerate(row):
            print(f"\nRevealing card at row {i + 1}, column {j + 1}: {card}")
            revealed.add((i, j))
            display_pyramid(pyramid, revealed)

            for player_name, player_data in players.items():
                for player_card in player_data['hand']:
                    if player_card.value == card.value:
                        choice = input(f"{player_name}, you have {player_card}. Play it for {i + 1} point(s)? (y/n): ").lower()
                        if choice == 'y':
                            points[player_name] += (i + 1)
                            print(f"{player_name} earns {i + 1} point(s)!")
                            player_data['hand'].remove(player_card)
                            break  # Prevent double scoring for multiple identical cards

