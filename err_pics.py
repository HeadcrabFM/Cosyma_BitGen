# Импорт функций из существующего скрипта
from RU_msg import get_text_input, generate_output_string, bitmap_ids
from bitmaps import letters_ru
from PIL import Image



def generate_image(text_ids,picname):
    # Размеры изображения
    char_width = 7
    char_height = 9
    img_width = char_width * len(text_ids)
    img_height = char_height

    # Создаем новое изображение
    image = Image.new('1', (img_width, img_height), 1)  # '1' - черно-белое изображение
    pixels = image.load()

    # Заполняем изображение
    for index, char_id in enumerate(text_ids):
        # Пропускаем пробелы (код 0)
        if char_id == '0':
            continue
        char_id_int = int(char_id)
        # Получаем соответствующий битмап из letters_ru
        bitmap_index = char_id_int - 42
        if bitmap_index < 0 or bitmap_index >= len(letters_ru):
            continue
        bitmap = list(letters_ru.values())[bitmap_index]

        # Рисуем символ
        for y in range(char_height):
            line = bitmap[y]
            for x in range(char_width):
                if line & (1 << (char_width - 1 - x)):
                    # Черный пиксель
                    pixels[index * char_width + x, y] = 0
                else:
                    # Белый пиксель
                    pixels[index * char_width + x, y] = 1

    # Сохраняем изображение
    image.save(f'picgen/{picname}.png')

def main():
    text_name = input("Введите имя переменной: ")
    text = get_text_input("Введите текст (23 символа) МАЛЕНЬКИМИ буквами: ", 23)
    # Генерация выходной строки, которая включает массив с индексами
    ErrText = generate_output_string(text_name, text, bitmap_ids,1)
    # Выводим результат в консоль
    print(ErrText)
    return ErrText



if __name__ == "__main__":
    print ('Welcome to Cosyma RuScreen Shooter!\n')
    while (1):
        generate_image(main(),input('PicName?\t'))
        print("Изображение успешно сгенерировано и перемещено в папку.\n" + '- ' * 13)
