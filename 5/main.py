# Функция для чтения матрицы смежности из файла
def read_adjacency_matrix(filename):
    with open(filename, 'r') as file:
        size = int(file.readline().strip())  # Читаем размер матрицы смежности из первой строки
        # Считываем саму матрицу смежности как список списков
        matrix = [[int(num) for num in line.split()] for line in file]
    return matrix

# Функция для записи результата в файл
def write_result(filename, result):
    with open(filename, 'w') as file:
        file.write(result)

# Обход в глубину (DFS) для графа
def dfs(graph, node, visited, stack):
    visited[node] = True  # Помечаем узел как посещенный
    for i, is_edge in enumerate(graph[node]):
        if is_edge and not visited[i]:  # Для каждой смежной вершины
            dfs(graph, i, visited, stack)  # Рекурсивно вызываем DFS
    stack.append(node)  # Добавляем узел в стек после посещения всех смежных вершин

# Функция для транспонирования графа
def transpose_graph(graph):
    # Транспонирование матрицы смежности
    return [list(row) for row in zip(*graph)]

# Алгоритм Косарайю для нахождения сильно связных компонент
def kosaraju(graph):
    visited = [False] * len(graph)  # Инициализируем список посещенных вершин
    stack = []  # Стек для хранения порядка завершения вершин
    
    # 1-й проход DFS для заполнения стека
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, stack)
    
    # Транспонируем граф
    transposed_graph = transpose_graph(graph)
    visited = [False] * len(graph)  # Сбрасываем список посещенных вершин
    components = []  # Список для хранения сильно связных компонент
    
    # 2-й проход DFS на транспонированном графе
    while stack:
        node = stack.pop()  # Берем вершину из стека
        if not visited[node]:
            component = []
            dfs(transposed_graph, node, visited, component)  # Выполняем DFS для вершины
            components.append(component)  # Добавляем сильно связную компоненту в список
    
    return components


input_filename = 'input.txt'
output_filename = 'output.txt'

adjacency_matrix = read_adjacency_matrix(input_filename)
components = kosaraju(adjacency_matrix)

# Формирование результата для записи в файл
result = f"Количество сильно связных компонент: {len(components)}\nСостав компонент:\n"
for i, component in enumerate(components):
    result += f"Компонент {i+1}: {component}\n"

write_result(output_filename, result)