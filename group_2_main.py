import json
import csv

#Load word list and train file
words = []
with open('group_2_words.json', encoding='utf-8') as f:
    words = json.load(f)
tweets = []
with open('sentiment_analysis_contest_train_file.csv', 'r', encoding='utf-8') as f:
    tweets = list(csv.reader(f, delimiter=','))

#Set each word in map to have default negative and positive counts
data = {}
for word in words:
    data[word] = {'Positive': 0, 'Negative': 0}

#Go through each tweet and increment sentiment for each word in the tweet
for line in tweets:
    for word in line[2].split():
            if line[1] == 'Negative':
                data[word]['Negative'] += 1
            else:
                data[word]['Positive'] += 1

#Remove words that have no clear favored sentiment 
pruned_data = {}
for key in data:
    value = data[key]
    total = value['Positive'] + value['Negative']
    if (value['Positive'])/total > 0.7 or (value['Negative'])/total > 0.7:
        pruned_data[key] = value


#Save both data sets, raw and pruned
with open('group_2_pruned_data.json', 'w') as f:
    json.dump(pruned_data, f)
with open('group_2_data.json', 'w') as f:
    json.dump(data, f)