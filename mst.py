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

    # Uncomment to check graph
    # print(ans.adj)
    return ans


def prim2(graph):
    # Graph to output as answer
    ans = WeightedGraph(graph.number_of_nodes())
    visited = set()

    # Number of nodes visited
    vertices_visited = 0

    # Heap for current edges we can choose from
    adjacent_edges = [Element(i, 1001)
                      for i in range(graph.number_of_nodes())]
    adjacent_edges = MinHeap(adjacent_edges)

    # Node we are on
    current_node = adjacent_edges.extract_min().value

    # Mark node as visited
    visited.add(current_node)

    # While not all nodes are visited
    while vertices_visited < graph.number_of_nodes():
        # Update heap with correct weights
        for edge in graph.adjacent_nodes(current_node):
            adjacent_edges.decrease_key(edge[0], edge[1])

        chosen_edge = None

        while not adjacent_edges.is_empty():
            # Set current edge to min
            chosen_edge = adjacent_edges.extract_min()

            # Information about chosen edge
            node1 = chosen_edge.value
            node2 = None
            weight = chosen_edge.key

            # Get node2 (other node that the edge connects)
            for node in visited:
                if graph.are_connected(node, node1):
                    if graph.w(node, chosen_edge.value) == weight:
                        node2 = node
                        break

            # Set new_node to the node that has not been visited yet
            new_node = None
            if node1 in visited:
                new_node = node2
            else:
                new_node = node1

            # If there is a valid node2, else fetch least value again
            if node2 != None:

                # Make sure both nodes weren't visited to avoid loops
                if not (node1 in visited and node2 in visited):
                    ans.add_edge(node1, node2, weight)
                    visited.add(node1)
                    visited.add(node2)

                    # List to append new edges to
                    L = []
                    for edge in graph.adjacent_nodes(new_node):
                        L.append(Element(edge[0], edge[1]))

                    # Add new possible edges
                    adjacent_edges.insert_elements(L)
                    current_node = new_node
                    break
        vertices_visited += 1

    # Uncomment to check graph
    # print(ans.adj)
    return ans
