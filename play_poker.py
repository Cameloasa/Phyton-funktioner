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


def evaluate_combinations(numeric_values, suits):
    is_flush = len(set(suits)) == 1
    is_straight = numeric_values == list(range(numeric_values[0], numeric_values[0] + 5))

    # Bygg en dictionary för att räkna förekomster av varje värde
    value_counts = {}
    for value in numeric_values:
        value_counts[value] = value_counts.get(value, 0) + 1

    counts = list(value_counts.values())

    # Utvärdera handens styrka
    if is_flush and is_straight:
        return "Straight Flush"
    elif 4 in counts:
        return "Four of a Kind"
    elif 3 in counts and 2 in counts:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif 3 in counts:
        return "Three of a Kind"
    elif counts.count(2) == 2:
        return "Two Pair"
    elif 2 in counts:
        return "One Pair"
    else:
        return f"High Card: {max(numeric_values)}"


def evaluate_hand(hand):
    # Extrahera värden och färger
    values = [card[:-1] for card in hand]
    suits = [card[-1] for card in hand]

    # Mappning av symboliska värden till numeriska
    value_map = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    # Omvandla värdena till nummer
    numeric_values = []
    for value in values:
        numeric_value = value_map.get(value, value)  # Använd mappning om det finns, annars behåll värdet
        numeric_values.append(int(numeric_value))

    numeric_values.sort()  # Sortera värdena

    # Anropa evaluate_combinations för att utvärdera handens styrka
    return evaluate_combinations(numeric_values, suits)


# Testa funktionerna
player_hand = deal_hand(deck,5)
computer_hand = deal_hand(deck,5)

print_hand(player_hand,"Cami")
print_hand(player_hand,"Computer")








