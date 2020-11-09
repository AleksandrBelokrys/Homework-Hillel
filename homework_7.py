from os import listdir
from os.path import isfile, join


def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }

        def wrapper(text):
            html_code = text

            for tag in tags[::-1]:
                try:
                    base = tag_base[tag]
                    html_code = base.replace('%text%', html_code)
                except KeyError:
                    return f'{tag} - this tag is not available!'

            return html_code

        return wrapper

    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text


print(get_text("qwerty"))

###############################################################


def log_reading(func):

    def wrapper(*args):
        files_list = func(*args)
        for value in files_list:
            if ".log" in value:
                f = open(value, "r")
                data = f.read()
                f.close()
                return data

    return wrapper


@log_reading
def get_files(path):
    file_list = [file for file in listdir(path) if isfile(join(path, file))]
    return file_list


print(get_files(r"C:\Users\Admin\PycharmProjects\homework"))