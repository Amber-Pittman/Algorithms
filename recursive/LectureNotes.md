# Recursion

Recursion is a very handy tool for coming up with a first step for solving certain algorithmic problems. 

1. Examples of recursion in a non-programming context. 
  
    * Mirrors on parallel walls, so the reflections continue to infinity

    * Sierpinski triangle - mathmatical pattern called a fractal where everything is defined within itself and just keeps reflecting in on itself, over and over again.

    * Mathmatical Recursion - The Fibonacci Sequence <br>
      F<sub>n</sub> = F<sub>n-1</sub> + F<sub>-2</sub> <br> F<sub>0</sub> = 0,  F<sub>1</sub> = 1

2. Recursion:
  
    * A base case (or cases) that specify when the recursion terminates. Once we've hit this case, stop the recursion.

    * A rule (or rules) that reduce all other cases towards a base case. If we're not at the base case, here's a rule for how we actually get there.  

3. Breaking Down Recursive Code:

    We're going to multiply everything preceding n all the way down to 1. So if it's a factorial of 4 where n = 4, then we'd multiply 4 by 3 by 2 by 1. But, obviously not zero because anything multiplied by zero returns zero. 

    For any n, we multiply it by the term before it and we multiply that by by the term before that, and then by the term before that, so on and so forth. 

    Then, the base case is going to be once it it hits zero because we don't actually want to multiply by zero. Once we hit zero, we want to stop the factorial function there in order to get our final product. 

    Once we've thought through what the factorial function was doing, we can kind of figure out that we want to stop at this point. We don't want to multiply by 0 and we're not going to consider negative values either.

    The function below assumes that n is a positive integer and then it's going to stop once it recurses down to zero.

    The second part of this function (the return), we essentially move towards this base case of n = 0. Note the recurse_factorial function gets called again, this time with n - 1. 

    If n were 4, it would skip down to the return, say 4 * recurse_factorial(4 - 1). It will do it again with 3. Then 2. And finally 1.

    ```
    def recurse_factorial(n):
      if n == 0:
        return 1
      return n * recurse_factorial(n-1)
    ```

4. Comparison between Recursive and Iterative Code:

    Both of the functions below do the same thing. But, you'll notice that the recursive function is slightly shorter and therefore less that you have to worry about, right?

    In the iterative function, you've got to worry about how to set up the for loop with a range that starts at n and goes down to 0 but skips zero, then steps through it backwards. 

    The recursive factorial function is more elegant because it's a lot easier to read if you just define a function recursively. That's kind of one of the big trade-offs when it comes to recursive code again. 

    ```
    def recurse_factorial(n):
      if n == 0:
        return 1
      return n * recurse_factorial(n-1)

    def iter_factorial(n):
      answer = 1
      for i in range(n, 0, -1): # the -1 makes it step through backwards
        answer *= i
      return answer
    ```

5. How do I know When to Use Recursion? <br>

    A lot of times, problems will have certain keywords or phrases that will make it pretty easy to spot out when you can use recursion to solve it. Anytime a problem asks you to `compute the nth term of` something, most of the time, you can utilize recursion to solve a problem. Other examples include:

    * "list the first n terms of ..."

    * "generate **_all_** possible permutations"

    * "compute the nth term of ..."

6. Pros and Cons of Recursion

    * Pros:

        * Starting Point - Most important facet of recursion is that oftentimes it gives us a tangible starting point for how to tackle a problem. We know that with recursion, we just need to figure out 2 things: the base case and how to get to that base case. That's pretty much it. 
        
            * Typically, it's not as obvious how we would solve a problem iteratively with loops and other things because there are no real established kind of rules for how to go about doing that. 
            
            * With recursion though, there are rules established for it. Oftentimes, recursion is a very good starting point even if you may not end up using your recursive solution as your final solution (for any number of reasons). 

        * Intuitive - once you get over the "mind-bending" aspect of how recursion itself works, more experienced, and accustomed to reading recursive code, recursive code is much easier to parse and understand.

        * Clean - the code is more elegant in the sense that you just define a function in terms of itself over and over again. 

    * Cons:

        * Initially, the idea of recursion can be a difficult concept to grasp.

        * Not Performant - Recursive code isn't actually as performant as iterative code. Part of that has to do with the fact that when you're using loops and things, you have finer grained control over how many iterations you want to do. 

            * With recursive code - even though you do have base cases - it doesn't give you as fined grained control as what you might have with loops. 

            * Although it's not as performant, it still gives you a framework that informs you of how you can start solving a recursive problem. 

7. Recursive Sorting Algorithms

    * Merge Sort:

        * Divide in half until you have subarrays of length 1(single element in the sub array); lists of length 1 are sorted!

            * It's impossible for a list of 1 element to be in the wrong spot. 

            * When we attempt to put sorted pieces back together, we can do that really efficiently. More efficiently than 

        * Merge sorted lists together. Let's say we have 8 subarrays that have 1 element in each. 
        
            * For example, we have [[3], [11], [10], [5], [8], [13], [4], [2]]. 

            * Start by merging the single elements. 
            
                * The 3 and the 11 will compare and determine it's already in order. They will make up the new subarray. [[3, 11]]

                * Then 10 and 5 will swap places and become a new subarray. [[5, 10]]

                * 8 and 13 will stay the same but make up a new sub array. [[8, 13]]

                * 4 and 2 will swap and create a new subarray. [[2, 4]]

                * Once all have been sorted, the array's subarrays should look like: [[3, 11], [5, 10], [8, 13], [2, 4]]

            * Since the subarrays are already sorted, we only have to check the front of each one. For `[3, 11], [5, 10]`, the comparison will be made at 3 and 5. 

                * Once it's determine that 3 is smaller, a comparison between 11 and 5 will be made since 11 is the new start of the first subarray. 11 is clearly larger than 5, so 5 joins 3. 

                * Now, 11 and 10 will compare. 10 will move into the new subarray next to 5. Finally, 11 will join the end after 10. 

                * At this point, the new subarray looks like this: `[3, 5, 10, 11]`.

            * Now that the left hand side of the array has been sorted, move on to the right hand side. The subarrays [8, 13], [2, 4] will now look like this: `[2, 4, 8, 13]`.

