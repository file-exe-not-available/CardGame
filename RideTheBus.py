import pydealer
import random

player_points = {}  # Ensure this is accessible or passed in if stored elsewhere

def ask_red_or_black():
    guess = input("Red or Black? ").strip().lower()
    return guess

def ask_higher_or_lower(prev_card):
    guess = input(f"Higher or Lower than {prev_card}? ").strip().lower()
    return guess

def ask_inside_or_outside(card1, card2):
    guess = input(f"Inside or Outside of {card1} and {card2}? ").strip().lower()
    return guess

def ask_suit():
    guess = input("Guess the suit (Hearts, Diamonds, Clubs, Spades): ").strip().capitalize()
    return guess

def update_points(player_name, points):
    player_points[player_name] = player_points.get(player_name, 0) + points

def run_ride_the_bus(player_name, deck):
    print(f"\n{player_name} is now riding the bus!")

    card_history = []
    index = 0  # Tracks the current stage (0 to 3)
    cards_used = 0  # Counts how many cards have been dealt in this phase

    while cards_used < 14:
        card = deck.deal(1)[0]
        cards_used += 1

        if index == 0:
            guess = ask_red_or_black()
            is_red = card.suit in ["Hearts", "Diamonds"]
            correct = (is_red and guess == "red") or (not is_red and guess == "black")
            if correct:
                print(f"Correct! It was {card}.")
                update_points(player_name, 2)
                card_history.append(card)
                index += 1
            else:
                print(f"Wrong! It was {card}. Try again with a new card...")

        elif index == 1:
            guess = ask_higher_or_lower(card_history[-1])
            correct = (card.value > card_history[-1].value and guess == "higher") or \
                      (card.value < card_history[-1].value and guess == "lower")
            if correct:
                print(f"Correct! It was {card}.")
                update_points(player_name, 2)
                card_history.append(card)
                index += 1
            else:
                print(f"Wrong! It was {card}. Returning to Red or Black with new card...")
                index = 0

        elif index == 2:
            card1 = card_history[-2]
            card2 = card_history[-1]
            low = min(card1.value, card2.value)
            high = max(card1.value, card2.value)
            guess = ask_inside_or_outside(card1, card2)
            correct = (low < card.value < high and guess == "inside") or \
                      (not (low < card.value < high) and guess == "outside")
            if correct:
                print(f"Correct! It was {card}.")
                update_points(player_name, 2)
                card_history.append(card)
                index += 1
            else:
                print(f"Wrong! It was {card}. Returning to Red or Black with new card...")
                index = 0

        elif index == 3:
            guess = ask_suit()
            if guess == card.suit:
                print(f"Correct! It was {card}. You win the Ride the Bus challenge!")
                update_points(player_name, 2)
            else:
                print(f"Wrong! It was {card}. Returning to Red or Black with new card...")
            index = 0

    print(f"\n{player_name}'s Ride the Bus phase is over after 14 cards.")
    print(f"{player_name}'s final score after Ride the Bus: {player_points[player_name]} points\n")

def display_final_scores():
    print("\n--- Final Scores ---")
    for player, points in player_points.items():
        print(f"{player}: {points} point(s)")

def ride_the_bus_for_all(players, deck):
    for player in players:
        run_ride_the_bus(player, deck)