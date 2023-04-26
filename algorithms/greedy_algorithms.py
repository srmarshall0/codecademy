# import packages and methods
from heapq import heappop, heappush
from math import inf

# write dijkstras algorithm
def dijkstras(graph, start):

    # define dictionary to be filled
    distances = {}

    # assign a start vertex of 0 and add to the vertices to explore
    distances[start] = 0
    vertices_to_explore = [(0, start)]

    # set each vertex in graph to have a distance on inf
    for vertex in graph:
        distances[vertex] = inf

    # while there are still vertices to explore search for shortest route
    while vertices_to_explore:

        current_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    # return dictionary
    return distances

# write A* algorithm

# write a heuristic helper function for estimating disatnce 
def heuristic(start, target):

    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])

    return x_distance + y_distance

# write actual algorithm
def a_star(graph, start, target):

    # initiate objects
    print("Starting A* algorithm!")
    count = 0
    paths_and_distances = {}

    # build out dictionary
    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]

    # set start vertex to 0
    paths_and_distances[start][0] = 0

    # add starting vertex to list to explore
    vertices_to_explore = [(0, start)]

    # loop while we are still exploring vertecies AND paths and target distances has not been defined
    while vertices_to_explore and paths_and_distances[target][0] == inf:

        # set current_distance and current_vertex to the minimum value in the list to explore
        current_distance, current_vertex = heappop(vertices_to_explore)

        # loop over the neighbor + edge weight combinations available at the current_vertex in graph 
        for neighbor, edge_weight in graph[current_vertex]:
            # define new distance, taking into account the heuristic calculation
            new_distance = current_distance + edge_weight + heuristic(neighbor, target)
            # set new path equal to the current_vertex's edge weight and vertex name
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]

            # check if the new distance is LESS THAN the distance produced by the neighboring vertex
            if new_distance < paths_and_distances[neighbor][0]:
                # add new distance to the dictionary
                paths_and_distances[neighbor][0] = new_distance
                # add new path to dictionary
                paths_and_distances[neighbor][1] = new_path
                # push new_distance and neighbor onto the vertices_to_explore heap
                heappush(vertices_to_explore, (new_distance, neighbor))
                # increment count
                count += 1

    return paths_and_distances[target][1]





    

