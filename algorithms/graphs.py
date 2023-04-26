# build a vertex class
class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edges(self, vertex, weight = 0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())

# build graph class
class Graph:
    def __init__(self, directed = False):
        self.directed = directed 
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        # if the list is bi-directional, draw an edge to -> from as well 
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = start[vertex]
        seen = {}
        while start:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
        
        if current_vertex == end_vertex:
            return True
        vertex = self.graph_dict[current_vertex]
        next_vertices = vertex.get_edges()
        next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
        start.extend(next_vertices)

        return False

# build a depth first graph search algorithm
def graph_dfs(graph, current_vertex, target_value, visited = None):

    if visited is None:
        visited = []

    visited.append(current_vertex)

    if current_vertex is target_value:
        return visited
    
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = graph_dfs(graph, neighbor, target_value, visited = None)
            if path:
                return path 

# build a breadth first search algorithm
def graph_bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()

    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if neighbor is target_value:
                    return path + [neighbor]
                else:
                    bfs_queue.append([neighbor, path + [neighbor]])

