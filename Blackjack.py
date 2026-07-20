import random

while True:
    cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,
             5,5,5,6,6,6,6,7,7,7,7,8,8,
             8,8,9,9,9,9,10,10,10,10,10,
             10,10,10,10,10,10,10,10,10,
             10,11,11,11,11]

    player_1 = []
    player_2 = []
    additional_player_cards = []
    total_player_cards = player_1 + player_2 + additional_player_cards
    dealer_1 = []
    dealer_2 = []


    player_1.append(random.choice(cards))
    cards.remove(player_1[0])


    player_2.append(random.choice(cards))
    cards.remove(player_2[0])

    dealer_1.append(random.choice(cards))
    cards.remove(dealer_1[0])


    dealer_2.append(random.choice(cards))
    cards.remove(dealer_2[0])


    def ace_logic(hand):
        aces = hand.count(11)
        total = sum(hand)
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    player_hands_played = 0
    player_busted = False
    player_got_blackjack = False

    while player_hands_played <11 :
        player_hand = player_1 + player_2 + additional_player_cards
        total_player_cards = ace_logic(player_hand)

        print(f"\n--- Player Turn ---")
        print(f"Your cards: {player_1} and {player_2} {additional_player_cards if additional_player_cards else ''}")
        print(f"Your total: {total_player_cards}")
        print(f"Dealer shows: {dealer_1} and a hidden card")

        if total_player_cards == 21:
            print("\nYou have a total of 21.")
            player_got_blackjack = True
            break

        if total_player_cards > 21:
            print("\nYou went over 21. The dealer wins.")
            player_busted = True
            break  

        player_choice = input("\nWould you like to hit or stay? ").lower()
        if player_choice == "hit" or player_choice == "h":
            additional_player_cards.append(random.choice(cards))
            cards.remove(additional_player_cards[-1])
            print(f"Drew a {additional_player_cards[-1]}.")
        
        if player_choice == "stay" or player_choice == "s":
            print(f"\nYou stay with a total of {total_player_cards}.")
            break

    # If the player didn't bust or hit 21 immediately, the dealer plays
    if not player_busted and not player_got_blackjack:
        player_hand = player_1 + player_2 + additional_player_cards
        total_player_cards = ace_logic(player_hand)

        print("")
        input("Press Enter to continue to the dealer's turn . . .")

        additional_dealer_cards = []
        dealer_hand= dealer_1 + dealer_2 + additional_dealer_cards
        dealer_total = ace_logic(dealer_hand)
        print("\n--- Dealer Turn ---")
        print(f"Dealer hidden card was {dealer_2}.")
        print(f"Dealer total: {dealer_total}")

        while dealer_total < 17:
            additional_dealer_cards.append(random.choice(cards))
            cards.remove(additional_dealer_cards[-1])
            dealer_hand= dealer_1 + dealer_2 + additional_dealer_cards
            dealer_total = ace_logic(dealer_hand)
            print(f"Dealer draws a {additional_dealer_cards[-1]}. New total: {dealer_total}")


        print("\n--- Match Result ---")
        if dealer_total > 21:
            print(f"Dealer went over 21 with a total of {dealer_total}. You win.")

        elif dealer_total == 21:
            print("Dealer has a total of 21. Dealer wins.")

        elif dealer_total == total_player_cards:
            print(f"Both totals are {dealer_total}. It's a tie.")
          
        elif dealer_total == 21 and total_player_cards == 21:
            print("Both sides have 21. It's a tie.")

        elif dealer_total > total_player_cards:
            print(f"Dealer has {dealer_total} and you have {total_player_cards}. Dealer wins.")

        elif dealer_total < total_player_cards:
            print(f"You have {total_player_cards} and the dealer has {dealer_total}. You win.")

    elif player_got_blackjack:
        print("\n--- Match Result ---")
        print("You win with 21.")

    # Play again prompt loop
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again != "yes" and play_again != "y":
        print("Thanks for playing.")
        break
