from adventcode.utils import read_file

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

    temp = [v for v in nodes]
    while len(temp) > 0:
        upper = {v: path_lengths[v] for v in temp}
        u = min(upper, key=upper.get)
        temp.remove(u)

        for v, w_uv in adjacent[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + w_uv)
    return path_lengths


def surround(i, j):
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
# print(nodes)
# print(edges)
