import csv
import re


def get_data(file_list):
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта',
                  'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data_files = []

    for file in file_list:
        with open(file) as f_n:
            for row in f_n:
                search_prod = re.match('\Изготовитель системы', row)
                if search_prod is not None:
                    os_prod_list.append(row.split(':')[1].strip())
                search_name = re.match('\Название ОС', row)
                if search_name is not None:
                    os_name_list.append(row.split(':')[1].strip())
                search_code = re.match('\Код продукта', row)
                if search_code is not None:
                    os_code_list.append(row.split(':')[1].strip())
                search_type = re.match('\Тип системы', row)
                if search_type is not None:
                    os_type_list.append(row.split(':')[1].strip())
    for y in range(len(file_list)):
        main_data_files.append([])
        with open(file_list[y]) as f_n_l:
            for row in f_n_l:
                search_prod = re.match('\Изготовитель системы', row)
                if search_prod is not None:
                    main_data_files[y].append(row.split(':')[1].strip())
                search_name = re.match('\Название ОС', row)
                if search_name is not None:
                    main_data_files[y].append(row.split(':')[1].strip())
                search_code = re.match('\Код продукта', row)
                if search_code is not None:
                    main_data_files[y].append(row.split(':')[1].strip())
                search_type = re.match('\Тип системы', row)
                if search_type is not None:
                    main_data_files[y].append(row.split(':')[1].strip())

    main_data.append(main_data_files[0])
    main_data.append(main_data_files[1])
    main_data.append(main_data_files[2])

    return main_data

file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def write_to_csv(file_name):
    with open(file_name, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        f_n_writer.writerows(get_data(file_list))

    with open(file_name) as f_n_r:
        print(f_n_r.read())

write_to_csv('info.csv')



























