#task 1 - palindrome
palindrome = input(f'submit your input: ') #kayak
if palindrome == palindrome[ : :-1]:
        print(f'yayy, it is a palindrome')
else:
        print('that is not a palindrome, try again')

#task 2 - type text + reserved words, change reserved words from lowercase to uppercase
#nebudu herečkovat, u tohohle tasku muselo pomoct AI, sama bych to nikdy nesplácala dohromady:D
text = input('submit your text: ') #I always walk my dog with an umbrella and a pepper spray.
words_to_capitalize = input('type in 3 reserved words: ') #dog, umbrella, spray
words = text.split()
capitalized_words = [word.upper() if word in words_to_capitalize else word for word in words]
result = ' '.join(capitalized_words)
print(result)


#task 3 - input a text and count the number of senteces
text = input('submit your text: ') #Ema má mámu. Máma má tátu. Táta má psa.
count = text.count('.')
print(f'The number of senteces is {count}.')
