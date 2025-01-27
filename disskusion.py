
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