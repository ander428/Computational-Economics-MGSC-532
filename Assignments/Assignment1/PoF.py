import random

# creates deck of cards
def create_deck():
    values = [i + 2 for i in range(9)] + ["J", "Q", "K", "A"]
    suits = ['D', 'H', 'S', 'C']

    deck = []
    for s in suits:
        for v in values:
            deck.append((v, s))
    return deck

# deal random n cards
def deal(deck, n):
    return random.sample(deck, n)

# check if there is a pair in a hand
def have_pair(hand):
    unique_values = set([card[0] for card in hand]) # finds unique values in a hand
    return len(unique_values) == len(hand)-1

# convert face cards to a number value
def face2num(values):
    face_card_low = {'J': 11, 'Q': 12, 'K': 13, 'A': 1} # Ace is low
    face_card_high = {'J': 11, 'Q': 12, 'K': 13, 'A': 14} # Ace is high
    low_vals = []
    high_vals = []
    for val in values:
        # if value is a face card, add numeric to low and high hands
        # else apply the normal number value
        if val in face_card_low.keys():
            low_vals.append(face_card_low[val])
            high_vals.append(face_card_high[val])
        else:
            low_vals.append(val)
            high_vals.append(val)
    return (low_vals, high_vals)

# check if a hand is a straight
def have_straight(hand):
    # get the low and high variants of the hand
    # sort the hands
    values = [card[0] for card in hand]
    low, high = face2num(values)
    low.sort()
    high.sort()

    # if a hand sorted ascending has a difference of value > 1, not a straight
    isLowStraight = True
    isHighStraight = True
    for i in range(0, len(hand)-1):
        if low[i] != low[i+1]-1:
            isLowStraight = False
        if high[i] != high[i+1]-1:
            isHighStraight = False
    return isLowStraight or isHighStraight

# check if a hand is a flush
def have_flush(hand):
    # if there is only 1 unique suit, must be a flush
    unique_suits = set([card[1] for card in hand]) # get unique suits
    return len(unique_suits) == 1

deck = create_deck()
samples = 10000

successes = 0

for _ in range(samples):
    hand = deal(deck, 5)
    successes += 1 if have_flush(hand) and not have_straight(hand) else 0

print("Successes:", successes)
print("Samples:", samples)
print("Probability:",successes/samples)
