import BitGen as bg
import BitDisplay as bd
import bitmaps as bm

print('Welcome to bitmap generator and displayer!')

while 1:
    print('\nКириллические символы 7х9:')
    bd.display_letters_in_row(bm.letters_ru)
    print('\nперевод картинок в битмап:')
    for i in range(len(bm.bitmaps)):
        try:
            print(f'\nБитмап {i+1}:\t{bm.bitmaps[i]}.png\n')
            hex_matrix = bg.image_to_bitmap(f'BITMAP/{bm.bitmaps[i]}.png', True)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        input('Нажмите Энтер для генерации следующего битмапа . . .')
    input('press any key to relaunch...\t')