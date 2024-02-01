#include <iostream>
#include <fstream>
#include <queue>
#include <vector>

const int maximum_N = 100; // максимальное количество вершин в графе

int n; // количество вершин в графе
int a[maximum_N][maximum_N]; // матрица смежности
bool used[maximum_N]; // массив для отслеживания пройденных вершин
std::vector<int> components[maximum_N]; // массив для хранения вершин в компонентах связности

void bfs(int v, int comp) // поиск в ширину
{
    std::queue<int> q;
    q.push(v);
    used[v] = true; // отмечаем вершину как посещенную
    components[comp].push_back(v); // добавляем вершину в текущую компоненту связности
    while (!q.empty()) 
    {
        int u = q.front();
        q.pop();
        for (int i = 0; i < n; i++) 
        {
            if (a[u][i] == 1 && !used[i]) // если вершина смежная и не посещена
            {
                used[i] = true; // отмечаем её как посещенную
                components[comp].push_back(i); // добавляем её в текущую компоненту связности
                q.push(i); // добавляем вершину в очередь для обхода её соседей
            }
        }
    }
}

int main() 
{
    std::ifstream fin("input.txt");
    fin >> n; // считывание количества вершин
    for (int i = 0; i < n; i++) 
    {
        for (int j = 0; j < n; j++) 
        {
            fin >> a[i][j]; // считывание матрицы смежности
        }
    }
    fin.close();

    int comp = 0; // количество компонент связности
    for (int i = 0; i < n; i++) 
    {
        if (!used[i]) 
        {
            bfs(i, comp); // запуск поиска в ширину из не пройденной вершины
            comp++; // увеличение количества компонент связности
        }
    }
    std::ofstream fout("output.txt");
    fout << "Количество компонент связности: " << comp << std::endl;
    for (int i = 0; i < comp; i++) 
    {
        fout << "Компонента связности " << i + 1 << ": ";
        for (int vertex : components[i]) 
        {
            fout << vertex << " "; // записываем вершины в компоненте связности
        }
        fout << std::endl;
    }
    fout.close();
}
