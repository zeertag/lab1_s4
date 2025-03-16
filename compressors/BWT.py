word = 'тёма'


def BWT(word):
    word += '$'
    shifts = []
    for i in range(len(word)):
        shifted = word[i::] + word[0:i]
        shifts.append(shifted)
    return sorted(shifts)


s = BWT(word)

code = ''.join(_[-1] for _ in s)
print(code)


def BWT_decode(cipher):
    words = []
    for i in range(len(cipher)):
        text = '*' * (len(cipher) - 1)
        text += cipher[i]
        words.append(text)

    for i in range(len(cipher) - 1):
        for k in range(len(words)):
            words[k] = words[k][-1] + words[k][:-1]

        words.sort()

        for j in range(len(cipher)):
            words[j] = words[j][0:-1] + cipher[j]
    return words


a = BWT_decode(code)
print(a)
