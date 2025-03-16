t = "xjhdueowpqmsncnvbxzlkajdhff"


def RLE(text):
    compressed_data = ''
    f = 0
    counter = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            if f:
                compressed_data += '$'
                f = 0
            counter += 1
        if text[i] != text[i - 1] or i == len(text):
            if counter > 1:
                compressed_data += f'{chr(counter)}{text[i - 1]}'
                counter = 1
            else:
                if not f:
                    compressed_data += '$'
                    f = 1
                compressed_data += f'{text[i - 1]}'
    if counter > 1:
        compressed_data += f'{chr(counter)}{text[-1]}'
    else:
        if f:
            compressed_data += f'{text[-1]}$'
        else:
            compressed_data += f'${text[-1]}$'

    return compressed_data



compressed = RLE(t)


def RLE_decomposition(c_t):
    original = ''
    f = 0
    i = 0
    while i < len(c_t):
        if c_t[i] == "$":
            if f:
                f = 0
            else:
                f = 1
        else:
            if f:
                original += c_t[i]
            else:
                original += ord(c_t[i]) * c_t[i + 1]
                i += 1
        i += 1
    return original


decomp = RLE_decomposition(compressed)
print(t)
print(compressed)
print(decomp)
print(t == decomp)
