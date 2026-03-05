# ── Node Class ────────────────────────────────────────────
class Node:
    def __init__(self, value):
        self.value    = value   # data stored in the node
        self.children = []      # list of child Node objects

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f'Node({self.value})'


# ── Queue Class ───────────────────────────────────────────
class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):     # add to the back
        self._data.append(item)

    def dequeue(self):           # remove from the front (FIFO)
        if self.is_empty():
            raise IndexError('Dequeue from empty queue')
        return self._data.pop(0)

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


# ── BFS Function ──────────────────────────────────────────
def bfs(start_node, goal_value):
    queue    = Queue()
    visited  = set()
    path_map = {start_node: None}

    queue.enqueue(start_node)
    visited.add(start_node.value)

    while not queue.is_empty():
        current = queue.dequeue()
        print('Visiting:', current.value)

        if current.value == goal_value:
            path = []
            node = current
            while node is not None:
                path.append(node.value)
                node = path_map[node]
            path.reverse()
            print('\nGoal Found!')
            print('Path:', ' -> '.join(path))
            return True

        for child in current.children:
            if child.value not in visited:
                visited.add(child.value)
                path_map[child] = current
                queue.enqueue(child)

    print('Goal not found.')
    return False


# ── Build the Tree ────────────────────────────────────────
#       A
#      / \
#     B   C
#    / \   \
#   D   E   F
#       |
#       G   <-- goal

A = Node('A')
B = Node('B'); C = Node('C')
D = Node('D'); E = Node('E'); F = Node('F')
G = Node('G')

A.add_child(B); A.add_child(C)
B.add_child(D); B.add_child(E)
C.add_child(F)
E.add_child(G)

bfs(A, 'G')
