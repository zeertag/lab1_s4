import math
import matplotlib.pyplot as plt
from collections import Counter

from compressors import BWT, MTF

with open("files/enwik7.txt", "rb") as file:
    file_data = file.read()


def entropy_calculate(data):
    freq = Counter(data)
    L = len(data)
    entropy = 0
    for f in freq.values():
        p = f / L
        entropy -= p * math.log2(p)
    return entropy


test_blocks = [i for i in range(1000, 10001, 1000)]
entropies = []
for block in test_blocks:
    test = file_data
    encode = MTF.MTF(BWT.BWT(test, block))
    entropies.append(entropy_calculate(encode))


plt.plot(test_blocks, entropies, marker='o')
plt.xlabel('Размер блока (байт)')
plt.ylabel('Энтропия')
plt.title('Зависимость энтропии от размера блока')
plt.grid(True)
plt.show()