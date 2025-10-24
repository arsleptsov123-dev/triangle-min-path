
def min_triangle_path(triangle):

    if not triangle or not triangle[0]:
        return 0, []

    n = len(triangle)
    # Создаем копию треугольника для DP
    dp = [row[:] for row in triangle]

    # Начинаем с предпоследней строки и двигаемся вверх
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Выбираем минимальный путь из двух возможных
            dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])

    # Теперь dp[0][0] содержит минимальную сумму
    min_sum = dp[0][0]

    # Восстанавливаем путь
    path = [triangle[0][0]]
    current_j = 0
    for i in range(1, n):
        # Выбираем направление: вниз или вниз-вправо
        if dp[i][current_j] <= dp[i][current_j + 1]:
            next_val = triangle[i][current_j]
        else:
            next_val = triangle[i][current_j + 1]
            current_j += 1
        path.append(next_val)

    return min_sum, path


def print_solution(triangle):
    """Печатает результат в требуемом формате"""
    min_sum, path = min_triangle_path(triangle)
    path_str = " → ".join(map(str, path))
    print(f"Минимальный путь: {path_str}")
    print(f"Результат: {min_sum}")


# Пример использования
if __name__ == "__main__":
    # Тест 1
    triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print("Треугольник 1:")
    print_solution(triangle1)
    print()

    # Тест 2
    triangle2 = [[-1], [2, 3], [1, -1, -3], [4, 2, 1, 3]]
    print("Треугольник 2:")
    print_solution(triangle2)