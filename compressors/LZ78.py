def LZ78(data):
    dictionary = {}
    output = []
    index = 1
    buffer = b''
    for byte in data:
        new_buffer = buffer + bytes([byte])
        if new_buffer in dictionary:
            buffer = new_buffer
        else:
            output.append((dictionary.get(buffer, 0), byte))
            dictionary[new_buffer] = index
            index += 1
            buffer = b''
    if buffer:
        output.append((dictionary.get(buffer, 0), None))
    encoded = b''
    for idx, byte in output:
        encoded += idx.to_bytes(3, 'big') + (bytes([byte]) if byte is not None else b'')
    return encoded


def LZ78_decode(data):
    dictionary = {0: b''}
    output = b''
    index = 1
    i = 0
    while i < len(data):
        idx = int.from_bytes(data[i:i + 3], 'big')
        i += 3
        byte = data[i:i + 1] if i < len(data) else b''
        i += len(byte)
        entry = dictionary[idx] + byte
        output += entry
        dictionary[index] = entry
        index += 1
    return output