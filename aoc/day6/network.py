import networkx as nx

with open("input.txt", 'r') as file:
    content = file.read().splitlines()


def bfs():
    graph = nx.Graph()
    graph.add_edges_from(i.split(')') for i in content)
    return nx.shortest_path_length(graph, "YOU", "SAN") - 2


print(bfs())
