import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    A strong number is a number whose sum of the factorial of its digits 
    equals the number itself.
    """
    if num < 0:
        return False  # Strong numbers are typically positive integers.
    
    original_num = num
    sum_of_factorials = 0

    # Handle the case of 0 separately as 0! is 1.
    if num == 0:
        return False # 0 is not considered a strong number in most definitions.

    # Iterate through each digit of the number
    for digit_char in str(num):
        digit = int(digit_char)
        sum_of_factorials += math.factorial(digit)

    return sum_of_factorials == original_num

def find_strong_numbers_in_range(start, end):
    """
    Finds all strong numbers within a specified range (inclusive).
    """
    strong_numbers = []
    for num in range(start, end + 1):
        if is_strong_number(num):
            strong_numbers.append(num)
    return strong_numbers

# Find and print strong numbers from 1 to 5000
start_range = 1
end_range = 5000
strong_numbers_list = find_strong_numbers_in_range(start_range, end_range)

print(f"Strong numbers between {start_range} and {end_range}:")
if strong_numbers_list:
    print(strong_numbers_list)
else:
    print("No strong numbers found in this range.")