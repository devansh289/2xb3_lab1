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


# def performance_test_bf_time():
#     f1 = open("bf_values.txt", "a")
#     f2 = open("bf_approx_values.txt", "a")
#     for i in range(1, 1001):
#         random_graph = random_weighted_graph()
#
#         start_time = timeit.default_timer()
#         bellman_ford(random_graph, 0)
#         end_time = timeit.default_timer()
#
#         bf_time = end_time-start_time
#
#
#         start_time = timeit.default_timer()
#         bellman_ford_approx(random_graph, 0, i)
#         end_time = timeit.default_timer()
#
#         bf_approx_time = end_time-start_time
#
#         f1.write(str(bf_time) + '\r')
#         f2.write(str(bf_approx_time) + '\r')


# performance_test_bf_time()
performance_test_bf_distance()
