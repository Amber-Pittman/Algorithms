import random
import time  # We'll use this later

my_range = 50000000000
my_size = 1000000

random_nums = random.sample(range(my_range), my_size)

num_to_find = 4578

# O(N) linear time
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False


print("Linear")
start = time.time()
print(linear_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")


def binary_search(arr, target):
    start = 0
    end = (len(arr) - 1)

    found = False
    while end >= start and not found: 
        # get the middle point
        middle_index = (start + end) // 2 
        # compare the value in the middle with target
        # if the middle value is the same as target, set found to True
        if arr[middle_index] == target:
            found = True
        # move start or end index closer to one another, and shrink our search space
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1
    return found

print("Binary")
start = time.time()
random_nums.sort()
print(binary_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")

print("Binary")
start = time.time()
print(binary_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")