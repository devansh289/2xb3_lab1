from lab8.py import *


def prim1(graph):
    # Graph to output as answer
    ans = WeightedGraph(graph.number_of_nodes())
    visited = [False] * graph.number_of_nodes()

    # Number of nodes visited
    vertices_visited = 0

    # Current edges we can choose from
    # Items must be [int, set(2 ints)]
    # First argument is weight
    # Second argument is set of nodes the edge connects
    adjacent_edges = []

    # Node we are on
    current_node = 0

    # While not all nodes are visited
    while vertices_visited < graph.number_of_nodes():
        visited[current_node] = True

        # Add current_node's edges to list of edges we can choose from (adjacent_edges)
        for edge in graph.adjacent_nodes(current_node):
            adjacent_edges.append([edge[1], {edge[0], current_node}])

        # Sort edges by weight
        adjacent_edges.sort(key=lambda edge: edge[0])

        chosen_edge = None

        for edge in adjacent_edges:
            chosen_edge = edge
            edges = list(edge[1])

            # Node which is not yet visited
            new_node = edges[0] if visited[edges[1]] else edges[1]

            # If edge does not create loop
            if not (visited[edges[0]] and visited[edges[1]]):
                ans.add_edge(edges[0], edges[1], edge[0])
                current_node = new_node
                break

        vertices_visited += 1
    return ans
