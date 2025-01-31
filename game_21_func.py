import random


def print_welcome_message():
    print("Välkommen till Python 21 spel!")


def draw_card():
    card = random.randint(2, 14)
    return 10 if card >= 10 else card


def player_turn():
    player_sum = draw_card()  # Spelaren drar alltid minst ett kort
    print(f"Första kortet är: {player_sum}")

    while player_sum <= 21:
        choice = input("Vill du ta ett kort till (j/n)? ").lower()

        if choice == 'j':
            card_value = draw_card()
            player_sum += card_value
            print(f"Du drog ett kort: {card_value}. Din summa är nu: {player_sum}")
        elif choice == 'n':
            print("Du valde att stå.")
            break
        else:
            print("Ogiltigt val. Välj 'j' eller 'n'.")
    return player_sum


def computer_turn():
    computer_sum = 0
    print("\nDatorns tur...")

    while computer_sum < 19:
        card_value = draw_card()
        computer_sum += card_value
        print(f"Datorn drog ett kort: {card_value}. Datorns summa är nu: {computer_sum}")

    return computer_sum


def determine_winner(player_sum, computer_sum):
    print("\n--- Resultat ---")
    print(f"Din summa: {player_sum}")
    print(f"Datorns summa: {computer_sum}")

    if player_sum > 21 and computer_sum > 21:
        print("Båda förlorade!")
    elif player_sum > 21:
        print("Du förlorade! Datorn vann.")
    elif computer_sum > 21:
        print("Du vann! Datorn förlorade.")
    elif player_sum > computer_sum:
        print("Du vann!")
    elif player_sum < computer_sum:
        print("Datorn vann!")
    else:
        print("Det blev lika!")


def play_21_against_computer():
    print_welcome_message()

    player_sum = player_turn()  # Nu måste spelaren alltid dra minst ett kort

    if player_sum <= 21:
        computer_sum = computer_turn()
        determine_winner(player_sum, computer_sum)
    else:
        print("\nDu förlorade! Datorn vann per default.")


def main():
    while True:
        play_21_against_computer()
        again = input("Vill du spela igen (j/n)? ").lower()
        if again != 'j':
            print("Tack för att du spelade! Hej då!")
            break


if __name__ == "__main__":
    main()
