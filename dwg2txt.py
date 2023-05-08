"""
Программа для перевода из списка автокад в текстовый файл для разбивки
"""

path = 'Новый текстовый документ.txt'
new_path = 'new file.txt'
START = 100


def replace_file(file_path, new_path_file, start_point):
    with open(file_path, 'r') as file:
        i = start_point - 1
        with open(new_path_file, 'w') as f:
            for line in file:
                if line.startswith(' '):
                    line = line.replace('          в точке  X=', ' ')
                    line = line.replace('  Y=', ' ')
                    new_line = line.split()
                    i += 1
                    s = '{} {} {}'.format(i, new_line[0], new_line[1])
                    s = s.replace(' ', '	')

                    f.write(s + '\n')


if __name__ == '__main__':
    replace_file(path, new_path, START)
