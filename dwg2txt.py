"""
Программа для перевода из списка автокад в текстовый файл для разбивки
"""

path = 'Новый текстовый документ.txt'
new_path = 'new file.txt'


def replace_file(file_path, new_path_file):
    with open(file_path, 'r') as file:
        i = 99
        with open(new_path_file, 'w') as f:
            for line in file:
                if line.startswith(' '):
                    line = line.split('X=')[1]
                    line = line.split('=')[:2]
                    new_line = []
                    for el in line:
                        el = el.split(' ')[0]
                        new_line.append(el)
                    i += 1
                    s = '{} {} {}'.format(i, new_line[0], new_line[1])
                    s = s.replace(' ', '	')

                    f.write(s + '\n')


replace_file(path, new_path)
