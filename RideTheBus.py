import pydealer
import random

# Global dictionary to track each player's points from Ride the Bus phase
player_points = {}

# Convert card rank to a number for comparisons
def rank_value(card):
    try:
        return int(card.value)
    except Exception:
        mapping = {"Ace": 1, "Jack": 11, "Queen": 12, "King": 13}
        s = str(card.value)
        if s.isdigit():
            return int(s)
        return mapping.get(s, 0)

# Input prompt: red or black
def ask_red_or_black():
    guess = input("Red or Black? ").strip().lower()
    return guess

# Input prompt: higher or lower than previous card
def ask_higher_or_lower(prev_card):
    guess = input(f"Higher or Lower than {prev_card}? ").strip().lower()
    return guess

# Input prompt: is the new card inside or outside of two previous cards
def ask_inside_or_outside(card1, card2):
    guess = input(f"Inside or Outside of {card1} and {card2}? ").strip().lower()
    return guess

# Input prompt: guess the suit
def ask_suit():
    guess = input("Guess the suit (Hearts, Diamonds, Clubs, Spades): ").strip().capitalize()
    return guess

# Add points to the player's score
def update_points(player_name, points):
    player_points[player_name] = player_points.get(player_name, 0) + points

# Main Ride the Bus logic for one player
def run_ride_the_bus(player_name, deck):
    print(f"\n{player_name} is now riding the bus!")

    card_history = []  
    index = 0          
    cards_used = 0     

    while cards_used < 14:
        card = deck.deal(1)[0]
        cards_used += 1

        # Stage 0: Red or Black
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

        # Stage 1: Higher or Lower than previous card
        elif index == 1:
            guess = ask_higher_or_lower(card_history[-1])
            correct = (rank_value(card) > rank_value(card_history[-1]) and guess == "higher") or \
                      (rank_value(card) < rank_value(card_history[-1]) and guess == "lower")
            if correct:
                print(f"Correct! It was {card}.")
                update_points(player_name, 2)
                card_history.append(card)
                index += 1
            else:
                print(f"Wrong! It was {card}. Returning to Red or Black with new card...")
                index = 0  # Restart

        # Stage 2: Inside or Outside the previous two cards
        elif index == 2:
            card1 = card_history[-2]
            card2 = card_history[-1]
            low = min(rank_value(card1), rank_value(card2))
            high = max(rank_value(card1), rank_value(card2))
            guess = ask_inside_or_outside(card1, card2)
            in_between = low < rank_value(card) < high
            correct = (in_between and guess == "inside") or (not in_between and guess == "outside")
            if correct:
                print(f"Correct! It was {card}.")
                update_points(player_name, 2)
                card_history.append(card)
                index += 1
            else:
                print(f"Wrong! It was {card}. Returning to Red or Black with new card...")
                index = 0  

        # Stage 3: Guess the exact suit
        elif index == 3:
            guess = ask_suit()
            if guess == card.suit:
                print(f"Correct! It was {card}. You win the Ride the Bus challenge!")
                update_points(player_name, 2)
            else:
                print(f"Wrong! It was {card}. Returning to Red or Black with new card...")
            index = 0  # Restart regardless

    print(f"\n{player_name}'s Ride the Bus phase is over after 14 cards.")
    print(f"{player_name}'s final score after Ride the Bus: {player_points[player_name]} points\n")

# Display everyone's final Ride the Bus scores
def display_final_scores():
    print("\n--- Final Scores ---")
    for player, points in player_points.items():
        print(f"{player}: {points} point(s)")

# Run Ride the Bus for each player in order
def ride_the_bus_for_all(players, deck):
    for player in players:
        run_ride_the_bus(player, deck)
