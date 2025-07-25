import pydealer 

#Build the Pyramid
def build_pyramid():
    deck = pydealer.Deck()
    deck.shuffle()

    pyramid = []
    total_rows = 5
    card_index = 0

    for row in range(1, total_rows + 1):
        pyramid_row = []
        for _ in range(row):
            pyramid_row.append(deck[card_index])
            card_index += 1
        pyramid.append(pyramid_row)

    return pyramid

#the Pyramid
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

#get points
def get_card_point(row_index):
    return row_index + 1

#track Points
player_points = {}

def update_points(player_name, row_index):
    points = get_card_point(row_index)
    player_points[player_name] = player_points.get(player_name, 0) + points

#coroutine for Game
def pyramid_game(pyramid):
    revealed = set()
    while True:
        row, col, player = yield
        if (row, col) in revealed:
            print("Card already revealed.")
            continue
        revealed.add((row, col))
        card = pyramid[row][col]
        update_points(player, row)
        print(f"\n{player} flipped {card} in row {row + 1} and got {get_card_point(row)} points.")
        display_pyramid(pyramid, revealed)
        print(f"\nCurrent Points: {player_points}\n")
