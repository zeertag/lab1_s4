def RLE(data):
    compressed_data = bytearray()
    i = 0
    while i < len(data):
        len_repeating = 1
        while i + len_repeating < len(data) and data[i] == data[i + len_repeating] and len_repeating < 255:
            len_repeating += 1

        if len_repeating > 1:
            compressed_data.append(len_repeating)
            compressed_data.append(data[i])
            i += len_repeating
        else:
            start_unic = i
            while i < len(data) - 1 and (data[i] != data[i + 1]) or (i > start_unic and data[i] == data[i - 1]):
                i += 1
                if i - start_unic >= 254:
                    break
            len_unic = i - start_unic + 1
            compressed_data.append(0)
            compressed_data.append(len_unic)
            compressed_data.extend(data[start_unic:i + 1:])
            i += 1

    return bytes(compressed_data)


def RLE_decode(data):
    original = bytearray()
    i = 0
    while i < len(data):
        if data[i] == 0:
            len_unic = data[i + 1]
            original.extend(data[i + 2:i + 2 + len_unic])
            i += 2 + len_unic
        else:
            len_repeat = data[i]
            original.extend([data[i + 1]] * len_repeat)
            i += 2
    return bytes(original)
