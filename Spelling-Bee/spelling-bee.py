def read_words(filename):
    words = []
    with open(filename, 'r') as f:
        for line in f:
            words.append(line.strip().lower())
    return words
def filter_words(words, outerLetters, center):
    filtered_words = []
    for word in words:
        if len(word) <= 3:
            continue
        if not center in word:
            continue
        add = True
        for letter in word:
            if not letter in outerLetters + center:
                add = False
                break
        if add:
            filtered_words.append(word)
    return filtered_words

if __name__ == '__main__':
    words = read_words('LetterBoxed/scrabble.txt')
    outerLetters = input('Enter outer letters: ')
    center = input('Enter center letter: ')
    words = filter_words(words, outerLetters, center)
    print(words)