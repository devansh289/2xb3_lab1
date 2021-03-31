import min_heap
from lab9 import *


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
