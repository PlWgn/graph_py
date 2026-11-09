from collections import deque

class DirectedGraph:
    def __init__(self):
        self.__graph = dict()
    
    def add_vertex(self, vertex:str):
        if vertex in self.__graph:
            return
        self.__graph[vertex] = set()
    
    def add_edge(self, vertex_from:str, vertex_to:list):
        if len(self.__graph) <= 1:
            return
        if vertex_from in self.__graph:
            value = self.__graph[vertex_from]
            for i in vertex_to:
                if i in self.__graph:
                    value.add(i)
        
    def BFS(self, start: str):
        if start not in self.__graph:
            return

        queue = deque([start])
        visited = {start}

        while queue:
            current = queue.popleft()
            print(current, end=' ')

            for neighbor in sorted(self.__graph[current]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    @property
    def MOF(self):
        matrix = []

        for i in self.__graph:
            row = []
            for j in self.__graph:
                row.append(1 if j in self.__graph[i] else 0)
            matrix.append(row)

        return matrix
    
    @property
    def LOG(self):
        res = {}

        for key in self.__graph:
            res[key] = sorted(self.__graph[key])

        return res
        
dg = DirectedGraph()
dg.add_vertex('A')
dg.add_vertex('B')
dg.add_vertex('A')
dg.add_vertex('D')

dg.add_edge('A', ['B', 'D', 'C'])
dg.add_edge('B', ['D'])
dg.add_edge('D', ['A'])
dg.add_edge('H', ['F'])

dg.BFS('A')
print('')
print(*dg.MOF, sep='\n')
print(dg.LOG)