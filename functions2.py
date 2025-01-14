#task1 - a function that prints formatted text given below
def quote():
    text ="𝒟𝑜𝓃'𝓉 𝒸𝑜𝓂𝓅𝒶𝓇𝑒 𝓎𝑜𝓊𝓇𝓈𝑒𝓁𝒻 𝓌𝒾𝓉𝒽 𝒶𝓃𝓎𝑜𝓃𝑒 𝒾𝓃 𝓉𝒽𝒾𝓈 𝓌𝑜𝓇𝓁𝒹\n\n""𝒾𝒻 𝓎𝑜𝓊 𝒹𝑜 𝓈𝑜, 𝓎𝑜𝓊 𝒶𝓇𝑒 𝒾𝓃𝓈𝓊𝓁𝓉𝒾𝓃𝑔 𝓎𝑜𝓊𝓇𝓈𝑒𝓁𝒻.\n\n""𝐵𝒾𝓁𝓁 𝒢𝒶𝓉𝑒𝓈"
    return text

print('please generate a quote')
print(quote()) 

#task2 - a function that takes two numbers as a parameter and displays all even numbers in between
def even_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)

even_numbers(10, 20) 

#task3 - a function that prints an empty or solid square made out of some symbol. The function takes the following as parameters: the length of the side of the square, a symbol, and a boolean variable:
#if it is True, the square is solid;
# if False, the square is empty.
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


#task4 - a function that returns the smallest of five numbers. Numbers are passed as parameters
def smallest_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)
print(smallest_of_five(10, 5, 20, 3, 15)) 

#task5 - a function that returns the product of numbers in a specified range. The start and end points of the range are passed as parameters. 
# If the order of these points is incorrect (e.g., 5 is the end, and 25 is the start), swap them
def product_num(start,end):
    if start > end:
        start, end = end, start 
    product = 1
    for number in range(start,end+1):
        product *= number
    return product
    
print(product_num(5,25))

#task6 - a function that counts how many digits a number has. 
# The number is passed as a parameter. Return the received number of digits from the function

def number_digits(number):
    counter = 0
    for _ in number:
        counter += 1
    print(f'the number of digits is {counter}')

digits = input('state the number: ')
number_digits(digits)

#task7 - a function that checks if a number is a palindrome. 
# The number is passed as a parameter. If the number is a palindrome, return true, otherwise false.
def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False
    
print(is_palindrome(123321))
print(is_palindrome(123456))