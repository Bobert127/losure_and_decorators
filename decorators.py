def capitalize(fn):
    def inner(name):
        result = fn(name)
        result = result.replace(name, f'Mr. {name}')

    return inner


@capitalize
def hello(name):
    return f"Hello {name}"


def goodbye(name):
    return f"Goodbye {name}"

print(hello("robert"))
print(goodbye("robert"))