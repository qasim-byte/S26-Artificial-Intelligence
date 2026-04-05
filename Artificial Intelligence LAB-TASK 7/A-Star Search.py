from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        
        open_list = set([start_node])
        closed_list = set([])

        g = {}
        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while open_list:
            
            n = min(open_list, key=lambda v: g[v] + self.h(v))

            
            if n == stop_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start_node)
                path.reverse()
                print('Path found: {}'.format(path))
                return path

            
            for (m, weight) in self.get_neighbors(n):
                tentative_g = g[n] + weight

                if m not in open_list and m not in closed_list:
                    
                    open_list.add(m)
                    parents[m] = n
                    g[m] = tentative_g

                elif tentative_g < g.get(m, float('inf')):
                    
                    g[m] = tentative_g
                    parents[m] = n

                    
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

            
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'D')