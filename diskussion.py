
#1a
def foo(t):
    print("test")

foo("hej") # test
print("****************")

#1b
def fun1(x, y):
    return x * y

print(3, 5) # (3,5)
print("****************")
# ifall vi vill använda funktionen som returnerar en produkt
x = 3
y = 5
result = fun1(3,5)
print(result) # 15
print("****************")

def fun1(x, y):
    return x * y

print(fun1(x=3,y= 5)) # (3,5)
print("****************")

#1c
def fun1(x, y):
    return x * y

print(fun1(3, 5)) # 15
print("****************")

#1d
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

#1e
a = 5 # utanför scoopet
def fun3(a):
    a += 1


a += 2
print(a) # 7 ( 5 + 2)

#1f
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a) # 18
print("****************")
# min förbättring av 1f för att jag tycker det är svårt att förstå vilken output man ska förvänta sig

def calculate_double_square(number): # def foo
    return 2 * number * number

def apply_function(func, value): # def goo
    return func(value)

result = apply_function(calculate_double_square, 3)
print(f"Outputen är: {result}")
print("****************")

# använd lambda

result_lambda = apply_function(lambda x: 2 * x * x, 3)
print(f"The result using lambda is: {result_lambda} ")
print("****************")

# 1g Funktionen "isinstance" kan kontrollera en variabels datatyp.
# Vad gör funktionen is_number? Går det att förbättra koden?
def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(42))
print(is_number(5.5))
print(is_number("number"))

# variant a
def is_number_func(x):
    return isinstance(x, (int, float))

print(is_number_func(2))
print(is_number_func(2.4))
print(is_number_func("number"))

# variant b
from numbers import Number
def is_number_num(x):
    return isinstance(x, Number)

print(is_number_num(3))
print(is_number_num(3.1))
print(is_number_num(" "))
print(is_number_num(2+3j))
print("****************")

# 1h
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

result_1 = average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(result_1)

def average_words(strings):
    return [item for item in strings if 4 < len(item) < 8]

result_2= average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(result_2)

average_word = ["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"]

result_3 = list(filter(lambda word: 4 < len(word) < 8, average_word))
print(result_3)
print("****************")

# 1i En uppgift i tre delar:
# Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
# Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
# Rätta felen, så funktionen gör det den ska.

def find_min(numbers):
    counter = 0 # startar med 0 och hittar negativa tal
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11]) # 11
find_min([]) # 0
find_min([100]) # 0
print("****************")

def find_min_1(numbers):
    if not numbers:
        print("The list is empty")
        return None

    min_value = min(filter(lambda x: True, numbers))
    print(f"The smallest item is: {min_value}")
    return min_value

find_min_1([10, 3, -4, -11]) # 11
find_min_1([]) # none
find_min_1([100]) # 100
print("****************")

def find_min_2(numbers):
    if not numbers:  # Kollar om listan är tom
        print("The list is empty")
        return None

    min_value = numbers[0]
    for item in numbers:
        if item < min_value:
            min_value = item
    print(f"The smallest item is: {min_value}")
    return min_value

find_min_2([10, 3, -4, -11])
find_min_2([])
find_min_2([100])




