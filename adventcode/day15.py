from adventcode.utils import read_file
import numpy as np
import heapq

file_path = './input/day15.txt'


def parse_file(file_content=read_file(file_path)):
    rows = file_content.split('\n')
    rows = [list(row) for row in rows]
    return rows


sample = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

cave = parse_file()


def dijkstra(nodes, edges, source=(0, 0)):
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source] = 0

    adjacent = {v: {} for v in nodes}
    for (u, v), w_uv in edges.items():
        adjacent[u][v] = w_uv

    # temp = [v for v in nodes]
    pq = [(0, source)]

    while len(pq) > 0:
        curr_d, curr_v = heapq.heappop(pq)

        if curr_d > path_lengths[curr_v]:
            continue

        for n, w in adjacent[curr_v].items():
            distance = curr_d + w
            if distance < path_lengths[n]:
                path_lengths[n] = distance
                heapq.heappush(pq, (distance, n))
    return path_lengths


def surround(i, j, cave=cave):
    def within(a, z):
        return a in range(z)

    edges = [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]
    edges = [edge for edge in edges if within(
        edge[1], y) and within(edge[0], x)]
    edge_values = {((i, j), edge): int(
        cave[edge[1]][edge[0]]) for edge in edges}
    return edge_values


x, y = len(cave[0]), len(cave)
nodes = []
edges = {}
for i in range(x):
    for j in range(y):
        nodes.append((i, j))
        edges.update(surround(i, j))

print(dijkstra(nodes, edges).get((x-1, y-1)))

# part 2


def increment(ele, i):
    return (ele+i) % 9 if ((ele+i) % 9) != 0 else 9


def expand(arr):
    arr = np.array([[int(ele) for ele in row] for row in arr])
    arr = np.concatenate((arr, np.vectorize(increment)(arr, 1),
                          np.vectorize(increment)(arr, 2),
                          np.vectorize(increment)(arr, 3),
                          np.vectorize(increment)(arr, 4)), axis=1)
    arr = np.concatenate((arr, np.vectorize(increment)(arr, 1),
                          np.vectorize(increment)(arr, 2),
                          np.vectorize(increment)(arr, 3),
                          np.vectorize(increment)(arr, 4)))
    return arr.tolist()


cave2 = expand(parse_file())
x, y = len(cave2[0]), len(cave2)
nodes = []
edges = {}
for i in range(x):
    for j in range(y):
        nodes.append((i, j))
        edges.update(surround(i, j, cave=cave2))

print(dijkstra(nodes, edges).get((x-1, y-1)))
