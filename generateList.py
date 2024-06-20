import csv
import json
import random
from Levenshtein import distance as levenshtein_distance 

csvoutput = open('Generated_List.csv', 'w', newline='')
writer = csv.writer(csvoutput)
writer.writerow(['Word'])

words_list = []
index = 643
generated_words_list = []

# words_file = csv.reader("text2.csv")('text2.csv', dialect='excel', )
# words_list = words_file['Word'].tolist()

with open('text2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    next(reader)
    for row in reader:
        words_list.append(row[0])

    csvfile.close()

# print(words_list)

# generates first word
first = random.randint(0, index)
generated_words_list.append(words_list[first])
writer.writerow([words_list[first]])
words_list.remove(words_list[first])
index -= 1

# print(generated_words_list)
# print(words_list)
# print(index)

for i in range(15):
    rand_index = random.randint(0, index)
    wordFound = False
    restartLoop = False
    while not wordFound:
        restartLoop = False
        for x in generated_words_list:
            # print(str(levenshtein_distance(words_list[rand_index], x))+ " " + words_list[rand_index] + " " + x)
            if (levenshtein_distance(words_list[rand_index], x) < 2):
                # print("rand reset")
                rand_index = random.randint(0, index)
                restartLoop = True
                break
        if(not restartLoop): 
            # print(words_list[rand_index])
            wordFound = True

    generated_words_list.append(words_list[rand_index])
    writer.writerow([words_list[rand_index]])
    words_list.remove(words_list[rand_index])
    index -= 1

print(generated_words_list)
csvoutput.close()




