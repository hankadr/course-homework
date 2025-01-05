#task 1 - a function that calculates the product of the elements from a list of integers
#možná je to tím, že mám v hlavě furt bramborový salát, ale napsat kód je snazší než zadefinovat funkci a na nic z tohohle jsem nepřišla sama:D rip 
def product(int_list):
    product = 1
    for num in int_list:
        product *= num
    return product
numbers = [1, 2, 3, 4, 5]
result = product(numbers)
print("The product of the elements is:", result)

#task 2 -  a function to find the minimum in a list of integers
def find_minimum(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(find_minimum(numbers))

#task 3 - a fuction to define the amount of prime numbers in a list of integers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(numbers):
    prime_count = 0
    for number in numbers:
        if is_prime(number):
            prime_count += 1
    return prime_count

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(count_primes(numbers))

#task 4 - a function that removes a given number from the list of integers. Return the number of removed elements
def remove_number(numbers, target):
    count_removed = 0
    while target in numbers:
        numbers.remove(target)
        count_removed += 1
    return count_removed

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 5
print(remove_number(numbers, target)) 
print(numbers)

#task 5 - a function that takes two lists as a parameter and returns a list containing the elements of both lists
def combine_lists(list1, list2):
    return list1 + list2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = combine_lists(list1, list2)
print(combined_list)

#task 6 - a function that calculates the power of each element from the list of integers. A value for the power is passed as a parameter, the list is also passed as a parameter. The function returns a new list containing the results
def power_elements(numbers, power):
    return [number ** power for number in numbers]
numbers = [1, 2, 3, 4, 5]
power = 2
powered_list = power_elements(numbers, power)
print(powered_list)  # Output: [1, 4, 9, 16, 25]       
