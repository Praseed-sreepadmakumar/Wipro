import time
import math
import sys
from multiprocessing import Pool, cpu_count

sys.set_int_max_str_digits(1000000)

numbers = [50000, 60000, 55000, 45000, 70000]

def calculate_factorial(n):
    return math.factorial(n)

def sequential_computation(nums):
    return [calculate_factorial(num) for num in nums]

def multiprocessing_computation(nums):
    with Pool(processes=cpu_count()) as pool:
        return pool.map(calculate_factorial, nums)

if __name__ == "__main__":

    start_time = time.time()
    sequential_results = sequential_computation(numbers)
    print("Sequential Time:", time.time() - start_time)

    start_time = time.time()
    multiprocessing_results = multiprocessing_computation(numbers)
    print("Multiprocessing Time:", time.time() - start_time)

    for num, result in zip(numbers, multiprocessing_results):
        print(f"Factorial of {num} has {len(str(result))} digits")
