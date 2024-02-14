# Находит множество вершины i
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

# Объединяет вершины i и j. Возвращает False, если i и j уже находятся в одном множестве.
def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b

# Находит минимальное остовное дерево с помощью алгоритма Краскала
def kruskalMST(cost):
    mincost = 0  # Стоимость минимального остовного дерева

    # Инициализация наборов непересекающихся множеств
    for i in range(V):
        parent[i] = i

    # Включаем минимальные ребра по одному
    edge_count = 0
    with open('output.txt', 'w') as f:
        while edge_count < V - 1:
            min = float('inf')
            a = -1
            b = -1
            for i in range(V):
                for j in range(V):
                    if find(i) != find(j) and cost[i][j] != 0 and cost[i][j] < min:
                        min = cost[i][j]
                        a = i
                        b = j
            union(a, b)
            f.write(f'{a} - {b}    cost: {cost[a][b]}\n')
            edge_count += 1
            mincost += min

        f.write(f"Minimum cost = {mincost}\n")

# Чтение графа из файла
with open('input.txt', 'r') as file:
    V = int(file.readline().strip())
    cost = [[int(x) for x in line.split()] for line in file]

parent = [i for i in range(V)]
kruskalMST(cost)
