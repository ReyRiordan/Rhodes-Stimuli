import csv
import json
import random


# csvoutput = open('Pokemon_Names_Pervasive_Harmony.csv', 'w', newline='')
csvoutput = open('Pokemon_Names_First_Last_Harmony.csv', 'w', newline='')
writer = csv.writer(csvoutput)
writer.writerow(['Word'])


# generated_words_list = ["CiCi", "CiCe","CeCi","CeCe","CuCu","CuCo","CoCu","CoCo"]
generated_words_list = ["CiCo", "CiCe","CeCi","CeCu","CuCe","CuCo","CoCu","CoCi"]
consonants = ['p', 'b', 't', 'd', 'g', 'k', 'n', 'm', 's', 'z']

for i in range(8):
    word = generated_words_list[i]
    for x in consonants:
        word_list = list(word)
        word_list[0] = x
        word = "".join(word_list)
        for y in consonants:
            word_list = list(word)
            word_list[2] = y
            word = "".join(word_list)
            print(word)
            writer.writerow([word])


print(generated_words_list)
csvoutput.close()