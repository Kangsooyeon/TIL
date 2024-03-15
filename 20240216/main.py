def traveling_salesman_backtracking(distances):
    num_cities = len(distances)

    start_city = 0
    min_distance = float('inf')

    stack = [(start_city, {start_city}, [start_city], 0)]

    while stack:
        current_city, visited, path, current_distance = stack.pop()

        if len(path) == num_cities:
            distance_to_start = distances[current_city][start_city]
            total_distance = current_distance + distance_to_start

            if total_distance < min_distance:
                min_distance = total_distance

        for next_city in range(num_cities):
            if next_city not in visited:
                new_distance = current_distance + distances[current_city][next_city]

                if new_distance < min_distance:
                    stack.append((next_city, visited | {next_city}, path + [next_city], new_distance))

    return min_distance


# 예제: 4개의 도시에 대한 거리 행렬
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# 백트래킹을 사용하여 최단 경로 찾기
shortest_distance = traveling_salesman_backtracking(distances)

# 결과 출력
print("최단 거리:", shortest_distance)
