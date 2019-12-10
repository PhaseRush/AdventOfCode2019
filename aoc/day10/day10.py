# 125 ms

import math

mat = [list(x) for x in open('input.txt').read().split('\n')]

coordinates = []

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == '#':
            coordinates.append((i, j))

ans = (0, 0, 0, set())

for (r, c) in coordinates:
    seen = set()
    for (rr, cc) in coordinates:
        if r == rr and c == cc:
            continue
        dr = rr - r
        dc = cc - c
        g = math.gcd(dr, dc)
        seen.add((-dr // g, dc // g))
    if len(seen) > ans[0]:
        ans = (len(seen), r, c, seen)

ans, r, c, seen = ans
print(ans)

to_sort = []
for (dr, dc) in seen:
    key = math.atan2(dr, dc)
    if key > math.pi / 2.0:
        key -= 2 * math.pi
    to_sort.append((key, (dr, dc)))
to_sort = list(reversed(sorted(to_sort)))
winner = to_sort[199][1]
rr = r - winner[0]
cc = c + winner[1]
while mat[rr][cc] != '#':
    rr -= winner[0]
    cc += winner[1]
assert mat[rr][cc] == '#'
print(cc * 100 + rr)
