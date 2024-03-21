def build_automaton(pattern):
    """
    Функция для построения автомата на основе образца.
    :param pattern: образец для поиска
    :return: автомат в виде двумерного списка
    """
    m = len(pattern)
    automaton = [[0] * 256 for _ in range(m + 1)]  # Создание двумерного списка для автомата
    automaton[0][ord(pattern[0])] = 1  # Инициализация первого состояния автомата

    x = 0  # Переменная для хранения текущего состояния суффиксной ссылки
    for j in range(1, m):  # Итерация по символам образца (кроме первого)
        for c in range(256):  # Итерация по всем возможным символам (ASCII)
            automaton[j][c] = automaton[x][c]  # Копирование переходов из состояния суффиксной ссылки
        automaton[j][ord(pattern[j])] = j + 1  # Установка перехода для текущего символа образца
        x = automaton[x][ord(pattern[j])]  # Обновление состояния суффиксной ссылки

    for c in range(256):  # Итерация по всем возможным символам (ASCII)
        automaton[m][c] = automaton[x][c]  # Копирование переходов из состояния суффиксной ссылки для последнего состояния

    return automaton  # Возвращение построенного автомата

def search_pattern(text, pattern):
    """
    Функция для поиска образца в тексте с использованием автомата.
    :param text: исходный текст
    :param pattern: образец для поиска
    """
    m = len(pattern)  # Длина образца
    n = len(text)  # Длина текста
    automaton = build_automaton(pattern)  # Построение автомата на основе образца

    state = 0  # Начальное состояние автомата
    for i in range(n):  # Итерация по символам текста
        state = automaton[state][ord(text[i])]  # Обновление состояния автомата на основе текущего символа
        if state == m:  # Если достигнуто конечное состояние автомата
            print(f"Образец найден по индексу {i - m + 1}")  # Вывод сообщения о найденном вхождении образца

# Чтение исходной строки из файла
with open("input.txt", "r") as file:
    text = file.read()

# Ввод строки поиска с клавиатуры
pattern = input("Введите строку поиска: ")
print(build_automaton('b'))
# Поиск образца в исходной строке
search_pattern(text, pattern)