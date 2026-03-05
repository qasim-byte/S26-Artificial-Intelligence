# Graph represented as a dictionary (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start_node = 'A'
goal_node  = 'G'

def bfs(graph, start, goal):
    queue   = [start]        # plain list used as a queue
    visited = set()
    visited.add(start)
    path_map = {start: None} # tracks how we reached each node

    while queue:
        current = queue.pop(0)   # dequeue from front
        print('Visiting:', current)

        if current == goal:
            # Reconstruct path
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = path_map[node]
            path.reverse()
            print('\nGoal Found!')
            print('Path:', ' -> '.join(path))
            return True

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                path_map[neighbour] = current
                queue.append(neighbour)

    print('Goal not found.')
    return False

bfs(graph, start_node, goal_node)