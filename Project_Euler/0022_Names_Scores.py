'''
Using names.txt (right click and 'Save Link/Target As...'), a 
46K text file containing over five-thousand first names, begin by sorting it 
into alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 
938 * 53 = 49714. 

What is the total of all the name scores in the file?

'''

import os
import re

file_path = os.path.abspath('./Project_Euler/input/22_names.txt')


list_of_names = []

with open(file_path) as f:
    string = f.readlines()
    names = string[0].split(',')
    for name in names:
        letters = re.sub(r'[^a-zA-Z]', '', name)
        list_of_names.append(letters.lower())
 

def name_to_score(word: str):
    letters = [ord(c) - ord('a') + 1 for c in word]
    return sum(letters)

def sort_names_alphabetically(word_list):
    word_list = [word.lower() for word in word_list]
    sorted_words = sorted(word_list)
    return sorted_words

def find_answer(names):
    test2 = sort_names_alphabetically(names)
    find_score = [name_to_score(name) * (i + 1) for name, i in zip(test2, range(len(test2)))]
    return sum(find_score)


print(find_answer(list_of_names))



