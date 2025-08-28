import itertools
import random

def build_deck():
    ranks = list(range(1, 14))
    suits = ['Spade', 'Heart', 'Diamond', 'Club']
    return list(itertools.product(ranks, suits))

def shuffle_deck(deck):
    random.shuffle(deck)

def draw_cards(deck, count=5):
    print("You got:")
    for card, suit in deck[:count]:
        print(f"{card} of {suit}")

if __name__ == "__main__":
    deck = build_deck()
    shuffle_deck(deck)
    draw_cards(deck, 5)
