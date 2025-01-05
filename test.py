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

def remove_number(numbers, target):
    count_removed = 0
    while target in numbers:
        numbers.remove(target)
        count_removed += 1
    return count_removed

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 5
print(remove_number(numbers, target))  # Output: 3
print(numbers)  # Output: [3, 1, 4, 1, 9, 2, 6, 3]