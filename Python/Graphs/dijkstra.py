
import sys

def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in graph}
    D[start_vertex] = 0

    unvisited = list(graph)

    while len(unvisited) > 0:
        current_vertex = unvisited[0]
        for vertex in unvisited:
            if D[vertex] < D[current_vertex]:
                current_vertex = vertex

        for neighbour, cost in graph[current_vertex].items():
            if D[current_vertex] + cost < D[neighbour]:
                D[neighbour] = D[current_vertex] + cost

        unvisited.remove(current_vertex)

    return D

# Testing
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 1},
    'D': {'B': 1, 'C': 1}
}

print(dijkstra(graph, 'A'))  # {'A': 0, 'B': 1, 'C': 2, 'D': 2}
