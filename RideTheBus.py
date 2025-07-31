def ride_the_bus_for_all(players, deck):
    print("\n--- Ride the Bus Phase Begins ---\n")

    for player in players:
        print(f"\n{player} is now riding the bus!")
        bus_cards = deck.deal(14)
        print("Cards for this ride:")
        print(', '.join(str(card) for card in bus_cards))

        stage = 1
        index = 0
        first_card = None
        second_card = None

        max_stage_reached = 1
        failed_attempts = 0

        while index < len(bus_cards):
            card = bus_cards[index]
            print(f"\nCard #{index + 1}: {card}")

            if stage == 1:
                guess = input(f"{player}, Red or Black? ").lower()
                actual = 'red' if card.suit in ['Hearts', 'Diamonds'] else 'black'
                if guess == actual:
                    print("Correct!")
                    first_card = card
                    stage += 1
                    max_stage_reached = max(max_stage_reached, stage)
                else:
                    print(f"Wrong! It was {card}. Restarting from card #{index + 2}...")
                    failed_attempts += 1
                    stage = 1
                    index += 1

            elif stage == 2:
                guess = input(f"{player}, Higher or Lower than {first_card}? ").lower()
                if (guess == 'higher' and card.value > first_card.value) or \
                   (guess == 'lower' and card.value < first_card.value):
                    print("Correct!")
                    second_card = card
                    stage += 1
                    max_stage_reached = max(max_stage_reached, stage)
                else:
                    print(f"Wrong! It was {card}. Restarting from card #{index + 2}...")
                    failed_attempts += 1
                    stage = 1
                    index += 1

            elif stage == 3:
                guess = input(f"{player}, In-between or Outside of {first_card} and {second_card}? ").lower()
                low, high = sorted([first_card.value, second_card.value])
                in_between = low < card.value < high
                if (guess == 'in-between' and in_between) or (guess == 'outside' and not in_between):
                    print("Correct!")
                    stage += 1
                    max_stage_reached = max(max_stage_reached, stage)
                else:
                    print(f"Wrong! It was {card}. Restarting from card #{index + 2}...")
                    failed_attempts += 1
                    stage = 1
                    index += 1

            elif stage == 4:
                guess = input(f"{player}, Guess the suit: ").capitalize()
                if card.suit == guess:
                    print(f"Correct! {player} completed the bus ride!")
                    break
                else:
                    print(f"Wrong! It was {card}. Restarting from card #{index + 2}...")
                    failed_attempts += 1
                    stage = 1
                    index += 1

        else:
            print(f"{player} could not complete the bus ride.")

        print(f"\nSummary for {player}:")
        print(f"- Max Stage Reached: {max_stage_reached}/4")
        print(f"- Failed Attempts: {failed_attempts}")
        print("-" * 30)
