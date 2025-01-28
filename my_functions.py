"""
1 Skriv en funktion som tar en sträng som parameter.
När den anropas ska den skriva ut strängen och "är en fena på programmering". Exempel:
my_function("David") → "David är en riktig hacker"
"""
def my_name(name):
    print(f"{name} är en 🪽 på programmering!")

"""
2a Skriv en funktion med namnet "eko". 
När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet. 
Exempel:
eko("hej") → skriver ut "hejhej"
"""

def eco(word):
    print(f"{word} & {word}")

"""
2b Lägg till en parameter "count", 
som avgör hur många ekon som ska skapas. 
Exempel:
eko("hej", 3) → skriver ut "hejhejhej"
"""

def count_eco(word,count):
    result = word * count
    print(result)
    return result

"""
3 Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.
end = 5
y = 1
for x in range(1, 100):
    y *= 2
    # avsluta loopen med en if-sats här
print(y)
"""
