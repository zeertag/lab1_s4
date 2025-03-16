def LZ77(data):
    i = 0
    n = len(data)
    window_size = 1024
    buffer_size = 16
    compressed_data = []

    while i < n:
        match_len = 0
        match_pos = 0
        for j in range(max(0, i - window_size), i):
            k = 0
            while k < buffer_size and i + k < n and data[j + k] == data[i + k]:
                k += 1
            if k > match_len:
                match_len = k
                match_pos = i - j
        if match_len >= 3:
            if i + match_len < n:
                compressed_data.append((match_pos, match_len, data[i + match_len]))
                i += match_len + 1
            else:
                compressed_data.append((0, 0, data[i]))
                i += 1
        else:
            compressed_data.append((0, 0, data[i]))
            i += 1
    result = bytearray()
    for pos, length, char in compressed_data:
        result.extend(pos.to_bytes(2, 'big'))
        result.extend(length.to_bytes(2, 'big'))
        result.append(char)
    return bytes(result)


def LZ77_decode(data):
    i = 0
    n = len(data)
    decompressed_data = bytearray()
    while i < n:
        pos = int.from_bytes(data[i:i + 2], 'big')
        length = int.from_bytes(data[i + 2:i + 4], 'big')
        char = data[i + 4]
        if pos == 0 and length == 0:
            decompressed_data.append(char)
        else:
            start = len(decompressed_data) - pos
            for j in range(length):
                decompressed_data.append(decompressed_data[start + j])
            decompressed_data.append(char)
        i += 5
    return bytes(decompressed_data)