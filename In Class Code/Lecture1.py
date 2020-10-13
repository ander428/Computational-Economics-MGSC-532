import random

def create_deck():
    values = [i + 2 for i in range(9)] + ["J", "Q", "K", "A"]
    suites = ['D', 'H', 'S', 'C']

    deck = []
    for s in suites:
        for v in values:
            deck.append((v, s))
    return deck

def deal(deck, n):
    return random.sample(deck, n)

def have_pair(hand):
    unique_values = set([card[0] for card in hand])
    return len(unique_values) == len(hand)-1

deck = create_deck()
samples = 10000

successes = 0

for _ in range(samples):
    hand = deal(deck, 5)
    successes += 1 if have_pair(hand) else 0

print(successes/samples)
