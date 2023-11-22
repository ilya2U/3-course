import string
import pandas as pd


"""Ввод алфавита"""
alphabet_english = False
alphabet_user = sorted(list(set(input('Введите алфавит: ').replace(' ', '').lower())))
alphabet_digit = string.digits


def alphabet_with_alpha(alphabet):
    global alphabet_english
    for alpha in alphabet:
        if alpha.isalpha():
            if alpha in string.ascii_letters:
                alphabet_english = True
            else:
                if alphabet_english:
                    print('Error\nНедопустимые символы!')
                    quit()
        else:
            print('Error\nНедопустимые символы!')
            quit()
        if alphabet[0] not in string.ascii_lowercase and alphabet_english:
            print('Error\nНедопустимые символы!')
            quit()
    print('Алфавит подходит')


def alphabet_with_number(alphabet):
    counter = 0
    for i in alphabet:
        if i in alphabet_digit:
            counter += 1
    if counter != len(alphabet):
        alphabet_with_alpha(alphabet)
    else:
        print(f'Алфавит подходит')


alphabet_with_number(alphabet_user)
alphabet_user.append('e')
print(alphabet_user)
"""Вводим вершины"""
lst1_peaks_finish = list()  # список финальных вершин
lst1_peaks_start = list()   # список начальных вершин


def input_peaks():
    global lst1_peaks_start, lst1_peaks_finish
    list_peaks = list()

    question_peaks_start = input('Введите начальную вершину: ').replace(' ', ',').split(',')
    lst1_peaks_start = question_peaks_start  # присваиваю начальные вершины для дальнейших операций с ними
    list_peaks += question_peaks_start

    question_peaks_finish = input('Введите финальную вершину: ').replace(' ', ',').split(',')
    lst1_peaks_finish = question_peaks_finish  # присваиваю финальный вершины для дальнейшей работы с ними

    question_peaks = input('Введите промежуточные вершины: ').replace(' ', ',').split(',')
    list_peaks += question_peaks

    list_peaks += question_peaks_finish

    return list_peaks


lst1_peaks = input_peaks()  # список написанных пользователем вершин
print(lst1_peaks)
"""Ввод переходов"""


def routes_peaks(list_peak):
    graph = dict()
    for peaks in list_peak:
        counter = 0
        routes = set(input(f'Введите в какие вершины можно попасть из вершины {peaks}: ').replace(' ', ',').lower().
                     split(','))
        for route in routes:
            if route in list_peak or route == '':
                counter += 1
                if counter == len(routes):
                    graph[peaks] = list(routes)
            else:
                print('Такой вершины не существует!')
                quit()

    return graph


dict1_graph = routes_peaks(lst1_peaks)  # строим граф
print(f'Из каких вершин и в какие мы можем попасть = {dict1_graph}\n')

"""Какие рёбра к какой вершине идут"""


def alphabet_ribs_peaks(graph):
    index = None  # индекс вершины где рёбер больше всего
    max_ribs = 0  # максимальное кол-во рёбер
    for peak in graph:
        if len(graph[peak]) > max_ribs:
            index = peak
            max_ribs = len(graph[index])
    pass_dict = {rout: None for rout in graph for i in range(max_ribs)}
    df = pd.DataFrame(pass_dict, index=lst1_peaks)
    for keys, values in graph.items():
        for i in values:
            if i != '':
                user_ask = input(f'Каким ребром можно попасть из {keys} в {i}?\n')
                if user_ask in alphabet_user:
                    df[keys][i] = user_ask
            else:
                print(f'У вершины {keys} отсутствуют переходы в какие-либо вершины\n')
                continue
    return df


df_from_graph = alphabet_ribs_peaks(dict1_graph)  # граф
print('Граф:')
print(df_from_graph)


"""Создаём S"""


def create_s(df_graph):
    global alphabet_user, lst1_peaks
    alphabet_user.remove('e')
    list_with_name_s = list()
    counter = 0
    """Создаю имена для S"""
    for i in range(len(lst1_peaks)):
        list_with_name_s.append(f's{counter}')
        counter += 1

    """Пользователь вводит значения S"""
    dict_with_s = dict()
    for name_s in list_with_name_s:
        error = True
        while error:
            ask_user_about_s_value = list(set(input(f'Введите значения {name_s}: ').replace(' ', ',').split(',')))
            counter_for_s_value = 0
            for value_s in ask_user_about_s_value:
                if value_s not in lst1_peaks:
                    print('Такой вершины не существует!\nПопробуйте ещё раз')
                else:
                    counter_for_s_value += 1
                    if counter_for_s_value == len(ask_user_about_s_value):
                        error = False
                        dict_with_s[name_s] = ask_user_about_s_value
    return dict_with_s


dict_s_with_values = create_s(df_from_graph)  # словарь с S и вершинами, которые ввёл пользователь
print(dict_s_with_values)

"""Заполняем таблицу с S"""


def create_table_s(dict_s):
    global alphabet_user
    list_with_table_index = list()
    """Создаём индексы для DF"""
    for name_s in dict_s:
        pass_string = str()
        pass_string += name_s
        list_with_table_index.append(pass_string)
    df_with_s = pd.DataFrame(columns=alphabet_user, index=list_with_table_index)
    print(df_with_s)
    print()
    """Даём пользователю заполнить таблицу с S"""

    keys_dict_s = list(dict_s.keys())
    keys_dict_s.append('NaN')

    for columns, index in df_with_s.items():
        test_for_index = True
        counter_for_index_df = 0
        while test_for_index:
            test_for_value = True
            while test_for_value:
                counter_for_value = 0
                user_input_values_s = input(f'Введите что-то для колонны {columns} в строчке'
                                            f' {df_with_s.index[counter_for_index_df]}: ')
                user_input_values_s_list = user_input_values_s.split(' ')
                for value in user_input_values_s_list:
                    if value not in keys_dict_s:
                        print('Такого S не существует попробуйте ещё раз')
                    else:
                        counter_for_value += 1
                        if counter_for_value == len(user_input_values_s_list):
                            df_with_s[columns][counter_for_index_df] = user_input_values_s
                            test_for_value = False
                            counter_for_index_df += 1
                            if counter_for_index_df == len(index):
                                test_for_index = False
    return df_with_s


