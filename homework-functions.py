#task 1 - a function that calculates the product of the elements from a list of integers
def product(int_list):
    product = 1
    for num in int_list:
        product *= num
    return product
numbers = [1, 2, 3, 4, 5]
result = product(numbers)
print("The product of the elements is:", result)

#task 2 -  a function to find the minimum in a list of integers
def minimumfind(min_list):
    min(input(f'submit random numbers with a space inbetween'))