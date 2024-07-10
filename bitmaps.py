import os


def pix_list(directory):
    pixnames = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            pixname = os.path.splitext(file)[0]
            pixnames.append(pixname)
    return pixnames


# Пиксельные матрицы для кириллического алфавита 7х9.
# Да, я не нашёл эти битмапы в опенсорсе.
# Да, мне нужно именно такое разрешение :D
letters_ru = {
    "А": [0x00, 0x18, 0x24, 0x42, 0x42, 0x7e, 0x42, 0x42, 0x00],
    "Б": [0x00, 0x7E, 0x40, 0x40, 0x7C, 0x42, 0x42, 0x7C, 0x00],
    "В": [0x00, 0x7C, 0x42, 0x42, 0x7C, 0x42, 0x42, 0x7C, 0x00],
    "Г": [0x00, 0x7E, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x00],
    "Д": [0x00, 0x1C, 0x24, 0x24, 0x24, 0x24, 0x24, 0x7E, 0x42],
    "Е": [0x00, 0x7E, 0x40, 0x40, 0x7E, 0x40, 0x40, 0x7E, 0x00],
    "Ё": [0x14, 0x7E, 0x40, 0x40, 0x7E, 0x40, 0x40, 0x7E, 0x00],
    "Ж": [0x00, 0x2A, 0x2A, 0x2A, 0x1C, 0x2A, 0x2A, 0x2A, 0x00],
    "З": [0x00, 0x3C, 0x42, 0x04, 0x18, 0x04, 0x42, 0x3C, 0x00],
    "И": [0x00, 0x42, 0x42, 0x46, 0x4A, 0x52, 0x62, 0x42, 0x00],
    "Й": [0x18, 0x42, 0x42, 0x46, 0x4A, 0x52, 0x62, 0x42, 0x00],
    "К": [0x00, 0x42, 0x44, 0x48, 0x70, 0x48, 0x44, 0x42, 0x00],
    "Л": [0x00, 0x0E, 0x12, 0x22, 0x22, 0x22, 0x22, 0x62, 0x00],
    "М": [0x00, 0x41, 0x63, 0x55, 0x49, 0x41, 0x41, 0x41, 0x00],
    "Н": [0x00, 0x42, 0x42, 0x42, 0x7E, 0x42, 0x42, 0x42, 0x00],
    "О": [0x00, 0x3C, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C, 0x00],
    "П": [0x00, 0x7E, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x00],
    "Р": [0x00, 0x7C, 0x42, 0x42, 0x7C, 0x40, 0x40, 0x40, 0x00],
    "С": [0x00, 0x3C, 0x42, 0x40, 0x40, 0x40, 0x42, 0x3C, 0x00],
    "Т": [0x00, 0x3E, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x00],
    "У": [0x00, 0x42, 0x42, 0x42, 0x3E, 0x02, 0x02, 0x3C, 0x00],
    "Ф": [0x00, 0x1C, 0x2A, 0x2A, 0x2A, 0x1C, 0x08, 0x08, 0x00],
    "Х": [0x00, 0x22, 0x22, 0x14, 0x08, 0x14, 0x22, 0x22, 0x00],
    "Ц": [0x00, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x7F, 0x01],
    "Ч": [0x00, 0x42, 0x42, 0x42, 0x3E, 0x02, 0x02, 0x02, 0x00],
    "Ш": [0x00, 0x42, 0x42, 0x4A, 0x4A, 0x4A, 0x4A, 0x7E, 0x00],
    "Щ": [0x00, 0x44, 0x44, 0x54, 0x54, 0x54, 0x54, 0x7E, 0x03],
    "Ъ": [0x00, 0x70, 0x10, 0x10, 0x1C, 0x12, 0x12, 0x1C, 0x00],
    "Ы": [0x00, 0x42, 0x42, 0x42, 0x7A, 0x46, 0x46, 0x7A, 0x00],
    "Ь": [0x00, 0x40, 0x40, 0x40, 0x7C, 0x42, 0x42, 0x7C, 0x00],
    "Э": [0x00, 0x3C, 0x42, 0x02, 0x1E, 0x02, 0x42, 0x3C, 0x00],
    "Ю": [0x00, 0x4C, 0x52, 0x52, 0x72, 0x52, 0x52, 0x4C, 0x00],
    "Я": [0x00, 0x3E, 0x42, 0x42, 0x3E, 0x12, 0x22, 0x42, 0x00]
}
#    "": [],
battery = {
    "left": [0x03, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x03],
    "right": [0x40, 0x40, 0x40, 0x70, 0x10, 0x70, 0x40, 0x40, 0x40],
    "empty": [0x7F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7F],
    "full": [0x7F, 0x00, 0x7E, 0x7E, 0x7E, 0x7E, 0x7E, 0x00, 0x7F],
    "f-left": [0x7F, 0x40, 0x5E, 0x5E, 0x5E, 0x5E, 0x5E, 0x40, 0x7F],
    "f-right": [0x7C, 0x04, 0x74, 0x77, 0x71, 0x77, 0x74, 0x04, 0x7C]
}

bitmaps = pix_list('BITMAP')