import json
import csv

#Load pruned data and test file
data = {}
with open('group_2_pruned_data.json', encoding='utf-8') as f:
    data = json.load(f)
tweets = []
with open('sentiment_analysis_contest_test_file.csv', 'r', encoding='utf-8') as f:
    tweets = list(csv.reader(f, delimiter=','))
tweets.pop(0)

#Return sentiment guess for input tweet.
#Returns 'Negative' for ambiguous tweets or tweets containing many words not in data set
def check_sentence(tweet):
    words = tweet.split()
    oddp = 1.0
    oddn = 1.0
    for word in words:
        if word in data:
            total = data[word]['Positive'] + data[word]['Negative']
            oddp *= (data[word]['Positive'])/total
            oddn *= (data[word]['Negative'])/total
    if oddp > oddn:
        return 'Positive'
    else:
        return 'Negative'

#Generate output 
out = {}
index = 0
for tweet in tweets:
    out[index+8000] = check_sentence(tweet[1])
    index+=1

#Test for verifying code against train file
'''
real = {}
index = 0
for tweet in tweets:
    real[index] = tweet[1]
    index+=1


total = len(tweets)
success = 0
for key in out:
    if out[key] == real[key]:
        success+=1

percent = success/total * 100
strp = str(percent) + '%'
print(strp)
'''

#Save guesses to files
with open('group_2_guesses.json', 'w') as f:
    json.dump(out, f)

with open('group_2_guesses.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['index', 'sentiment'])
    for guess in out:
        csvwriter.writerow([guess, out[guess]])