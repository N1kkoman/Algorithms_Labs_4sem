def read_graph(file_name):
    with open(file_name, 'r') as file:
        num_vertices = int(file.readline().strip())
        graph = []
        for _ in range(num_vertices):
            row = list(map(int, file.readline().strip().split()))
            graph.append(row)
    return graph

def find_eulerian_cycle(graph):
    num_vertices = len(graph)
    degree = [sum(row) for row in graph]
    for d in degree:
        if d % 2 != 0:
            return None  # Граф не содержит эйлеров цикл
    stack = [0]
    cycle = []
    while stack:
        v = stack[-1]
        if any(graph[v]):
            u = next(i for i, x in enumerate(graph[v]) if x)
            stack.append(u)
            graph[v][u] -= 1
            graph[u][v] -= 1
        else:
            cycle.append(stack.pop())
    return cycle[::-1]

file_name = 'input.txt'

graph = read_graph(file_name)
eulerian_cycle = find_eulerian_cycle(graph)

output_file = 'output.txt'
with open(output_file, 'w') as file:
    if eulerian_cycle:
        file.write('Eulerian cycle found:\n')
        file.write(' -> '.join(map(str, eulerian_cycle)))
    else:
        file.write('Graph does not have an Eulerian cycle.')