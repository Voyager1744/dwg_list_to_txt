"""
Программа для перевода из списка автокад в текстовый файл для разбивки
"""

RAW_FILE = 'Новый текстовый документ.txt'
NEW_FILE = 'new file_test.txt'
START = 100


def read_file(file_path):
    data_list = []
    for line in open(file_path):
        data_list.append(line)
    return data_list


def write_file(new_path_file, replaces_list):
    with open(new_path_file, 'w') as f:
        f.writelines(replaces_list)


# def replace_file(file_path, new_path_file, start_point):
#     with open(file_path, 'r') as file:
#         i = start_point - 1
#         with open(new_path_file, 'w') as f:
#             for line in file:
#                 if line.startswith(' '):
#                     line = line.replace('          в точке  X=', ' ')
#                     line = line.replace('  Y=', ' ')
#                     new_line = line.split()
#                     i += 1
#                     s = '{} {} {}'.format(i, new_line[0], new_line[1])
#                     s = s.replace(' ', '	')
#
#                     f.write(s + '\n')


def replace_data(data_list, start_point):
    replaces_list = []
    i = start_point - 1
    for line in data_list:
        if line.startswith(' '):
            line = line.replace('          в точке  X=', ' ')
            line = line.replace('  Y=', ' ')
            new_line = line.split()
            i += 1
            s = '{}\t{}\t{}\n'.format(i, new_line[0], new_line[1])
            replaces_list.append(s)
    return replaces_list


if __name__ == '__main__':
    # replace_file(path, new_path, START)
    data = replace_data(read_file(RAW_FILE), START)
    write_file(NEW_FILE, data)
