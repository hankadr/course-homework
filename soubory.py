# Task 1: You have two text files. Find out if their lines match. If they don't, print the mismatched line from each file.
import os
path = r'C:\Users\hdrastichova\OneDrive - ATS Global B.V\Desktop\osobní\python\homeworks\course-homework'
text_1 = 'match_first.txt'
text_2 = 'match_second.txt'

full_path_1 = os.path.join(path,text_1)
full_path_2 = os.path.join(path,text_2)

with open(full_path_1, "r") as file1, open (full_path_2, "r") as file2:
    file1_lines=file1.readlines()
    file2_lines=file2.readlines()

    for line in file1_lines:
        if line not in file2_lines:
            print(f"- {line.strip()}")

    for line in file2_lines:
        if line not in file1_lines:
            print(f" {line.strip()}")

# Task 2
#You have a text file. Create a new file and write the following statistics based on the source file to it:
#Number of characters;
#Number of lines;
#Number of vowels;
#Number of consonants;
#Number of digits.

import os
path = r'C:\Users\hdrastichova\OneDrive - ATS Global B.V\Desktop\osobní\python\homeworks\course-homework'
text = 'lyrics.txt'
statistics = 'lyrics_stat.txt'
full_path = os.path.join(path,text)
new_full_path = os.path.join(path, statistics)
char_count = 0
line_count = 0
vowel_count = 0
consonant_count = 0
digit_count = 0
vowels = "aeiouAEIOU"

with open(full_path, "r") as file:
    lines = file.readlines()
    line_count = len(lines)
    for line in lines:
        char_count += len(line) 
        for char in line:
            if char.isdigit():
                digit_count += 1
            elif char.isalpha():  
                if char in vowels:
                    vowel_count += 1  
                else:
                    consonant_count += 1 
with open(new_full_path, "w") as new_file:
    new_file.write(f"Number of characters: {char_count}.\n Number of consonants: {consonant_count}.\n Number of lines: {line_count}.\n Number of digits: {digit_count}.\n Number of vowels: {vowel_count}.\n")

#Task 3: You have a text file. Delete the last line from it. Write the result to another file.
import os
path = r'C:\Users\hdrastichova\OneDrive - ATS Global B.V\Desktop\osobní\python\homeworks\course-homework'
text = 'lyrics.txt'
new_text = 'lyrics_new.txt'
full_path = os.path.join(path,text)
new_full_path = os.path.join(path, new_text)

with open(full_path, "r") as file:
   lines = file.readlines()
last_line = lines[-1]
with open(full_path, "w") as file:
    file.writelines(lines[:-1])
with open(new_full_path, "w") as new_file:
    new_file.write(last_line)

#Task 4: You have a text file. Find the length of the longest line.
import os
path = r'C:\Users\hdrastichova\OneDrive - ATS Global B.V\Desktop\osobní\python\homeworks\course-homework'
text = 'lyrics.txt'
full_path = os.path.join(path,text)

with open(full_path, "r") as file:
    longest_line_length = max(len(line) for line in file)
print(f"The length of the longest line is {longest_line_length} characters.")

# Task 5: You have a text file. Count how many times the word specified by the user occurs in it.
import os
path = r'C:\Users\hdrastichova\OneDrive - ATS Global B.V\Desktop\osobní\python\homeworks\course-homework'
text_1 = 'lyrics.txt'
full_path = os.path.join(path,text_1)

with open(full_path, "r") as file1:
    file1_lines=file1.readlines()
    
    a = 'storm'.lower()
    counter=0
    for line in file1_lines:
        counter += line.lower().count(a)
    print(f"The word 'Storm' appears {counter} times.")

# Task 6: You have a text file. Find and replace the specified word. 
# The user determines what to search for and to what it should be replaced.
import os
path = r'C:\Users\hdrastichova\OneDrive - ATS Global B.V\Desktop\osobní\python\homeworks\course-homework'
text_old = 'lyrics.txt'
full_path1 = os.path.join(path,text_old)
word_to_replace = input('Please enter a word that should be replced in the text file: ')
new_word = input('Now please enter the new word: ')
with open(full_path1, "r+") as file:
    lines=file.readlines()
    file.seek(0)

    for line in lines:
        file.write(line.replace(word_to_replace, new_word))
print(f"All occurrences of '{word_to_replace}' have been replaced with '{new_word}'.")