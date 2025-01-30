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
3 Följande kod ska sluta loopa efter 5 varv. 
Flytta den in i en funktion och justera den enligt kommentaren.
end = 5
y = 1
for x in range(1, 100):
    y *= 2
    # avsluta loopen med en if-sats här
print(y)

"""
def loop_five():
    end = 5
    y = 1
    for x in range(1,100):
        y *= 2
        print(y)
        if x == end:
            break

"""
4 Skriv en funktion med namnet last. 
Den ska ta en lista som parameter och returnera det sista elementet i listan.
last([1, 2, 3]) → 3
"""
def last(lst):
    if lst:  # Kollar om listan inte är tom
        return print(lst[-1])  # Returnerar sista elementet
    else:
        return print("Listan är tom!")  # Returnerar None om listan är tom

"""
5 Skriv en funktion med namnet cut_edges. 
Den ska ta en lista som parameter. 
När den anropas ska den returnera en ny lista, 
där den har tagit bort första och sista elementet.
cut_edges([1, 2, 3, 4]) → [2, 3]
"""
def cut_edges(lst):
    if len(lst) < 2:
        return []
    return print(lst[1:-1])

"""
6 Lös felen i koden.
def increase(x):
    return x
    x += 1

print(increase(1))
"""
def increase(x):
    x += 1 # Öka värdet med 1
    return x # Returnera det uppdaterade värdet

"""
7 Bygg en funktion med namnet average. 
Den ska ta parametrar: x och y. 
Båda ska vara tal. 
Funktionen ska returnera medelvärdet. 
Till exempel så räknar man ut medelvärdet av 4 och 8 genom med formeln: 
(4 + 8) / 2, vilket blir 6.
Tips: det kan vara enklare att använda fler variabler.
"""
def average(x,y):
    total = x + y
    avg = total / 2
    return avg

average_2 = lambda x, y: (x + y) / 2

"""
8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. 
Först ska funktionen tala om ifall listan är tom, eller hur många element den har. 
Sedan ska funktionen skriva ut elementen i en punktlista. 
Exempel:
pretty_print(["a", "b", 3.14])
Listan har 3 element:
1. a
2. b
3. 3.14
"""
def pretty_print(lst):
    if not lst:
        print("Listan är tom.")
    else:
        print(f"Listan har {len(lst)} element:")
        for i in range(len(lst)):
            print(f"{i + 1}. {lst[i]}")