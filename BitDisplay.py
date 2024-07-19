import bitmaps as bm

pix = '++'
void = '  '
sep = ''


# Функция для отображения всех сгенеренных букв в строку
def display_letters_in_row(matrices):
    # Создаем 9 строк для вывода
    rows = ['' for _ in range(9)]

    # Обрабатываем каждую букву
    for letter, matrix in matrices.items():
        for i, row in enumerate(matrix):
            binary_str = format(row, '07b')  # преобр. в 7-битное бинарное представление
            rows[i] += ' '.join(
                pix if bit == '1' else void for bit in binary_str) + sep  # расстояне между буквами
    # Печатаем строки
    for row in rows:
        print(row)


def hex_bitmap_to_string(hex_bitmap):
    # Функция для преобразования одной шестнадцатеричной строки в бинарную строку
    def hex_to_binary(hex_str):
        # Преобразуем шестнадцатеричную строку в число, а затем в бинарную строку
        binary_str = bin(int(hex_str, 16))[2:]
        # Добавляем ведущие нули, чтобы длина строки была 16 битов
        return binary_str.zfill(16)

    # шестнадцатеричные строки в бинарне
    binary_matrix = [hex_to_binary(hex_str) for hex_str in hex_bitmap]

    formatted_matrix = []
    for binary_string in binary_matrix:
        formatted_string = ''.join(pix if bit == '1' else void for bit in binary_string)
        formatted_matrix.append(formatted_string + sep)  # Добавляем табуляцию между строками

    for row in formatted_matrix:
        print(row)
    print('\n', end='')


if __name__ == "__main__":
    # Тестовый вывод всех букв в строку
    display_letters_in_row(bm.letters_ru)
