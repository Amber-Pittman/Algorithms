# Constant time O(1)
def print_num(n):
    print(n)

# Constant Time O(10000)
def print_num_10000(n):
    for _ in range(10000):
        print(n)


# Linear Times

#O(n) 
# n = 10
# n will be printed 10 times
# n = 10000000
# n will be printed 10000000 times
def print_num_n_times(n):
    for _ in range(n): # loop runs O(n) times
        print(n) #O(1)

# O(N*10000)
def print_num_n_times_modified(n):
    for _ in range(n): # loop runs O(n) times
        print(n) #O(1)
        for _ in range(10000): # O(10000)
            print(n)


animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

# O(N * N) = O(N^2)
# Polynomial Time
def print_animal_pairs():
    for animal_1 in animals: #O(N)
        for animal_2 in animals: #O(N)
            print(f'{animal_1} and {animal_2}') #O(1)

# (N * N * N) = O(N^3)
def print_animal_triplets():
    for animal_1 in animals: #O(N)
        for animal_2 in animals: #O(N)
            for animal_3 in animals: #O(N)
                print(f'{animal_1} and {animal_2} and {animal_3}') #O(1)

# Logarithmic Time
# we are removing HALF of the remaining animals each time
# the input gets reduced by a factor each iteration
def free_animals(animals):
    while len(animals) > 0:
        animals = animals[0: len(animals // 2)]