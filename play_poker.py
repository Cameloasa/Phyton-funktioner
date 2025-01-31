import random

#Skapa en kortlek med 52 kort (valörer + färger)
def create_deck():

    suits = ["♠️", "♣️", "♥️", "♦️"]  # Ruter Klöver Hjärter Spader
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]  # 2-10 + figurer
    deck = [f"{value}{suit}" for suit in suits for value in values]  # List comprehension
    return deck

# print(create_deck())

# 2. Slumpa ett spelkort
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

deck = create_deck()
shuffled_deck = shuffle_deck(deck)

#print("Första handen: " , create_deck())
#print("Random kort: ", shuffled_deck)

print("Första handen: " , create_deck() [:5])
print("Random kort: ", shuffled_deck [:5])

# Dela cort from kortleken
def deal_hand(deck, num_cards):
    hand = deck[:num_cards]
    del deck[:num_cards]
    return hand

player_hand = deal_hand(deck,5)
computer_hand = deal_hand(deck,5)

print("Dina kort",player_hand)
print("Mina kort", computer_hand)

#Visa korten
def print_hand(hand, player_name):
    print(f"{player_name} har följande kort: {''.join(hand)}")

print_hand(player_hand,"Cami")
print_hand(player_hand,"Computer")










