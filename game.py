import random

# Define the deck of cards
suits = ('♥', '♦', '♣', '♠')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'J': 10, 'Q': 10, 'K': 10, 'A': 11}


# Define Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} {self.suit}"


class Deck:
    deck = None
    normalDeck = None

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]
        self.normalDeck = self.deck.copy()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.shownCards = []

    def add_card(self, card):
        self.cards.append(card)
        if len(self.cards) != 1:
            self.shownCards.append(card)

        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand, dealer):
    playing = True

    while playing:
        # win_lose_odds(deck, hand, dealer)
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck, hand)
            print("Pulled: {}".format(hand.cards[len(hand.cards) - 1]))
            hand.adjust_for_ace()
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")

        if hand.value > 21: return


    # def win_lose_odds(deck, player, dealer):
    #     win = 0
    #     lose = 0
    #
    #     # if player.value <= dealer.value: return
    #
    #     # deck including players hidden card
    #     deckWithHidden = (deck.deck + [x for x in dealer.cards if x not in dealer.shownCards])
    #
    #     for i in deckWithHidden:
    #
    #         possibleDealer = Hand()
    #         for g in dealer.shownCards:
    #             possibleDealer.add_card(g)
    #
    #         possibleDealer.add_card(i)
    #
    #         possibleDealer.adjust_for_ace()
    #
    #         if possibleDealer.value <= 21:
    #
    #             for j in deckWithHidden:
    #                 if j != i:
    #                     possiblyPlayer = Hand()
    #
    #                     for k in player.cards:
    #                         possiblyPlayer.add_card(k)
    #
    #                     possiblyPlayer.add_card(j)
    #                     possiblyPlayer.adjust_for_ace()
    #
    #                     if possiblyPlayer.value > 21 or possiblyPlayer.value <= possibleDealer.value:
    #                         lose += 1
    #                     else:
    #                         win += 1
    #
    #     print("Hit odds {}   Stand odds {}".format(win,lose))

    # print("Player current value: {}".format(player.value))
    # print("Dealer current value: {}".format(dealer.value))
    #
    # hit(deck, dealer)
    # hitCard = dealer.cards[len(dealer.cards) - 1]
    # print("Dealer hits a {}, value now: {}".format(hitCard, dealer.value))
    # quit()


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("———")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer):
    print("Player busts!")


def player_wins(player, dealer):
    print("Player wins!")


def dealer_busts(player, dealer):
    print("Dealer busts!")


def dealer_wins(player, dealer):
    print("Dealer wins!")


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


def play_blackjack():
    while True:
        # Print an opening statement
        print("Welcome to Blackjack!")

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        playing = True

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand, dealer_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break

        if player_hand.value <= 21:
            #
            # computer_calculator(deck, player_hand, dealer_hand)
            # quit()

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand)

            else:
                push(player_hand, dealer_hand)

            break


play_blackjack()
