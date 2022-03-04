
# Here is the recursive solution for exercise 6.4
def is_power(a: int, b: int) -> bool:
    '''
    :param: a: int
    :param: b: int
    :return: True if a is power of b else, False
    '''
    if a == b:
        return True
    elif a % b == 0 and is_power(a / b, b):
            return True
    else:
        return False


if __name__ == '__main__':
    print(is_power(64, 2))
    print(is_power(27, 3))
    print(is_power(16384, 4))
