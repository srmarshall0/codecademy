# define Vertex class
class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight = 0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())

    def get_weight(self, edge):
        return self.edges[edge]

# define graph class
class Graph:

    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):

        start = [start_vertex]
        seen = {}

        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print("Visiting " + current_vertex)

            if current_vertex == end_vertex:
                return True

            else:
                vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]

            return False

# build a traveling salseperson graph -- requires a connected graph with symmetrical weights
def build_tsp_graph(directed):
    tsp_graph = Graph(directed)
    vertices = []

    for val in ['a', 'b', 'c', 'd']:
        vertex = Vertex(val)
        vertices.append(vertex)
        tsp_graph.add_vertex(vertex)

    tsp_graph.add_edge(vertices[0], vertices[1], 3)
    tsp_graph.add_edge(vertices[0], vertices[2], 4)
    tsp_graph.add_edge(vertices[0], vertices[3], 5)
    tsp_graph.add_edge(vertices[1], vertices[0], 3)
    tsp_graph.add_edge(vertices[1], vertices[2], 2)
    tsp_graph.add_edge(vertices[1], vertices[3], 6)
    tsp_graph.add_edge(vertices[2], vertices[0], 4)
    tsp_graph.add_edge(vertices[2], vertices[1], 2)
    tsp_graph.add_edge(vertices[2], vertices[3], 1)
    tsp_graph.add_edge(vertices[3], vertices[0], 5)
    tsp_graph.add_edge(vertices[3], vertices[1], 6)
    tsp_graph.add_edge(vertices[3], vertices[2], 1)

    return tsp_graph



