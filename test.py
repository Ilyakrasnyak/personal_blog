MIN_A = 1
MIN_B = 2
MIN_C = 335

MAX_A = 332
MAX_B = 333
MAX_C = 997

a = MIN_A
b = MIN_B
c = MAX_C


def is_py_triplet(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False


while True:
    c = 1000 - a - b
    print(a, b, c)
    if is_py_triplet(a, b, c):
        print('Win!')
        break

    a += 1

    if a > MAX_A:
        b += 1
        a = MIN_A
