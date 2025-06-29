'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

"""
Find the largest 1-9 pandigital number that can be formed as the concatenated 
product of an integer with (1,2,...,n) where n > 1.

Examples:
- 192 × (1,2,3) = 192|384|576 = 192384576
- 9 × (1,2,3,4,5) = 9|18|27|36|45 = 918273645
"""

def is_pandigital_1_to_9(number_str):
    """Check if a 9-digit string contains each digit 1-9 exactly once."""
    return len(number_str) == 9 and set(number_str) == set('123456789')

def find_pandigital_products():
    """Find all pandigital numbers formed as concatenated products."""
    results = []
    
    # n = 2: 4-digit × (1,2) → 4+5 = 9 digits
    for number in range(5000, 50000):  # 5000 ≤ number < 50000 to get 5-digit product
        concatenated = str(number) + str(number * 2)
        if len(concatenated) == 9 and is_pandigital_1_to_9(concatenated):
            results.append((concatenated, number, 2))
    
    # n = 3: 3-digit × (1,2,3) → 3+3+3 = 9 digits
    for number in range(100, 334):  # Stop when number*3 becomes 4 digits
        concatenated = str(number) + str(number * 2) + str(number * 3)
        if len(concatenated) == 9 and is_pandigital_1_to_9(concatenated):
            results.append((concatenated, number, 3))
    
    # n = 4: 2-digit × (1,2,3,4) → need exactly 9 digits total
    for number in range(10, 100):
        products = [number * i for i in range(1, 5)]
        concatenated = ''.join(str(p) for p in products)
        if len(concatenated) == 9 and is_pandigital_1_to_9(concatenated):
            results.append((concatenated, number, 4))
    
    # n = 5: 1-digit × (1,2,3,4,5) → need exactly 9 digits total  
    for number in range(1, 10):
        products = [number * i for i in range(1, 6)]
        concatenated = ''.join(str(p) for p in products)
        if len(concatenated) == 9 and is_pandigital_1_to_9(concatenated):
            results.append((concatenated, number, 5))
    
    # n ≥ 6: Check remaining cases with 1-digit numbers
    for n in range(6, 10):
        for number in range(1, 10):
            products = [number * i for i in range(1, n + 1)]
            concatenated = ''.join(str(p) for p in products)
            if len(concatenated) == 9 and is_pandigital_1_to_9(concatenated):
                results.append((concatenated, number, n))
    
    return results

def main():
    results = find_pandigital_products()
    
    largest = max(results, key=lambda x: x[0])
    pandigital, number, n = largest
    return pandigital

if __name__ == "__main__":
    print(main())