from graphs import *
import random


def gen_random_graph(k, c):
    g = Graph(k)
    for i in range(c):
        g.add_edge(random.randint(0, k), random.randint(0, k))
    return g


def test():
    f = open("data.txt", "a")
    for i in range(100):
        my_graph = None
        connected = 0
        not_connected = 0
        for _ in range(100):
            my_graph = gen_random_graph(100, i)

            if is_connected(my_graph):
                connected += 1
            else:
                not_connected += 1

        f.write(connected/(not_connected+connected))
    f.close()


# def cycle_v_c():
#
