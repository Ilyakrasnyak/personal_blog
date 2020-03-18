def example(e1, e2):
    return e1 + 10 + e2


list_1 = [i for i in range(10)]
list_2 = [i * 2 for i in range(2)]
list_3 = [i / 2 for i in range(10)]

list_1 = dict(map(lambda *args: args, list_1, list_2))
print(list_1)