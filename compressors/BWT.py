def quick_sort(A):
    def divide(A, j):
        B = []
        count = 0
        for i in range(len(A)):
            if A[i] < A[j]:
                B.append(A[i])
                count += 1
        for i in range(len(A)):
            if A[i] == A[j]:
                B.append(A[i])
        for i in range(len(A)):
            if A[i] > A[j]:
                B.append(A[i])
        return B, count

    if len(A) <= 1:
        return A
    if len(A) == 2:
        if A[0] > A[1]:
            return [A[1], A[0]]
        return A
    if len(A) > 2:
        A, i = divide(A, 0)
        A = quick_sort(A[0: i]) + A[i: i + 1] + quick_sort(A[i + 1::])
        return A


'''для длинных последовательностей'''
def BWT(data, l=1000):
    code = bytearray()
    for i in range(l, len(data), l):
        code.extend(BWT_help(data[i - l:i]))
    code.extend(BWT_help(data[i:]))
    return bytes(code)

def BWT_decode(cipher, l=1000):
    decoded_data = bytearray()
    i = 0
    while i < len(cipher):
        original_pos = int.from_bytes(cipher[i:i + 2], "big")
        end = i + 2 + l if i + 2 + l <= len(cipher) else len(cipher)
        decoded_data.extend(BWT_help_decode(cipher[i:end]))
        i = end
    return bytes(decoded_data)

'''обычный бвт, но для длинных память ломается'''
def BWT_help(word):
    shifts = []
    for i in range(len(word)):
        shifted = word[i::] + word[0:i]
        shifts.append(shifted)
    shifts = quick_sort(shifts)
    original_pos = shifts.index(word).to_bytes(2, "big")
    code_word = b''
    code_word += bytes(l[-1] for l in shifts)
    code = original_pos + code_word
    return code


def BWT_help_decode(cipher):
    original_pos = int.from_bytes(cipher[:2], "big")
    cipher = cipher[2:]
    table = quick_sort([(c, i) for i, c in enumerate(cipher)])
    result = []
    row = original_pos
    for _ in range(len(cipher)):
        char, row = table[row]
        result.append(char)
    return bytes(result)