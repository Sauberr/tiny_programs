import random


def input_matrix(result):
    for i in result:
        print(str(i).replace(',', ''))
        

def transport_matrix(matrix_1):
    rows = len(matrix_1)
    cols = len(matrix_1[0])
    transposed_matrix = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix_1[i][j])
        transposed_matrix.append(new_row)
    return transposed_matrix


def multiplication_matrix_by_number(matrix_1):
    try:
        number = input('Ведите число на какой будете умножать матрицу : ')
        number = int(number)
        result = []
        for i in range(len(matrix_1)):
            rows = []
            for j in range(len(matrix_1)):
                rows.append(matrix_1[i][j] * int(number))
            result.append(rows)
        return result
    except (TypeError, ValueError):
         print('Ведите число а не символы')


def random_generate_matrix_values():
    rows = int(input('Ведите количество строк матрицы: '))
    columns = int(input('Ведите количество столбцов матрицы : '))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(rows):
            element = random.randint(0, 9)
            row.append(element)
        matrix.append(row)
    return matrix


def random_generate_matrix_values_and_size():
    rows = random.randint(1, 9)
    columns = random.randint(1, 9)
    matrix = []
    for i in range(rows):
        row = []
        for j in range(rows):
            element = random.randint(0, 9)
            row.append(element)
        matrix.append(row)
    return matrix

def degree_matrix_by_number(matrix_1):
    try:
        number = input('Ведите степень на какой будете умножать матрицу : ')
        number = int(number)
        result = []
        for i in range(len(matrix_1)):
            rows = []
            for j in range(len(matrix_1)):
                rows.append(matrix_1[i][j] ** int(number))
            result.append(rows)
        return result
    except (TypeError, ValueError):
         print('Ведите число а не символы')


def create_matrix(text):
    rows = int(input(text + 'Ведите количество строк матрицы: '))
    columns = int(input(text + 'Ведите количество столбцов матрицы : '))
    matrix = []
    print(f"Введите элементы матрицы {rows}x{columns}:")
    for i in range(rows):
        row = []
        for j in range(rows):
            element = int(input(f"Элемент [{i + 1}][{j + 1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix


def add_matrix(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        print("Матрицы должны иметь одинаковые размеры для сложения.")
    else:
        result = []
        for i in range(len(matrix_1)):
            row = []
            for j in range(len(matrix_1)):
                row.append(matrix_1[i][j] + matrix_2[i][j])
            result.append(row)
        return result


def subtract_matrix(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        print("Матрицы должны иметь одинаковые размеры для сложения.")
    else:
        result = []
        for i in range(len(matrix_1)):
            row = []
            for j in range(len(matrix_1)):
                row.append(matrix_1[i][j] - matrix_2[i][j])
            result.append(row)
        return result


def multiplication_matrix(matrix_1, matrix_2):
    if len(matrix_1[0]) != len(matrix_2[0]):
        print("Число столбцов первой матрицы должно быть равно числу строк второй матрицы для умножения.")
    else:
        result = []
        for i in range(len(matrix_1)):
            row = []
            for j in range(len(matrix_2[0])):
                total = 0
                for k in range(len(matrix_2)):
                    total += matrix_1[i][k] * matrix_2[k][j]
                row.append(total)
            result.append(row)
        return result



while True:
    print('Выберите операцию: ')
    print('"+" - Сложение матриц.')
    print('"*" - Умножение матриц.')
    print('"-" - Отнимания матриц.')
    print('"T" - Транспонирование матриц.')
    print('"N" - Умножение матрицы на число.')
    print('"^" - Умножение матрицы на число.')
    print('"R" - Сгенерировать матрицу определеного размера заполненой рандомнами цифрами.')
    print('"Н" - Сгенерировать матрицу рандомного размера заполненой рандомнами цифрами.')

    choice = input('Ведите операцию: ')

    if choice in ['+', '-', '*']:
        matrix_1 = create_matrix("Введите первую матрицу: ")
        matrix_2 = create_matrix("Введите вторую матрицу: ")

        if choice == '+':
            result = add_matrix(matrix_1, matrix_2)
        elif choice == '-':
            result = subtract_matrix(matrix_1, matrix_2)
        elif choice == '*':
            result = multiplication_matrix(matrix_1, matrix_2)

        input_matrix(result)
    elif choice == 'T':
        matrix_1 = create_matrix("Введите матрицу: ")
        result = transport_matrix(matrix_1)
        input_matrix(result)
    elif choice in {'N', '^'}:
        matrix_1 = create_matrix("Введите матрицу: ")

        if choice == 'N':
            result = multiplication_matrix_by_number(matrix_1)
        elif choice == '^':
            result = degree_matrix_by_number(matrix_1)

    elif choice in {'R', 'H'}:
        if choice == 'R':
            result = random_generate_matrix_values()
        elif choice == 'H':
            result = random_generate_matrix_values_and_size()

        input_matrix(result)
    else:
        print('Вы ввели неправильную операцию. Попробуйте еще раз.')
