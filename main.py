from my_functions import (my_name,
                          eco,
                          count_eco,
                          loop_five,
                          last,
                          cut_edges,
                          increase,average,
                          pretty_print)

my_name("Cami") # Output: Cami är en 🪽 på programmering!
eco("Hej!") # Output: Hej! & Hej!
count_eco("Hello!", 3) # Output: Hello!Hello!Hello!
loop_five() # Output: 2, 4, 8, 16, 32
last(lst= [1, 2, 3]) #Output: 3
last(lst= []) #Output: Listan är tom!
cut_edges(lst= [1, 2, 3, 4]) #Output: [2, 3]
cut_edges(lst= [0, 1]) #Output: []
cut_edges(lst= [1, 2, 3, 4, 5]) #Output: [2, 3, 4]
print(increase(1)) #Output: 2
print(average(2,4))
pretty_print(lst= []) #Listan är tom, None
pretty_print(lst= [1,-1, 3]) # Listan har 3 element:
pretty_print(lst = [ "a", "b" ,3.14, "Cami"]) # Listan har 4 element:

