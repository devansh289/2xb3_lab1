from mst import *
from lab8 import *
import random
import timeit


def random_weighted_graph(v):
    graph = WeightedGraph(v)
    weights = list(range(0, v+1000))
    random.shuffle(weights)
    nodes = list(range(0, v))

    while(len(nodes) > 1):
        node_a = random.sample(nodes, 1)[0]
        nodes.remove(node_a)
        node_b = random.sample(nodes, 1)[0]
        graph.add_edge(node_a, node_b, weights.pop(0))

    return graph


def performance_test():
    f = open("performance.txt", "a")
    for v in range(2, 100):
        random_graph = random_weighted_graph(v)
        start_time = timeit.default_timer()
        prim1(random_graph)
        end_time = timeit.default_timer()
        prim2(random_graph)
        end_time2 = timeit.default_timer()

        f.write(str(v) + '\t' + str(end_time-start_time) + '\t' +
                str(end_time2 - end_time) + '\r')


performance_test()