table_s = create_table_s(dict_s_with_values)
print('Таблица S:')
print(table_s)


"""Создаём начальное P0"""


def start_p():
    global lst1_peaks_start, df_from_graph
    lst_for_index = list() + lst1_peaks_start
    for peak in lst1_peaks_start:
        for column, values in df_from_graph.items():
            counter_for_index = -1
            if column == peak:
                for value in values:
                    counter_for_index += 1
                    if 'e' == value:
                        index_e = df_from_graph.index
                        lst_for_index.append(index_e[counter_for_index])
    for peak in lst_for_index:
        for column, values in df_from_graph.items():
            counter_for_ind = -1
            if column == peak and column not in lst_for_index:
                for value in values:
                    counter_for_ind += 1
                    if 'e' == value:
                        index_e = df_from_graph.index
                        lst_for_index.append(index_e[counter_for_ind])
    return lst_for_index


start_peaks_for_p = start_p()  # вершины до которых можно добраться из начальной по Е
print('Вершины к которым можно добраться из начальной по E = ', start_peaks_for_p)
"""Создаём P таблицу"""
finish_dict_with_p = 0


def create_table_p(start_for_p, dict_with_s):
    global alphabet_user, table_s, finish_dict_with_p
    dict_with_p = dict()
    list_with_s_for_p0 = list()
    for s in dict_with_s:
        if sorted(dict_with_s[s]) == sorted(start_for_p):  # для того чтобы они стали точно одинаковыми
            list_with_s_for_p0.append(s)
        if len(dict_with_s[s]) == 1:
            for peak in start_for_p:
                if peak == dict_with_s[s][0]:
                    list_with_s_for_p0.append(s)
    dict_with_p['p0'] = list_with_s_for_p0  # здесь мы p0 равняем начальным S
    print()
    print('Показывает чему равно p0: ', dict_with_p)
    df_for_p = pd.DataFrame(index=['p0'], columns=alphabet_user)  # df только с p0
    counter_for_p = 1
    counter_tr = 0
    pp = 0
    new_dict_with_p = dict()

    for columns in table_s:
        for keys, values in dict_with_p.items():
            for value in values:
                if value != 'NaN':
                    column_table_s = table_s[columns]
                    index_table_s = column_table_s[value]
                    counter_tr += 1
                    if counter_tr == len(values):
                        df_for_p[columns][keys] = keys
                        counter_tr = 0
                    else:
                        if sorted(index_table_s.split(' ')) != sorted(dict_with_p['p0']) and pp != \
                                sorted(index_table_s.split(' ')):
                            new_dict_with_p[f'p{counter_for_p}'] = index_table_s.split(' ')
                            pp = sorted(index_table_s.split(' '))
                            counter_for_p += 1
                else:
                    continue
    finish_dict_with_p = dict_with_p | new_dict_with_p
    print('Все P = ', finish_dict_with_p)
    p = [i for i in finish_dict_with_p]
    df_p = pd.DataFrame(columns=alphabet_user, index=p)
    """Заполняем таблицу с P"""
    for columns in table_s:
        for values in finish_dict_with_p:
            for value in finish_dict_with_p[values]:
                val_s = sorted(table_s[columns].loc[value].split(' '))
                for val in finish_dict_with_p:
                    if val_s == sorted(finish_dict_with_p[val]):
                        df_p[columns].loc[values] = val
    print('Таблица P:')
    return df_p


table_p = create_table_p(start_peaks_for_p, dict_s_with_values)
print(table_p)


"""Проверка"""


def chain_check():
    global table_p, alphabet_user, lst1_peaks_finish, dict_s_with_values, finish_dict_with_p
    all_s = [s for s in dict_s_with_values]  # finish S
    s_start = finish_dict_with_p['p0']
    for s in s_start:
        all_s.remove(s)
    lst_finish_p = list()
    list_for_chain = list()
    control_input = True
    index_table_p = table_p.index
    user_chain = 0
    list_for_chain.append(index_table_p[0])

    while control_input:
        user_chain = input('Введите цепочку для проверки: ').split(' ')
        counter_len_user_chain = len(user_chain)
        t1 = 'p0'
        for alpha in user_chain:
            if alpha == 'NaN' and counter_len_user_chain != 0:
                print('Не допущена')
            if alpha in alphabet_user:
                counter_len_user_chain -= 1
                tt = table_p[alpha].loc[t1]
                t1 = tt
                index_p = tt
                list_for_chain.append(index_p)
            else:
                print('Такой буквы нет в алфавите\nПопробуйте ещё раз')

        control_input = False
    for s in all_s:
        for p in finish_dict_with_p:
            if s in finish_dict_with_p[p]:
                lst_finish_p.append(p)
    if list_for_chain[-1] in lst_finish_p:
        print('Цепочка допущена')
        print(['p0', user_chain])
    else:
        if isinstance(list_for_chain[-1], float):
            print('Цепочка допущена')
        else:
            print('Цепочка не допущена')
            quit()

    for p in list_for_chain[1::]:
        try:
            print([p, user_chain[1::]])
            user_chain = user_chain[1::]
        except IndexError:
            print([p, user_chain])
            if len(user_chain) != 0:
                user_chain = []
            else:
                quit()


chain_check()
