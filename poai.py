from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = set()
    result = []

    while queue:
        current_node = queue.popleft()
        result.append(current_node)

        for n in graph[current_node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

        return result
