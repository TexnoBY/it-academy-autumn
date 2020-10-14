"""
Даны два списка чисел.
Посчитайте, сколько различных чисел входит только в один из этих списков
"""


def diff(lst1, lst2):
    return len(set(lst1) ^ set(lst2))


if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst2 = [5, 6, 7, 8, 9, 0, 12, 23]
    print(diff(lst1, lst2))
