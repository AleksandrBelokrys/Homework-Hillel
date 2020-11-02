from datetime import date
# d = date(1969, 6, 26) - конструктор даты
# d.year < 2020 - проверка даты

# database - список словарей, эмулирующий базу данных со строками и полями
database = [{"first_name": "Alex", "last_name": "Bilokrys",
             "birth": date(1969, 6, 27), "email": "iamguido@python.org"},
            {"first_name": "Guido", "last_name": "Ivanov",
             "birth": date(1999, 6, 27), "email": "iamguido@gmail.org"},
            {"first_name": "Guido", "last_name": "But Van Rossum",
             "birth": date(1969, 6, 28), "email": "iamanotherguido@pythonorg"}]


def _validate_input(data: tuple) -> bool:
    """
    Функция принимает кортеж словарей, валидирует каждый из словарей на наличие
    всех необходимых полей и тип их данных. Возвращает bool в зависимости от результатов проверки.
    Правила валидации:
    first_name - string, не пустой, короче 48 символов
    last_name - string, не пустой, короче 64 символов
    birth - date, не пустой, не в будущем, не старше 100 лет
    email - string, формат строка, затем @, затем опять строка, точка,
    строка от 2 до 3 символов
    Допустимые символы в email: буквы, цифры
    """
    first_name_len = 48
    last_name_len = 64
    max_age = 100
    for row in data:
        if not _validate_name(row['first_name'], first_name_len):
            return False
        if not _validate_name(row['last_name'], last_name_len):
            return False
        if not _validate_birth(row['birth'], max_age):
            return False
        if not _validate_email(row['email']):
            return False

    return True


def _validate_name(name, max_len):
    if not type(name) is str:
        return False
    if not 0 < len(name) < max_len:
        return False
    return True


def _validate_birth(birth, max_age):
    if not type(birth) is date:
        return False
    if birth > date.today():
        return False
    if date.today().year - birth.year > max_age:
        return False
    return True


def _validate_email(email):
    if not type(email) is str:
        return False
    email_parts = email.split('@')
    if len(email_parts) != 2:
        return False
    if not email_parts[0].isalnum():
        return False
    domain_parts = email_parts[1].split('.')
    if len(domain_parts) == 1:
        return False
    if not 2 <= len(domain_parts[-1]) <= 3:
        return False
    return True


def insert_to_db(data: tuple) -> bool:
    """
    Функция принимает кортеж словарей с данными, валидирует каждую запись с
    помощью вспомогательной функции validate_input, и если данные валидны,
    добавляет их в database.
    Возвращает bool по результатам успешного/неуспешного выполнения.
    """
    if _validate_input(data):
        database.extend(list(data))
        return True

    return False


def _format_output(data):
    """
    Принимает тапл диктов с данными из БД.
    Форматирует данные в таблицу вида:
    ---------------------------------------
    | название колонки | название колонки |
    ---------------------------------------
    | значение строки  | значение колонки |
    Возвращает таблицу строкой.
    """
    # смещение
    offset = 13

    def _find_max_length(data_tuple: tuple, field: str) -> int:
        max_len = 0

        if data_tuple:
            max_len = max([len(item[field]) for item in data_tuple])

        if max_len < len(field):
            return len(field)
        else:
            return max_len

    max_len_first_name = _find_max_length(data, 'first_name')
    max_len_last_name = _find_max_length(data, 'last_name')
    max_len_birth = 10
    max_len_email = _find_max_length(data, 'email')

    horizontal_line_len = max_len_first_name + max_len_last_name + max_len_birth + max_len_email + offset
    horizontal_line = '-' * horizontal_line_len
    table = horizontal_line

    table += '\n'
    table += f"| {'first_name':{max_len_first_name}} "
    table += f"| {'last_name':^{max_len_last_name}} "
    table += f"| {'birth_name':{max_len_birth}} "
    table += f"| {'email':^{max_len_email}} |"
    table += '\n'
    table += horizontal_line

    for row in data:
        table += '\n'
        table += f"| {row['first_name']:^{max_len_first_name}} "
        table += f"| {row['last_name']:^{max_len_last_name}} "
        table += f"| {str(row['birth']):^{max_len_birth}} "
        table += f"| {row['email']:^{max_len_email}} |"
        table += '\n'
        table += horizontal_line

    return table


def select_from_db(field: str, value: str):
    """
    Функция возвращает таблицу (строка) с релевантными результатами, где переданное значение встречается в переданном ключе.
    Форматирование результатов выполняет вспомогательная функция _format_output
    """

    selected = filter(lambda item: item[field] == value, database)
    selected = tuple(selected)

    return _format_output(selected)


in_data = ({"first_name": "Guido", "last_name": "Van Rossum",
            "birth": date(1969, 6, 27), "email": "iamguido@python.org"},
            {"first_name": "Not Guido", "last_name": "But Van Rossum",
            "birth": date(1969, 6, 28), "email": "iamanotherguido@pythonorg"})
result = insert_to_db(in_data)
# print(result)
# print(database)
print(select_from_db("first_name", "Guido"))
print(select_from_db("last_name", "Bilokrys"), '\n')
print(select_from_db("email", "o@pythonorg"), '\n')
print(_format_output(database))