#Zdravím, vzala jsem task1 z úplně prvního souboru úkolů a updatovala viz níže
#The user types in three numbers. The program prints the sum or product of these numbers based on the user's choice.
sum = 0
product = 1
for _ in range(3):
    numbers = int(input(f'submit your number: '))
    sum += numbers
    product *= numbers 
print(f'the sum of the numbers is {sum} and the product is equal to {product}')
    
