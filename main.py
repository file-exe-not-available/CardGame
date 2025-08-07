import pydealer
import CardDistribution
import pyramid_logic as pyramid
import RideTheBus

if __name__ == "__main__":
    #Create shuffled deck
    deck = pydealer.Deck()
    deck.shuffle()

    players = CardDistribution.setup_players()

    # Deal cards to each player
    CardDistribution.deal_initial_cards(deck, players)

    # Show what cards each player got
    CardDistribution.display_player_hands(players)

    revealed_cards = {}

    # Keep track of each player’s pyramid score
    player_points = {}

    #Pyramid Phase
    pyramid_cards = pyramid.build_pyramid(deck)

    # Let each player flip pyramid cards from bottom to top, scoring points
    pyramid.reveal_pyramid_and_score(pyramid_cards, players, revealed_cards, player_points)

    # Show everyone's points after pyramid phase
    print("\n--- Final Scores After Pyramid ---")
    CardDistribution.display_points(players)

    #RIDE THE BUS PHASE
    RideTheBus.ride_the_bus_for_all(players, deck)

    # Final scores after full game
    print("\n--- Final Scores After Ride the Bus ---")
    CardDistribution.display_points(players)

    print("\n--- Game Over! ---")
    print("Thanks for playing!")
