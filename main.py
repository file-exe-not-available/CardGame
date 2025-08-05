import pydealer
import CardDistribution
import pyramid_logic as pyramid
import RideTheBus

if __name__ == "__main__":
    deck = pydealer.Deck()
    deck.shuffle()

    players = CardDistribution.setup_players()
    CardDistribution.deal_initial_cards(deck, players)
    CardDistribution.display_player_hands(players)

    revealed_cards = {}     
    player_points = {}      

    # Pyramid Phase
    pyramid_cards = pyramid.build_pyramid(deck)
    pyramid.reveal_pyramid_and_score(pyramid_cards, players, revealed_cards, player_points)

    # Display final scores
    print("\n--- Final Scores After Pyramid ---")
    CardDistribution.display_points(players)

    # Ride the Bus Phase (every player)
    RideTheBus.ride_the_bus_for_all(players, deck)
    print("\n--- Final Scores After Ride the Bus ---")
    CardDistribution.display_points(players)
    print("\n--- Game Over! ---")
    print("Thanks for playing!")