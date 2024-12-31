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
def minimumfind(min_list):
    number = 1
    for _ in min_list:
        min(int(_))
    return(_)
 
numbers = [1, 2, 3, 4, 5, 6]
result = minimumfind(numbers)
print(result)