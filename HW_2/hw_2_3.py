import yaml


def write_to_yaml(data):

    with open('file.yaml', 'w') as f_n:
        yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)

    with open('file.yaml') as f_n_1:
        f_n_1_data = yaml.safe_load(f_n_1)

    if data == f_n_1_data:
        res = "Данные равны"
    else:
        res = 'Что-то пошло не так'
    return res

small_data = {
    's_first': '\u20AC'
}
small_list = [1, 2, 3]
data = {
    'first': small_list,
    'second': 123,
    'third': small_data

}
print(write_to_yaml(data))
