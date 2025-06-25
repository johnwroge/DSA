

def solve_problem_compressed(input_data):
    # For problems where we only need the last few states
    # instead of the entire DP table
    
    # Step 1: Initialize variables to store necessary previous states
    prev1, prev2 = initial_values
    
    # Step 2: Iterate and update states
    for i in range(start, end):
        # Calculate current state based on previous states
        current = compute_from_previous(prev1, prev2)
        
        # Update previous states
        prev2 = prev1
        prev1 = current
    
    # Step 3: Return final answer
    return prev1



def fibonacci(n):
    if n <= 1:
        return n
    
    prev2 = 0  # fib(0)
    prev1 = 1  # fib(1)
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1