

def do_cache(maxsize=None):
    def decorator(func):
        cache = dict()

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            if len(cache) > maxsize:
                cache.popitem()

            return cache[key]

        return wrapper
    return decorator


@do_cache(maxsize=3)
def my_func(x, y, v=5, b=3):
    return x * y * v * b


print(my_func(5, 76, v=6, b=7))
print(my_func(5, 76, v=6, b=7))










