from graphs import *
import random


def gen_random_graph(k, c):
    g = Graph(k)
    for i in range(c):
        g.add_edge(random.randint(0, k), random.randint(0, k))


# def cycle_v_c():
#