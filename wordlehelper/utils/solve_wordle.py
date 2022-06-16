import json
import os.path
import requests

def solve_wordle(gray_letters, green_letters, yellow_letters, top_x: int = 10) -> list:
    """
    returns a list of words that can be used to solve the wordle
    """

    # check if the file 'word_freq.json' exists
    path = os.path.join(os.path.dirname(__file__), 'word_freq.json')
    if not os.path.isfile(path):
        # if not, download the file from the internet
        url = "https://raw.githubusercontent.com/3b1b/videos/master/_2022/wordle/data/freq_map.json"
        response = requests.get(url)
        assert response.status_code == 200
        data = response.json()
        with open(path, 'w') as outfile:
            json.dump(data, outfile)

    # read the word_freq file
    with open(path, 'r') as infile:
        word_freq = json.load(infile)


    rejected_letters = gray_letters  # letters not in word
    yellow = yellow_letters  # letter in word _ but not in the given index
    green = green_letters  # letter in word _ and in the given index

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
    cand.sort(key=lambda x: float(x[1]), reverse=True)
    cand = [x[0] for x in cand]
    return cand[:top_x] if top_x < len(cand) else cand

if __name__ == '__main__':
    print(solve_wordle('a','e2','c3'))