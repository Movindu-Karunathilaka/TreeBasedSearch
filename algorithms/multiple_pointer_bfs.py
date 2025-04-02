from collections import deque

def multiple_pointer_bfs(graph, start, goals):
    number_of_nodes = 0
    startDeque = deque([(start, [start])])
    visited = set()
    # Create a stack for every goal to expand
    goalsDeque = deque()
    goalsVisited = set()
    for goal in goals:
        goalsDeque.append([(goal, [goal])])
    while startDeque:
        # Expand start
        node, path = startDeque.popleft()
        if node in visited:
            continue
        visited.add(node)
        number_of_nodes += 1

        # Check if it's in goal (need to implement hashmap not brute force later)
        for goal in goalsDeque:
            if node == goal[0]:
                return node, number_of_nodes, path + goal[1][::-1]
        # Use _ because we are not considering weight
        for currNode, _ in graph[node]:
            if currNode not in visited:
                startDeque.append(currNode, path + [])


        # Expand all goals
        for goalDeque in goalsArr:
