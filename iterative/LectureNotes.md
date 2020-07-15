# Iterative Sorting

In search algos, imagine that you need to find a 7 of Hearts in a deck of 52 cards. If the deck of cards is sorted, we know that it's not going to be all the way at the end, nor all the way at the beginning; it's going to be closer to the middle. Maybe we can optimize for it, right? 

Search is something we consume everyday - everyone Googles things all the time. We look through our word docs for spelling errors or for text, we search and replace. Search is something that computers are not only very much used for, but it's also very important to find ways that we can optimize searching. We don't really have too many options unless we start to deep dive into what Google does. 

We do have a couple of basic things we could do to incredibly drastically improve our search capabilities if we're looking through an array or a long list of certain items. 

```
my_range = 100
my_size = 15

# This array is a list of sorted numbers
nums = list(range(0, my_size))

# This array is the same list, except it's unsorted numbers/randomized
shuffled_nums = list(range(0, my_size))
random.shuffle(shuffled_nums)

print(nums) # prints the numbers in a nice, neat line
print(shuffled_nums) # prints a jumbled up version of the same numbers

```

When it comes to a shuffled (or non-sorted) array/list we don't really have the ability to be too creative, unfortunately. We kind of have to do the most-obvious thing. We could certainly do worse than the most obvious thing, but we're just going to start at the beginning and go to the end, just checking to see if your 7 of Hearts is in the deck. 

Let's say we want to find the number 12. We want to write a function that searches through an array. It can return true or false if this number exists in the array. In the function, just take each number for num in array if num is the target, then return True.

Otherwise, if we've gone through the whole array, we return false.

This particular function is considered O(N). We're not doing anything logarithmic - we're not dividing anything or shortening the problem in any way. It's definitely _not_ constant because if we add more numbers to the list, we're going to add more steps. It's not squared because we're not over-complicating it in any sort of way. For each step, we don't have to do `n` more things. We just do a constant amount of things.

The function below is not a _bad_ solution, but if Google took 10K or even 1M steps to find what you need, you wouldn't use it. We definitely want to be a little bit more creative.

```
num_to_find = 12

# O(N) -- Linear Time
def linear_search(arr, target):
  for num in arr:
    if num == target:
      return True
  return False

print(linear_search(shuffled_nums, num_to_find)) # True
print(linear_search(nums, num_to_find)) # True
```

Going back to this idea of a sorted deck or list of numbers, what can we do to optimize the sorted list? We've already talked a little bit about the idea of binary search, but let's implement an idea. 

Since the list is already sorted, all we have to do is start in the middle, open up the array right in the middle, and see that it's 8 (for example) and we're looking for the number 12. Well, we know that 12 is larger than 8, so we'll ignore everything to the left of 8.

Let's change our list up a bit. We're going to make the list create a random set of numbers within a certain range, and have it do that 15 times. Then, we can use the sort method on the list. 

```
my_range = 100
my_size = 15

# Generates a random set of nums from 0 to 100 and have it do that 15x.
random_nums = random.sample(range(my_range), my_size)

print(random_nums) #prints a random number each time
num_to_find = 12

# O(N) -- Linear Time
def linear_search(arr, target):
  for num in arr:
    if num == target:
      return True
  return False

print(linear_search(shuffled_nums, num_to_find)) # True
print(linear_search(nums, num_to_find)) # True

random_nums.sort()
print(random_nums)
```

Once it's sorted and you see that 45 is in the middle of the range, there's no point in looking past 45 to larger numbers. The best thing you can do it start in the middle every single time. You effectively have the best chance of removing the most amount of range at any given chance. 

We can do this a very well known algorithm - Binary Search. It's a very practical and very great optimization for a problem that frankly exists in a lot of different situations for computers to solve. 

We're going to pass in the same array and target into the Binary Search function. We want to basically find the middle point/index of our list and start looking from there.  We need to write our algorithm in such a way that we know where to start our search (4) and we know where the end is (92). Our middle is 31. Then we constantly modify the values to update the middle and end until we find our target. `start + end // 2`

If at any point the start and end equal the same thing (or if somehow the end becomes _smaller_ than the start), we'll modify either of the values to the point where this algorithm no longer makes sense. Eventually, if we haven't found something just purely mathematically, we're going to end up with a value for end that is smaller than the start value.

In the while loop, we'll add the condition for a boolean. Using a boolean here kind of helps keep track of the while loop. We'll then look for the middle point in the list by adding the start and end together and then dividing by 2. Once divided, check to see if the middle index is the same as the target value. If it is, return True. 

Otherwise, we need to check if it is smaller. So if target is smaller, then we want to search kind of to the left-hand side of the array/list. We want to make the end move to the left. If 31 was the original middle, then the new end will be 29 (the median minus 1). We make it the median minus 1 because we already know the median 31 wasn't what we're looking for. No point in checking it again. 

Obviously, we have the other situation to contend with, which is target is greater than the middle index of the list. We need to move our start index to point to the next index after the original middle (32 is the new start).

If there's a target number that isn't found, the start eventually becomes the higher valued number and the end point eventually becomes the lower valued number - and  then there is no longer a middle point. 

```
random_nums = [4,10,13,17,21,26,29,31,32,50,67,70,74,85,92]

# O(log n) -- Logarithmic
def binary_search(arr, target):
    # get the middle point
    # compare the value in the middle with the target value
    # [4,10,13,17,21,26,29, //middle// 31,32,50,67,70,74,85,92 //end//]
    # [4,10,13,17, //middle// 21,26,29 //end//]

    start = 0
    end = (len(arr) - 1) # since we have 15 numbers, the end value is 14

    found = False
    while end >= start and not found:
      # get the middle point
      middle_index = (start + end) // 2
      
      # compare the value in the middle with the target value
      # if the middle the value is the same as target, set found to True
      if arr(middle_index) == target:
        found = True
      
      # move start or end index closer to one another, and shrink our 
      #   search space by half
      else:
        if target < arr(middle_index):
          end = middle_index - 1
        if target > arr(middle_index):
          start = middle_index + 1
    
    return found

random_nums.sort()
print(binary_search(random_nums, 13)) # returns True
print(binary_search(random_nums, 12)) # returns False
```

Given that the random_nums list is _sorted_, what is the runtime of the binary search? It's logarithmic because we are halving the input all the time. Even if you doubled the numbers within the list, logarithmically, we're just doing one more step. This is because we now have to halve this twice as large space but then after that, we're back to the original size of the list. That's the power of logarithmic time. However, logarithmic time does _require_ an already sorted array. You may be tempted to apply sort to the unordered array. 

What if our range is 50B with a size of 1M and we want to find 4578? We have 2 ways of searching through it - linear and binary. We can already tell linear search is going to take quite some time since it starts at the very beginning and goes one-by-one through the list until it finds the target number. 

```
my_range = 50000000000
my_size = 1000000

random_nums = random.sample(range(my_range), my_size)

print(random_nums)
num_to_find = 4578

# O(N) -- Linear Time
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

```