from collections import deque

# Undirected graph using an adjacency list


class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


# Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


# Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


# Breadth First Search
def BFS2(G, node1, node2):
    Q = deque([[node1]])
    marked = {node1: True}

    for node in G.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        path = Q.popleft()
        current_node = path[-1]

        if current_node == node2:
            return path

        for node in G.adj[current_node]:
            if not marked[node]:
                next_path = list(path)
                next_path.append(node)
                Q.append(next_path)
            else:
                marked[node] = True

    return False


def DFS2(G, node1, node2):
    S = [(node1, [node1])]
    marked = {}

    for node in G.adj:
        marked[node] = False

    while len(S) != 0:
        current_node, current_path = S.pop()
        if not marked[current_node]:
            if current_node == node2:
                return current_path
            marked[current_node] = True

            for node in G.adj[current_node]:
                S.append((node, current_path + [node]))
    return False


def BFS3(G, node1):
    pred = {}
    Q = deque([node1])
    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                if node not in pred:
                    pred[node] = current_node
    return pred


def DFS3(G, node1):
    pred = {}
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node not in pred and node != 0:
                    pred[node] = current_node
                S.append(node)
    return pred


def has_cycle(g):
    seen = [False for _ in range(len(g.adj))]

    def has_cycle_rec(g, v, inner_seen, predessor):
        inner_seen[v] = True

        for i in g.adjacent_nodes(v):
            if not inner_seen[i]:
                if (has_cycle_rec(g, i, inner_seen, v)):
                    return True
            elif predessor != i:
                return True

        return False

    for j in range(len(g.adj)):
        if not seen[j]:
            if (has_cycle_rec(g, j, seen, -1)):
                return True
    return False


def is_connected(g):
    for i in g.adj:
        if len(g.adj[i]) == 0:
            return False
    return True