"""
Spelet 21
Om man lägger ihop talen 1 + 2 + 3 + 4 + …
så kommer talens summa att bli större och större.
Förr eller senare kommer man förbi 21.
Skriv en funktion som skriver ut det första talet i talserien som är större än 21.
"""

def find_first_number():
    number_list = []
    sum = 0
    number = 1
    while sum <= 21:
        number_list.append(number)
        sum += number
        number += 1
    return number - 1  # Returnera det första talet som gjorde att summan översteg 21

# Anropa funktionen och skriv ut resultatet
first_number = find_first_number()
print(f"Det första talet i talserien som summan är större än 21 är: {first_number}")

"""
Version 2: i stället för att använda talserien,
slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
Tips: importera modulen random och använd funktionen randint för att slumpa tal.
Exempel: card = random.randint(1, 13)
"""
import random

def play_21():
    sum = 0
    while sum <= 21:
        card = random.randint(1,13)
        sum += card

        print(f"Du drog ett kort: {card}. Summan är nu: {sum}")

        if sum > 21:
            return  print("Du har över 21! Förlorare!")
        if sum == 21:
            return print("Du vann!")

play_21()

"""
Möjlig vidareutveckling:
bygg ett spel som frågar användaren om man vill ta ett nytt kort eller stanna.
(slumpa ett tal) Gör så att datorn kan simulera en motståndare. Målet är att vinna över datorn.
"""

print("Välkommen till Phyton 21 spel!")
def play_21_against_computer():
    player_sum = 0
    computer_sum = 0
    face_cards = [10, 11, 12, 13] #["J", "A", "Q", "K"]


    # Spelarens tur
    while player_sum <= 21:
        print(f"Din summa: {player_sum}")
        choice = input("Vill du ta ett kort till (j/n)? ")

        if choice.lower() == 'j':
            card = random.randint(2, 14)

            if card in face_cards: # J, Q, K räknas som 10
                card_value = 10
            else:
                card_value = card
            player_sum += card_value
            print(f"Du drog ett kort: {card}. Din summa är nu: {player_sum}")
        elif choice.lower() == 'n':
            break  # Spelaren väljer att stanna
        else:
            print("Ogiltigt val. Välj 'j' eller 'n'.")

    # Datorns tur
    while computer_sum  < 17:  # Datorn drar kort tills den når 17 eller mer
        card = random.randint(2, 14)
        if card in face_cards:  # J, Q, K räknas som 10
            card_value = 10
        else:
            card_value = card
        computer_sum += card_value
        print(f"Datorn drog ett kort: {card}. Datorns summa är nu: {computer_sum }")

    # Resultat
    print("\n--- Resultat ---")
    print(f"Din summa: {player_sum}")
    print(f"Datorns summa: {computer_sum }")

    if player_sum > 21 and computer_sum > 21:
        print("Båda förlorade!")
    elif player_sum > 21:
        print("Du förlorade! Datorn vann.")
    elif computer_sum > 21:
        print("Du vann! Datorn förlorade.")
    elif player_sum > computer_sum :
        print("Du vann!")
    elif player_sum < computer_sum :
        print("Datorn vann!")
    else:
        print("Det blev lika!")

# Starta spelet
play_21_against_computer()


