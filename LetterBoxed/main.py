from heapq import heappop, heappush


def read_words(filename):
    words = []
    with open(filename, 'r') as f:
        for line in f:
            words.append(line.strip().lower())
    return words


def filter_words(words, sides):
    filtered_words = []
    for word in words:
        if len(word) <= 2:
            continue
        add = True
        for c, letter in enumerate(word):
            if not letter in ''.join(sides):
                add = False
                break
            if c < len(word) - 1:
                if letter in sides[0] and word[c+1] in sides[0]:
                    add = False
                    break
                if letter in sides[1] and word[c+1] in sides[1]:
                    add = False
                    break
                if letter in sides[2] and word[c+1] in sides[2]:
                    add = False
                    break
                if letter in sides[3] and word[c+1] in sides[3]:
                    add = False
                    break
        if add:
            filtered_words.append(word)
    return filtered_words


def categorize_words(words):
    categorized = {}
    for word in words:
        if not word[0] in categorized:
            categorized[word[0]] = []
        categorized[word[0]].append(word)
    return categorized


def find_word_paths(words, categorized):
    queue = []
    for word in words:
        heappush(queue, (1, [word]))
    mini = float('inf')
    miniTwo = float('inf')
    while len(queue) > 0:
        nextUp = heappop(queue)[1]
        for nextWord in categorized[nextUp[-1][-1]]:
            if nextWord in nextUp:
                continue
            toAdd = nextUp + [nextWord]
            if len(set(''.join(toAdd))) == 12:
                if (len(toAdd) >= 3 and len(''.join(toAdd)) < mini) or (len(toAdd) < 3 and len(''.join(toAdd)) < miniTwo):
                    if len(toAdd) < 3:
                        miniTwo = len(''.join(toAdd))
                    else:
                        mini = len(''.join(toAdd))
                    mini = min(mini, miniTwo)
                    print(' '.join(toAdd), len(''.join(toAdd)))
                    if mini == 11 + len(toAdd):
                        return
                continue
            heappush(queue, (len(toAdd), toAdd))


if __name__ == '__main__':
    words = read_words('LetterBoxed/words-easy.txt')
    sides = [input('Enter side 1: '), input('Enter side 2: '), input('Enter side 3: '), input('Enter side 4: ')]
    filtered_words = filter_words(words, sides)
    category = categorize_words(filtered_words)
    find_word_paths(filtered_words, category)