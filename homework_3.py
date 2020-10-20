from collections import Counter


def catalog_finder(url_list):
    result_list = list()
    for value in url_list:
        if '/catalog/' in value:
            result_list.append(value)
    return result_list


def get_str_center(input_str):
    if len(input_str) % 2:
        output_str = input_str[(len(input_str) // 2) - 1:(len(input_str) // 2) + 2]
    else:
        output_str = input_str[(len(input_str) // 2) - 1:(len(input_str) // 2) + 1]
    return output_str


def count_symbols(input_str):
    output_dict = dict(Counter(input_str))
    return output_dict


def mix_strings(str1, str2):
    mid_str1 = len(str1) // 2
    result_str = str1[:mid_str1] + str2 + str1[mid_str1:]
    return result_str


def even_int_generator():
    even_int_list = [i for i in range(0, 100) if not i % 2]
    return even_int_list
































