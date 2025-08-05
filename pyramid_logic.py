import pydealer

#Build pyramid
def build_pyramid(deck):
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

#Reveal cards from bottom to top
def reveal_pyramid_and_score(pyramid, players, revealed_cards, player_points):
    print("\n--- Pyramid Phase ---")
    total_rows = len(pyramid)

    for player in players:
        print(f"\n{player}'s turn:")
        score = 0
        revealed = set()

        for row_index in reversed(range(total_rows)):
            row = pyramid[row_index]
            for col_index, card in enumerate(row):
                revealed.add((row_index, col_index))

                # Top row = 5 pts, bottom row = 1 pt
                points = total_rows - row_index

                score += points
                print(f"{player} flipped {card} from row {row_index + 1} and earned {points} point(s).")
                print(f"Current Score: {score}\n")
                display_pyramid(pyramid, revealed)
                print()

                choice = input("Keep going? (y/n): ").strip().lower()
                if choice != 'y':
                    print(f"{player} stopped with {score} points.")
                    player_points[player] = score
                    revealed_cards[player] = revealed
                    break
            else:
                continue
            break  

        # If finished all cards
        if (row_index, col_index) == (0, 0):
            print(f"{player} finished the pyramid! Total: {score}")
            player_points[player] = score
            revealed_cards[player] = revealed

#Display pyramid with XX for hidden and card text for revealed
def display_pyramid(pyramid, revealed):
    for i, row in enumerate(pyramid):
        indent = " " * (5 - i)
        display_row = []
        for j, card in enumerate(row):
            if (i, j) in revealed:
                display_row.append(str(card))
            else:
                display_row.append("XX")
        print(indent + "  ".join(display_row))
        #checking
