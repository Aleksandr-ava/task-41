def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in range(len(numbers)):
        try:
            result += numbers[i]
        except TypeError:
            print(f'Некорректный тип данных для подсчета суммы – {numbers[i]}')
            incorrect_data += 1

    return result


def calculate_average(numbers):
    try:
        int_ = [x for x in numbers if type(x) == int]
        srednee = personal_sum(numbers) / len(int_)
        return srednee
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
