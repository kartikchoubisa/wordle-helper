import json
import os.path

import requests


# check if the file 'word_freq.json' exists
if not os.path.isfile('word_freq.json'):
    # if not, download the file from the internet
    url = "https://raw.githubusercontent.com/3b1b/videos/master/_2022/wordle/data/freq_map.json"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    with open('word_freq.json', 'w') as outfile:
        json.dump(data, outfile)

# read the word_freq file
with open('word_freq.json', 'r') as infile:
    word_freq = json.load(infile)


rejected_letters = 'r'  # letters not in word
yellow = ''  # letter in word _ but not in the given index
green = ''  # letter in word _ and in the given index

yellow = [[yellow[i], int(yellow[i + 1]) - 1] for i in range(0, len(yellow), 2)]
green = [[green[i], int(green[i + 1]) - 1] for i in range(0, len(green), 2)]

cand = []
# for word, frequency in the word_freq dict
for word, freq in word_freq.items():
    # if word is a 5 letter word, continue
    if len(word) != 5:
        continue
    # if the word contains any of rejected letters
    if any(letter in word for letter in rejected_letters):
        continue
    # if the word does not contain all yellow letters
    if not all(yellow_letter in word for yellow_letter, yellow_index in yellow):
        continue
    # if a yellow character lies at a yellow index in the word
    if any(word[yellow_index] == yellow_letter for yellow_letter, yellow_index in yellow):
        continue
    # if a green character does not lie at green index in the word
    if not all(word[green_index] == green_letter for green_letter, green_index in green):
        continue
    cand.append((word, freq))
# sort cand by freq (ascending)
cand.sort(key=lambda x: float(x[1]))
for word, freq in cand:
    print(word, freq)