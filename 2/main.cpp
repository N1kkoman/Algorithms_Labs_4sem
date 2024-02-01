#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <string>

// Функция для поиска в ширину (BFS), возвращает вектор кратчайших расстояний от стартовой вершины до всех остальных
std::vector<int> BFS(const std::vector<std::vector<int>>& graph, int startVertex) {
    int n = graph.size(); // Количество вершин в графе
    std::vector<int> distances(n, -1); // Вектор для хранения расстояний
    std::queue<int> q; // Очередь для BFS

    distances[startVertex] = 0; // Расстояние до стартовой вершины равно 0
    q.push(startVertex); // Добавляем стартовую вершину в очередь

    // Пока очередь не пуста, продолжаем поиск
    while (!q.empty()) {
        int current = q.front(); // Берем вершину из начала очереди
        q.pop(); // Удаляем её из очереди

        // Обходим всех соседей текущей вершины
        for (int i = 0; i < n; ++i) {
            if (graph[current][i] && distances[i] == -1) { // Если сосед существует и еще не посетили
                distances[i] = distances[current] + 1; // Обновляем расстояние
                q.push(i); // Добавляем вершину в очередь
            }
        }
    }

    return distances; // Возвращаем вектор расстояний
}

int main() {
    std::ifstream infile("input.txt"); // Открываем файл для чтения
    std::ofstream outfile("output.txt"); // Открываем файл для записи
    int n, startVertex;
    infile >> n >> startVertex; // Считываем количество вершин и стартовую вершину

    // Считываем матрицу смежности
    std::vector<std::vector<int>> graph(n, std::vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            infile >> graph[i][j];
        }
    }

    // Выполняем поиск в ширину
    std::vector<int> distances = BFS(graph, startVertex);

    // Записываем результаты в файл
    for (int distance : distances) {
        outfile << distance << " ";
    }

    // Закрываем файлы
    infile.close();
    outfile.close();

    return 0;
}