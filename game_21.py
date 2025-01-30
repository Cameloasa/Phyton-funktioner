"""
Spelet 21
Om man lägger ihop talen 1 + 2 + 3 + 4 + …
så kommer talens summa att bli större och större.
Förr eller senare kommer man förbi 21.
Skriv en funktion som skriver ut det första talet i talserien som är större än 21.

Version 2: i stället för att använda talserien,
slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
Tips: importera modulen random och använd funktionen randint för att slumpa tal.
Exempel: card = random.randint(1, 13)

Möjlig vidareutveckling:
bygg ett spel som frågar användaren om man vill ta ett nytt kort eller stanna. (slumpa ett tal) Gör så att datorn kan simulera en motståndare. Målet är att vinna över datorn.
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