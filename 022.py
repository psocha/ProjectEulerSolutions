"""
Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.
What is the total of all the name scores in the file?
"""

def alphabetical_value(name):
    alpha_sum = 0
    for ch in name:
        alpha_sum += (ord(ch) - ord('A') + 1)
    return alpha_sum

with open('input_files/022.txt') as f:
    names_str = f.read()
    names_list = names_str.split(',')
    names_list = [name[1:-1] for name in names_list]

sorted_names_list = sorted(names_list)

name_score = 0
for index, name in enumerate(sorted_names_list):
    index_score = index + 1
    word_score = alphabetical_value(name)
    name_score += (index_score * word_score)

print(name_score)

