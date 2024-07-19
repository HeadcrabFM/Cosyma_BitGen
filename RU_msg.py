import os

# Создаем маппинг символов на ID битмапа
bitmap_ids = {
    ' ': 0, '.': 1, ',': 2, '!': 3, '%': 4, '?': 5,
    '0': 6, '1': 7, '2': 8, '3': 9, '4': 10, '5': 11,
    '6': 12, '7': 13, '8': 14, '9': 15, '*': 86
}

# Добавляем кириллические символы
cyrillic_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for i, char in enumerate(cyrillic_chars, start=42):
    bitmap_ids[char] = i

def get_text_input(prompt, length):
    while True:
        text = input(prompt)
        if len(text) > length:
            print(f"Текст слишком длинный. Введите текст не более {length} символов.")
        else:
            return text.ljust(length)  # Добавить пробелы до необходимой длины

def generate_output_string(text_name, text, bitmap_ids):
    text_ids = []
    for char in text:
        if char in bitmap_ids:
            text_ids.append(str(bitmap_ids[char]))
        else:
            print(f"Предупреждение: символ '{char}' не найден в маппинге, заменён на 0.")
            text_ids.append(str(0))
    return f"{text_name}[N_Chars] =\t{{{','.join(text_ids)}}},\t// {text}"

def append_to_file(filename, content):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content + '\n')

def main():
    text_name = input("Введите имя переменной: ")
    text = get_text_input("Введите текст (23 символа) МАЛЕНЬКИМИ буквами: ", 23)
    output_string = generate_output_string(text_name, text, bitmap_ids)
    append_to_file('NS3_RuTexts.txt', output_string)
    print("Строка успешно добавлена в файл.\n"+'- '*13)

if __name__ == "__main__":
    print('W E L C O M E to Cosyma bitmap generator!\nР У С И Ф И К А Ц И Я\n\n'+'* '*13)
    while(1):
        main()
