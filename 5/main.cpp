#include <iostream>
#include <vector>
#include <stack>
#include <fstream>

using namespace std;

void DFS1(int v, vector<vector<int>>& graph, vector<bool>& visited, stack<int>& finishStack) {
    visited[v] = true;
    for (int i = 0; i < graph[v].size(); i++) {
        if (!visited[i] && graph[v][i] > 0) {
            DFS1(i, graph, visited, finishStack);
        }
    }
    finishStack.push(v);
}

void DFS2(int v, vector<vector<int>>& transposeGraph, vector<bool>& visited, vector<int>& component) {
    visited[v] = true;
    component.push_back(v);
    for (int i = 0; i < transposeGraph[v].size(); i++) {
        if (!visited[i] && transposeGraph[v][i] > 0) {
            DFS2(i, transposeGraph, visited, component);
        }
    }
}

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n;
    fin >> n; // Чтение количества вершин графа

    vector<vector<int>> graph(n, vector<int>(n));
    vector<vector<int>> transposeGraph(n, vector<int>(n));
    vector<bool> visited(n, false);
    stack<int> finishStack;
    vector<vector<int>> components;

    // Чтение матрицы смежности из файла
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            fin >> graph[i][j];
            transposeGraph[j][i] = graph[i][j]; // Транспонирование графа
        }
    }
    fin.close();

    // 1-й проход DFS для определения порядка завершения вершин
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            DFS1(i, graph, visited, finishStack);
        }
    }

    // Очистка флагов посещения для второго прохода
    fill(visited.begin(), visited.end(), false);

    // 2-й проход DFS на транспонированном графе
    while (!finishStack.empty()) {
        int v = finishStack.top();
        finishStack.pop();
        if (!visited[v]) {
            vector<int> component;
            DFS2(v, transposeGraph, visited, component);
            components.push_back(component);
        }
    }

    // Вывод результатов
    fout << "Количество сильно связных компонент: " << components.size() << endl;
    for (const auto& component : components) {
        for (int v : component) {
            fout << v << " ";
        }
        fout << endl;
    }

    fout.close();
    return 0;
}