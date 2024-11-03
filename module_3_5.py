# Создаем функцию get_multiplied_digits с параметром number в ней, а также создаем
# переменную str_number и строковое (str) числа number в ней.
def get_multiplied_digits(n):
    str_number = str(n)
# По условию задачи создаём переменную first и записываем в неё первый символ из str_number
# в числовом представлении(int)
    first = int(str_number[0])
# Следующий шаг можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном
# случае не получится взять срез str_number[1:].
# здесь комп встает на паузу и переходит к выполнению следующей задачи, проверке условия:
# Если длина str_number не больше 1, тогда вернуть оставшуюся цифру first.

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) < 2:
        return first

# Стек вызовов будет выглядеть следующим образом:
# При преобразовании строки(str) в число(int) первые нули будут убираться.

# get_multiplied_digits(40203) -> # 4 * get_multiplied_digits(203) ->
# 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3

result = get_multiplied_digits(40203)
print(result)
