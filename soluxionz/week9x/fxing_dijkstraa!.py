# O(V+E) time/O(V) space: include keys and neighbours, even neighbour-only leaf nodes.
def graph_nodes(graph):
    nodes = {}
    for node in graph:
        nodes[node] = True
        for neighbour in graph[node]:
            nodes[neighbour] = True
    return nodes


# O(V+E) time/O(V) space: BFS discovers each node once and stores its parent.
def shortest_path(graph, start, goal):
    nodes = graph_nodes(graph)
    if start not in nodes or goal not in nodes:
        return []
    queue = [start]
    head = 0
    parents = {start: start}
    while head < len(queue):
        node = queue[head]  # pop(0) would shift every remaining item, O(queue length) 😭
        head += 1
        if node == goal:
            path = [goal]
            while node != start:
                node = parents[node]
                path.append(node)
            path.reverse()
            return path
        for neighbour in graph.get(node, []):
            if neighbour not in parents:
                parents[neighbour] = node
                queue.append(neighbour)
    return []


# O(V+E) time/O(V) space: preserve the starter name; these unweighted edges need BFS.
def dijkstra(graph, start, end) -> list:
    return shortest_path(graph, start, end)


# O(V+E) time/O(V) space: queue and visited dictionary avoid counting nodes twice.
def reachable(graph, start):
    if start not in graph_nodes(graph):
        return 0
    queue = [start]
    head = 0
    visited = {start: True}
    while head < len(queue):
        node = queue[head]
        head += 1
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited[neighbour] = True
                queue.append(neighbour)
    return len(visited)


# O(V+E) time/O(V) space: an iterative DFS detects edges back into its active stack.
def has_cycle(graph):
    states = {}
    for start in graph_nodes(graph):
        if states.get(start, 0) != 0:
            continue
        states[start] = 1
        stack = [(start, 0)]
        while stack:
            node, index = stack[-1]
            neighbours = graph.get(node, [])
            if index == len(neighbours):
                states[node] = 2
                stack.pop()
                continue
            neighbour = neighbours[index]
            stack[-1] = (node, index + 1)
            if states.get(neighbour, 0) == 1:
                return True
            if states.get(neighbour, 0) == 0:
                states[neighbour] = 1
                stack.append((neighbour, 0))
    return False


# O(V+E+P*L) time/space: BFS stores shortest parents, then materializes P paths of length L.
def all_shortest_paths(graph, start, goal):
    nodes = graph_nodes(graph)
    if start not in nodes or goal not in nodes:
        return []
    queue = [start]
    head = 0
    distance = {start: 0}
    parents = {start: []}
    while head < len(queue):
        node = queue[head]
        head += 1
        seen_neighbours = {}
        for neighbour in graph.get(node, []):
            if neighbour in seen_neighbours:
                continue
            seen_neighbours[neighbour] = True
            steps = distance[node] + 1
            if neighbour not in distance:
                distance[neighbour] = steps
                parents[neighbour] = [node]
                queue.append(neighbour)
            elif distance[neighbour] == steps:
                parents[neighbour].append(node)
    if goal not in distance:
        return []
    result = []
    current = [goal]

    # O(P*L) total time/output space: copy each complete path; stack depth is at most L.
    def collect(node):
        if node == start:
            path = current.copy()
            path.reverse()
            result.append(path)
            return
        for previous in parents[node]:
            current.append(previous)
            collect(previous)
            current.pop()

    collect(goal)
    return result


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"],
             "D": ["F"], "E": ["F"], "F": []}
    for start, goal in (("A", "F"), ("A", "A"), ("F", "A"), ("missing", "F")):
        print(start, "→", goal, shortest_path(graph, start, goal))
    print("Reachable from A:", reachable(graph, "A"))
    print("Reachable from C:", reachable(graph, "C"))
    print("All shortest A to F:", all_shortest_paths(graph, "A", "F"))
    for network in (graph, {"X": ["Y"], "Y": ["X"]}, {}, {"A": ["A"]},
                    {"A": ["B", "B"]}, {"alone": []}):
        print("Cycle:", network, "→", has_cycle(network))
