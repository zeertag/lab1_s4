import matplotlib.pyplot as plt

from compressors import LZ77

with open("files/enwik7.txt", "rb") as file:
    file_data = file.read()

buffer_sizes = [256, 512, 1024, 2048]
coefficient = []

for b in buffer_sizes:
    test = file_data
    encode = LZ77.LZ77(test, b)
    c = len(test) / len(encode)
    print(b, len(encode))
    coefficient.append(c)

plt.plot(buffer_sizes, coefficient, marker='o')
plt.xlabel('Размер буфера (байт)')
plt.ylabel('Коэффициент сжатия')
plt.title('Зависимость коэффициента сжатия от размера буфера в LZ77')
plt.grid(True)
plt.show()