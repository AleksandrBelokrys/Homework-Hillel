

def validate_password(*password):
    my_list = ["содержит запрещенные символы", "количество букв должно быть четным",
               "количество цифр должно быть нечетным"]
    my_list_error = list()
    password = str(input("Введите пароль:"))
    if not _validate_symbols(password):
        my_list_error.append(my_list[0])
        return my_list_error
    if not _validate_letters_even(password):
        my_list_error.append(my_list[1])
        return my_list_error
    if not _validate_numbers_odd(password):
        my_list_error.append(my_list[2])
        return my_list_error
    return True


def _validate_symbols(input_str):
    if input_str.isalnum():
        return True
    else:
        return False


def _validate_letters_even(input_str):
    my_list = [value for value in input_str if value.isalpha()]
    if not len(my_list) % 2:
        return True
    else:
        return False


def _validate_numbers_odd(input_str):
    my_list1 = [value for value in input_str if value.isdigit()]
    if len(my_list1) % 2:
        return True
    else:
        return False


print(validate_password())







