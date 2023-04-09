import csv
import json

#Put all data into list
data = []
with open('sentiment_analysis_contest_train_file.csv', 'r', encoding='utf-8') as f:
    data = list(csv.reader(f, delimiter=','))

#Put each word into a list
words = []
for line in data:
    for word in line[2].split():
        if word not in words:
            words.append(word)

#Save list of words
with open('group_2_words.json', 'w') as f:
    json.dump(words, f)
