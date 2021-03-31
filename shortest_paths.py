from lab9 import *

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
