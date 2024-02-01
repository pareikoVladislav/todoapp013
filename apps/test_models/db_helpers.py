def str_generator():
    for i in range(2, 1_000_000):
        yield f"Задача №{i}"


def generate_default_title():
    return next(str_generator())
