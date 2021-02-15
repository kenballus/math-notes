import sys
import math
import random

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.n = 0

    def add_edge(self, v1, v2):
        for v in v1, v2:
            if v not in self.adj_list:
                self.add_node(v)
        
        self.adj_list[v1].add(v2)
        self.adj_list[v2].add(v1)

    def add_node(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = set()
            self.n += 1

    def neighbors(self, v):
        return self.adj_list[v]

def read_graph(filename):
    g = Graph()
    for line in open(filename).readlines():
        if line.strip()[0] == "#":
            continue

        orig_line = line
        line = line.split()
        
        if len(line) == 1:
            g.add_node(line[0])
        elif len(line) == 2:
            g.add_edge(line[0], line[1])
        else:
            print("Error:", line, "contains more than 2 entries.")

    return g

def circle_tikz(g, radius=1, node_color="white", node_size=3, label=False, label_x_offset=0, label_y_offset=.35):
    """ Prints out a tikz picture of g, with its vertices along a circle of radius r """
    pt_locs = {}

    print("\\begin{tikzpicture}")
    for i, v in enumerate(g.adj_list):
        x = round(radius * math.cos(2 * math.pi * i / g.n), 3)
        y = round(radius * math.sin(2 * math.pi * i / g.n), 3)
        pt_locs[v] = x, y
        print(f"\\draw[fill={node_color}] ({x}, {y}) circle ({node_size}pt);")
        if label:
            print(f"\\node at ({x + label_x_offset}, {y + label_y_offset}) " + "{$" + f"{v}" + "$};")
    
    print()
    for v1 in g.adj_list:
        for v2 in g.neighbors(v1):
            print(f"\\draw[thick] {pt_locs[v1]} -- {pt_locs[v2]};")

    print("\\end{tikzpicture}")

def bipartitize(g):
    """ If g is bipartite, partitions it into its partite sets. Otherwise, partitions g into two useless sets. """

    def bipartite_dfs(g, root, p1, p2):
        for neighbor in g.neighbors(root):
            new = neighbor not in p1.union(p2)
            if root in p1:
                p2.add(neighbor)
            elif root in p2:
                p1.add(neighbor)
            else:
                print("Node", root, "is not in either partite set.", file=sys.stderr)
                sys.exit(1)

            if new:
                bipartite_dfs(g, neighbor, p1, p2)


    p1 = set()
    p2 = set()
    while p1.union(p2) != set(g.adj_list):
        for root in g.adj_list:
            if root not in p1.union(p2):
                break

        p1.add(root)
        bipartite_dfs(g, root, p1, p2)

    return p1, p2

def bipartite_tikz(g, h_space=1, v_space=1, node_color="white", node_size=3, label=False, label_x_offset=0, label_y_offset=.35):
    pt_locs = {}

    p1, p2 = bipartitize(g)

    print("\\begin{tikzpicture}")
    p1_ctr = 0
    p2_ctr = 0
    for v in g.adj_list:
        if v in p1:
            x = p1_ctr * h_space
            p1_ctr += 1
            y = 0
        elif v in p2:
            x = p2_ctr * h_space
            p2_ctr += 1
            y = v_space

        pt_locs[v] = x, y
        print(f"\\draw[fill={node_color}] ({x}, {y}) circle ({node_size}pt);")
        if label:
            print(f"\\node at ({x + label_x_offset}, {y + label_y_offset}) " + "{$" + f"{v}" + "$};")

    print()
    for v1 in g.adj_list:
        for v2 in g.neighbors(v1):
            print(f"\\draw[thick] {pt_locs[v1]} -- {pt_locs[v2]};")

    print("\\end{tikzpicture}")

def random_tikz(g, radius=1, node_color="white", node_size=3, label=False, label_x_offset=0, label_y_offset=.35):
    pt_locs = {}

    print("\\begin{tikzpicture}")
    for v in g.adj_list:
        x = round(random.random() * radius * 2 - radius, 3)
        y = round(random.random() * radius * 2 - radius, 3)
        pt_locs[v] = x, y
        print(f"\\draw[fill={node_color}] ({x}, {y}) circle ({node_size}pt);")
        if label:
            print(f"\\node at ({x + label_x_offset}, {y + label_y_offset}) " + "{$" + f"{v}" + "$};")

    print()
    for v1 in g.adj_list:
        for v2 in g.neighbors(v1):
            print(f"\\draw[thick] {pt_locs[v1]} -- {pt_locs[v2]};")

    print("\\end{tikzpicture}")

def main():
    if len(sys.argv) != 3:
        print("USAGE: python3 translate_to_tikz.py <bipartite|circle|random> <filename>", file=sys.stderr)
        print()
        print("This program expects its input to be a list of edges, each on its own line.", file=sys.stderr)
        print("Don't try to put big graphs in here; it'll be too slow.")
        sys.exit(1)

    g = read_graph(sys.argv[2])

    mode = sys.argv[1]
    if mode == "bipartite":
        bipartite_tikz(g)
    elif mode == "random":
        random_tikz(g)
    elif mode == "circle":
        circle_tikz(g, label=True, radius=3)
    else:
        print("Invalid graph mode:", mode, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
