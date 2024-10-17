import random
import itertools

# Create a deck of cards
deck = list(itertools.product(range(1, 14), ["Spade", "Club", "Hearts", "Diamond"]))

# Shuffle the deck
random.shuffle(deck)

print(deck)

# Print the first 5 cards from the shuffled deck
for i in range(5):
    print(deck[i][0], "of", deck[i][1])
