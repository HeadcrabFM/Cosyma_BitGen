import os
from PIL import Image
import BitDisplay as bs
import bitmaps as bm


def image_to_bitmap(image_path, display=bool):
    if image_path == "null":
        image_path = input("Путь к картинке:\t")
    # Открыть изображеие получить размеры
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Файл {image_path} не найден")

    image = Image.open(image_path)
    width, height = image.size
    image = image.convert("RGBA")
    pixels = image.load()
    matrix = []  # бинарная матрица
    for y in range(height):
        binary_string = ""
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                binary_string += "0"
            else:
                binary_string += "1"
        matrix.append(binary_string)

    hex_matrix = []
    for binary_string in matrix:
        binary_string = binary_string.zfill(width)
        hex_value = hex(int(binary_string, 2))[2:].zfill(width // 4)
        hex_matrix.append(f'0x{hex_value}')

    print(hex_matrix)
    if display == True:
        bs.hex_bitmap_to_string(hex_matrix)

    return hex_matrix


if __name__ == "__main__":
    for i in range(len(bm.bitmaps)):
        try:
            hex_matrix = image_to_bitmap(f'{bm.folder}/{bm.bitmaps[i]}.png', True)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
