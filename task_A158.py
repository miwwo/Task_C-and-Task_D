# Написать функцию palindrom, которая определяет является ли заданное число палиндромом
# (читается одинаково слева направо и справа налево)
#
# Пример:
# palindrom(1234321) ==> True

import traceback


def palindrom(num):
    a = str(num)
    flag = 0
    length = len(a)-1
    for i in range(0, length//2+1):
        if a[i] == a[length-i]:
            flag = 0
        else:
            flag = 1
            break
    if flag == 0:
        return True
    else:
        return False


# Тесты
try:
    assert palindrom(0) == True
    assert palindrom(1233221) == False
    assert palindrom(1000010) == False
    assert palindrom(5555555) == True
    assert palindrom(1234554321) == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
