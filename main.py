import os
import subprocess


def picture_convertor():
    source = 'Source'
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), source)
    picture_list = os.listdir(path)

    print('Конвертирование началось...')

    source_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Source')
    result_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Result')

    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    for i in picture_list:
        input = os.path.join(source_folder, i)
        output = os.path.join(result_folder, i)
        command = 'convert ' + input + ' -resize 200 ' + output
        subprocess.run(command)
    print('Сконвертированные изображения размещены в папке {}'.format(result_folder))


picture_convertor()
