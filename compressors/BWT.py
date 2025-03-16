'''для длинных последовательностей'''
def BWT(data):
    code = bytearray()
    for i in range(1000, len(data), 1000):
        code.extend(BWT_help(data[i - 1000:i]))
    code.extend(BWT_help(data[i:]))
    return bytes(code)

def BWT_decode(cipher):
    decoded_data = bytearray()
    i = 0
    while i < len(cipher):
        original_pos = int.from_bytes(cipher[i:i + 2], "big")
        end = i + 2 + 1000 if i + 2 + 1000 <= len(cipher) else len(cipher)
        decoded_data.extend(BWT_help_decode(cipher[i:end]))
        i = end
    return bytes(decoded_data)

'''обычный бвт, но для длинных память ломается'''
def BWT_help(word):
    shifts = []
    for i in range(len(word)):
        shifted = word[i::] + word[0:i]
        shifts.append(shifted)
    shifts.sort()
    original_pos = shifts.index(word).to_bytes(2, "big")
    code_word = b''
    code_word += bytes(l[-1] for l in shifts)
    code = original_pos + code_word
    return code


def BWT_help_decode(cipher):
    original_pos = int.from_bytes(cipher[:2], "big")
    cipher = cipher[2:]
    table = sorted([(c, i) for i, c in enumerate(cipher)])
    result = []
    row = original_pos
    for _ in range(len(cipher)):
        char, row = table[row]
        result.append(char)
    return bytes(result)