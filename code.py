from lab9 import *
from shortest_paths import *
import random
import timeit


# Generate weighted graph for bellman ford tests
def random_weighted_graph_bf():
    graph = DirectedWeightedGraph()
    for i in range(1000):
        graph.add_node(i)

    weights = list(range(-1000, 1000))
    random.shuffle(weights)
    nodes = list(range(0, 1000))

    while len(nodes) > 1:
        node_a = random.sample(nodes, 1)[0]
        nodes.remove(node_a)
        node_b = random.sample(nodes, 1)[0]
        graph.add_edge(node_a, node_b, weights.pop(0))

    return graph


# Test for calculating sum of distances
def performance_test_bf_distance():
    f1 = open("bf_values.txt", "a")
    f2 = open("bf_approx_values.txt", "a")
    for i in range(1, 100):
        random_graph = random_weighted_graph_bf()
        dist = bellman_ford(random_graph, 0)
        f1.write(str(total_dist(dist)) + '\r')

        dist = bellman_ford_approx(random_graph, 0, i)
        f2.write(str(total_dist(dist)) + '\r')


def performance_test_bf_time():
    f1 = open("bf_values.txt", "a")
    f2 = open("bf_approx_values.txt", "a")
    for i in range(1, 1000):
        random_graph = random_weighted_graph_bf()

        start_time = timeit.default_timer()
        bellman_ford(random_graph, 0)
        end_time = timeit.default_timer()

        bf_time = end_time - start_time

        start_time = timeit.default_timer()
        bellman_ford_approx(random_graph, 0, i)
        end_time = timeit.default_timer()

        bf_approx_time = end_time - start_time

        f1.write(str(bf_time) + '\r')
        f2.write(str(bf_approx_time) + '\r')


performance_test_bf_time()
# performance_test_bf_distance()

g1 = DirectedWeightedGraph()
for _ in range(4):
    g1.add_node(_)
g1.add_edge(0,2,-2)
g1.add_edge(1,0,4)
g1.add_edge(1,2,-3)
g1.add_edge(3,1,-1)
g1.add_edge(2,3, 2)

g2 = DirectedWeightedGraph()
for _ in range(5):
    g2.add_node(_)
g2.add_edge(0,1,3)
g2.add_edge(0,3,-7)
g2.add_edge(0,4,8)
g2.add_edge(1,2,1)
g2.add_edge(1,3,4)
g2.add_edge(3,2,-2)
g2.add_edge(4,3,3)

g3 = DirectedWeightedGraph()
for _ in range(7):
    g3.add_node(_)
g3.add_edge(0,4,-1)
g3.add_edge(1,0,1)
g3.add_edge(1,3,2)
g3.add_edge(2,1,2)
g3.add_edge(2,5,-8)
g3.add_edge(3,0,-4)
g3.add_edge(3,4,3)
g3.add_edge(4,1,7)
g3.add_edge(5,1,5)
g3.add_edge(5,2,10)


def mystery_test():
    f = open("mystery.txt", "a")
    for v in range(2, 100):
        if v != (4, 5, 7):
            random_graph = create_random_complete_graph(v, 1000)
        elif v == 4:
            random_graph = g1
        elif v == 5:
            random_graph = g2
        else:
            random_graph = g3
        start_time = timeit.default_timer()
        mystery(random_graph)
        end_time = timeit.default_timer()

        f.write(str(v) + '\t' + str(end_time-start_time) + '\r')

# mystery_test()
