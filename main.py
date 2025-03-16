from tqdm import tqdm

from compressors import RLE, BWT, MTF, HA, LZ77, LZ78


def print_coeficient(original, compressed, t=0, file=None):
    if t:
        file.write(f"Размер сжатого файла {len(compressed)} байт\n")
    else:
        print(f"Размер сжатого файла {len(compressed)} байт")
    k = len(original) / len(compressed)
    if t:
        file.write(f"Коэффициент сжатия: {k:.3f}\n")
    else:
        print(f"Коэффициент сжатия: {k:.3f}")


def compressors(data, c, t=0, file=None):
    original = data
    if t:
        file.write(f"Размер оригинального файла {len(original)} байт\n")
    else:
        print(f"Размер оригинального файла {len(original)} байт")
    if c == 1:
        compressed = HA.Huffman(data)
        print_coeficient(original, compressed, t, file)
        decompressed = HA.Huffman_decode(compressed)
    elif c == 2:
        compressed = RLE.RLE(data)
        print_coeficient(original, compressed, t, file)
        decompressed = RLE.RLE_decode(compressed)
    elif c == 3:
        compressed = RLE.RLE(BWT.BWT(data))
        print_coeficient(original, compressed, t, file)
        decompressed = BWT.BWT_decode(RLE.RLE_decode(compressed))
    elif c == 4:
        compressed = HA.Huffman(MTF.MTF(BWT.BWT(data)))
        print_coeficient(original, compressed, t, file)
        decompressed = BWT.BWT_decode(MTF.MTF_decode(HA.Huffman_decode(compressed)))
    elif c == 5:
        compressed = HA.Huffman(RLE.RLE(MTF.MTF(BWT.BWT(data))))
        print_coeficient(original, compressed, t, file)
        decompressed = BWT.BWT_decode(MTF.MTF_decode(RLE.RLE_decode(HA.Huffman_decode(compressed))))
    elif c == 6:
        compressed = LZ77.LZ77(data)
        print_coeficient(original, compressed, t, file)
        decompressed = LZ77.LZ77_decode(compressed)
    elif c == 7:
        compressed = HA.Huffman(LZ77.LZ77(data))
        print_coeficient(original, compressed, t, file)
        decompressed = LZ77.LZ77_decode(HA.Huffman_decode(compressed))
    elif c == 8:
        compressed = LZ78.LZ78(data)
        print_coeficient(original, compressed, t, file)
        decompressed = LZ78.LZ78_decode(compressed)
    elif c == 9:
        compressed = HA.Huffman(LZ78.LZ78(data))
        print_coeficient(original, compressed, t, file)
        decompressed = LZ78.LZ78_decode(HA.Huffman_decode(compressed))

    if original == decompressed:
        if t:
            file.write("Файл после декомпрессии совпадает с оригинальным\n\n")
        else:
            print("Файл после декомпрессии совпадает с оригинальным")
    else:
        if t:
            file.write("Неверная декомпрессия\n\n")
        else:
            print("Неверная декомпрессия")
    return 0


def run():
    variants = ["Черно-белое изображение", "Цветное изображение", "Серое изображение", "Файл enwik7", "Файл exe",
                "Текст на русском", "Текст на английском"]
    v = ["bw_img.bmp", "color_img.bmp", "gray_img.bmp2", "enwik7.txt", "EscapeFromTarkov.exe", "rus_text.txt",
         "test.txt"]
    for i in range(1, 8):
        print(f"{i}) {variants[i - 1]}")
    print("8) Создать строку")
    choice = int(input("Выберите файл: "))
    if 0 < choice <= 7:
        with open(f"files/{v[choice - 1]}", "rb") as file:
            data = file.read()
    elif choice == 8:
        data = input("Введите строку: ").encode()
    else:
        return 0
    print(f"Размер файла: {len(data)} байт\n\n")

    variants2 = ["HA", "RLE", "BWT + RLE", "BWT + MTF + HA", "BWT + MTF + RLE + HA", "LZ77", "LZ77 + HA", "LZ78",
                 "LZ78 + HA"]
    for i in range(9):
        print(f"{i + 1}) {variants2[i]}")
    choice2 = int(input("Выберите компрессор: "))
    print()
    compressors(data, choice2)


def auto():
    file = open("Test_Data.txt", "w")

    variants = ["Черно-белое изображение", "Цветное изображение", "Серое изображение", "Файл enwik7", "Файл exe",
                "Текст на русском", "Текст на английском"]
    v = ["bw_img.bmp", "color_img.bmp", "gray_img.bmp", "enwik7.txt", "EscapeFromTarkov.exe", "rus_text.txt",
         "test.txt"]
    variants2 = ["HA", "RLE", "BWT + RLE", "BWT + MTF + HA", "BWT + MTF + RLE + HA", "LZ77", "LZ77 + HA", "LZ78",
                 "LZ78 + HA"]

    total_steps = len(variants) * len(variants2)
    progress_bar = tqdm(total=total_steps, desc="Обработка файлов", ncols=100)

    for test_file in range(len(variants)):
        with open(f"files/{v[test_file]}", "rb") as f:
            data = f.read()
        file.write(f"Файл: {variants[test_file]}\n")

        for compressor in range(len(variants2)):
            file.write(f"Компрессор: {variants2[compressor]}\n")

            compressors(data, compressor + 1, 1, file)
            file.write("\n")

            progress_bar.update(1)

        file.write("-------------------------------------------------------\n")

    progress_bar.close()
    file.close()
    print("Все тесты завершены")

if __name__ == "__main__":
    print("1) Автоматическое выполнение")
    print("2) Ручное тестирование")
    choice = int(input("Выберите вариант работы: "))
    while choice != 1 and choice != 2:
        choice = int(input("Выберите вариант работы: "))

    if choice == 1:
        auto()

    if choice == 2:
        print()
        run()
