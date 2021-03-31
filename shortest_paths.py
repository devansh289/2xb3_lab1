import min_heap
from lab9.py import *


def bellman_ford_approx(G, source, k):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    times_visited = {}  # Determining how many times a node is visited
    nodes = list(G.adj.keys())

    # Initialize distances
    for node in nodes:
        dist[node] = 99999
        times_visited[node] = 0
    dist[source] = 0

    # Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour) and times_visited[neighbour] <= k:
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
                    times_visited[neighbour] += 1
    return dist


def dijkstra(G, source):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, 99999))
        dist[node] = 99999
    Q.decrease_key(source, 0)

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(
                    neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + \
                    G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


def bellman_ford(G, source):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    nodes = list(G.adj.keys())

    # Initialize distances
    for node in nodes:
        dist[node] = 99999
    dist[source] = 0

    # Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist


def all_pairs_dijkstra(G):
    # Initialize empty list for holding shortest paths
    matrix = []

    # Loop through all nodes in G and use Dijkstra's algorithm
    for i in list(G.adj.keys()):
        shortest_path_dijkstra = dijkstra(G, i)
        # Convert dictionary to list and append
        matrix.append(list(shortest_path_dijkstra.values()))

    return matrix


def all_pairs_bellman_ford(G):
    # Initialize empty list for holding shortest paths
    matrix = []

    # Loop through all nodes in G and use Dijkstra's algorithm
    for i in list(G.adj.keys()):
        shortest_path_bellman = bellman_ford(G, i)
        # Convert dictionary to list and append
        matrix.append(list(shortest_path_bellman.values()))

    return matrix
