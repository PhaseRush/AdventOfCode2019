from collections import defaultdict as nyaaaaa
from collections import deque as deep

lines = [line.rstrip('\n') for line in open("input.txt").readlines()]


def bfs():
    global distances
    tree = nyaaaaa(set)
    for line in lines:
        big, small = line.split(')')
        tree[big].add(small)
        tree[small].add(big)
    distances = {}
    q = deep()
    q.append(('YOU', 0))
    while q:
        curr_node, distance = q.popleft()
        if curr_node in distances:
            continue  # seen
        distances[curr_node] = distance
        for child in tree[curr_node]:
            q.append((child, distance + 1))
    return distances['SAN'] - 2  # fuck this -2


print(bfs())
