# This program simulates a simple 5-card poker game. It deals a hand, lets the player choose cards to replace, and shows the final hand.

# Import random
import random

# Define the Card class to represent individual playing cards
class Card:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']

    # Initialize the card with suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Define a custom method to display the card as a string
    def display(self):
        return f'{Card.ranks[self.rank]} of {Card.suits[self.suit]}'

# Define the Deck class to represent a standard 52-card deck
class Deck:
    def __init__(self):
        # Create all 52 cards and shuffle them
        self.cards = [Card(s, r) for s in range(4) for r in range(1, 14)]
        random.shuffle(self.cards)

    # Deal a specific number of cards from the deck
    def deal(self, num):
        return [self.cards.pop() for _ in range(num)]

# Define the main poker game logic
def play_poker():
    # Create and shuffle a new deck
    deck = Deck()

    # Deal 5 cards to form the player's hand
    hand = deck.deal(5)

    # Display the initial hand
    print("You were dealt:")
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card.display()}")

    # Prompt the user to select cards to replace
    to_replace = input("\nEnter card numbers to replace (e.g., 2 4), or press Enter to keep all: ")

    if to_replace.strip():
        try:
            # Convert input into a list of valid indices (0-based)
            indices = sorted(set(int(x) - 1 for x in to_replace.split() if 0 < int(x) <= 5))

            # Replace the selected cards with new ones from the deck
            for i in indices:
                hand[i] = deck.deal(1)[0]
        except ValueError:
            # Handle invalid input gracefully
            print("Invalid input. No cards were replaced.")

    # Display the final hand after replacements
    print("\nYour final hand:")
    for card in hand:
        print(card.display())

# Run the poker game
if __name__ == "__main__":
    play_poker()
