from graphs import *
import random


def gen_random_graph(k, c):
    g = Graph(k)
    for i in range(c):
        g.add_edge(random.randint(0, k-1), random.randint(0, k-1))
    return g


def test():
    f = open("data.txt", "a")
    for i in range(100):
        my_graph = None
        cycle = 0
        no_cycle = 0
        for _ in range(100):
            my_graph = gen_random_graph(100, i)

            if has_cycle(my_graph):
                cycle += 1
            else:
                no_cycle += 1

        f.write(f"{i}\t{cycle/(no_cycle+cycle)}\n")
    f.close()


def test2():
    f = open("data2.txt", "a")
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

        f.write(f"{i}\t{connected / (not_connected + connected)}\n")
    f.close()
