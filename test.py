# text = input('submit your text: ') #I always walk my dog with an umbrella and a pepper spray.
# myStr = ['dog','umbrella','spray']
# words = text.split
# myStr = str(myStr)
# capitalized_words = [myStr.upper()]
# result = text + ' '.join(capitalized_words)
# print(result)

# Define the text and the words to capitalize
# text = input('submit your text: ')
# words_to_capitalize = input('type in 3 reserved words: ')

# Split the text into words
# words = text.split()

# Capitalize the specific words
# capitalized_words = [word.upper() if word in words_to_capitalize else word for word in words]

# Join the words back into a single string
# result = ' '.join(capitalized_words)

# Print the result
# print(result)

#task 2 -  a function to find the minimum in a list of integers
# def find_minimum(numbers):
#     minimum = numbers[0]
#     for number in numbers:
#         if number < minimum:
#             minimum = number
#     return minimum

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# print(find_minimum(numbers))

#task 3 - a fuction to define the amount of prime numbers in a list of integers
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def count_primes(numbers):
#     prime_count = 0
#     for number in numbers:
#         if is_prime(number):
#             prime_count += 1
#     return prime_count

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# print(count_primes(numbers))  

#task 4: a function that removes a given number from the list of integers. Return the number of removed elements

# def remove_number(numbers, target):
#     count_removed = 0
#     while target in numbers:
#         numbers.remove(target)
#         count_removed += 1
#     return count_removed

# # Example usage:
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# target = 5
# print(remove_number(numbers, target))  # Output: 3
# print(numbers)  # Output: [3, 1, 4, 1, 9, 2, 6, 3]

#a function that takes two numbers as a parameter and displays all even numbers in between

# x = 1
# y = 10
# for a in range(x,y):
#     if a//2:
#         print(a)
#     else:
#         print('no even numbers in this range')


# def even_numbers(start, end):
#     for number in range(start, end + 1):
#         if number % 2 == 0:
#             print(number)

# even_numbers(10, 20) 
# 
# a function that returns the smallest of five numbers. Numbers are passed as parameters
# def smallest_of_five(a, b, c, d, e):
#     return min(a, b, c, d, e)
# print(smallest_of_five(10, 5, 20, 3, 15)) 
#task5 - a function that returns the product of numbers in a specified range. The start and end points of the range are passed as parameters. 
# If the order of these points is incorrect (e.g., 5 is the end, and 25 is the start), swap them
# def product_num(start,end):
#     if start > end:
#         start, end = end, start 
#     product = 1
#     for number in range(start,end+1):
#         product *= number
#     return product
    
# print(product_num(5,25))

#task6 - a function that counts how many digits a number has. 
# The number is passed as a parameter. Return the received number of digits from the function.

# def number_digits(number):
#     counter = 0
#     for _ in number:
#         counter += 1
#     print(f'the number of digits is {counter}')

# digits = input('state the number: ')
# number_digits(digits)

#task7 - a function that checks if a number is a palindrome. 
# The number is passed as a parameter. If the number is a palindrome, return true, otherwise false.

# def is_palindrome(number):
#     number = str(number)
#     if number == number[::-1]:
#         return True
#     else:
#         return False
    
# print(is_palindrome(123321))
# print(is_palindrome(123456))

def print_square(side_length, symbol, is_solid):
    if side_length < 1:
        print("Side length must be at least 1.")
        return

    if is_solid:
        for _ in range(side_length):
            print(symbol * side_length)
    else:
        for i in range(side_length):
            if i == 0 or i == side_length - 1:
                print(symbol * side_length)
            else:
                print(symbol + " " * (side_length - 2) + symbol)

print_square(5, '*', True)  # Solid square
print()
print_square(5, '*', False)  # Empty square    



        
