# Функция для определения направления поворота p, q и r.
# pq = (q[0] - p[0], q[1] - p[1])
# qr = (r[0] - q[0], r[1] - q[1]).
# Вычисляем векторное произведение val по формуле:
# val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]).
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Коллинеарны
    elif val > 0:
        return 1  # По часовой стрелке
    else:
        return 2  # Против часовой стрелки

# Реализация алгоритма Джарвиса для нахождения выпуклой оболочки множества точек.
def jarvis_convex_hull(points):
    n = len(points)
    if n < 3:  # Если точек меньше 3, выпуклая оболочка не может быть построена
        return None

    hull = []  # Список для хранения точек выпуклой оболочки
    l = 0  # Инициализация индекса самой левой нижней точки
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i  # Находим самую левую нижнюю точку
    p = l  # Начальная точка для построения оболочки
    while True:
        hull.append(points[p])  # Добавляем текущую точку в оболочку
        q = (p + 1) % n  # Начинаем сравнивать с следующей точкой
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i  # Находим следующую точку с максимальным углом
        p = q  # Переходим к следующей точке
        if p == l:
            break  # Когда мы вернулись к начальной точке, завершаем алгоритм

    return hull  # Возвращаем список точек выпуклой оболочки


# Пример использования
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
convex_hull = jarvis_convex_hull(points)
print("Выпуклая оболочка:")
for point in convex_hull:
    print(point)
