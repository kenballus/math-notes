# A = {-2,-1,0,1,2}
# S = {-2,-1,1,2,3}
A = {0,1,2,3,4}
S = {-2,-1,1,2,3}

edges = set()

counts = {}
for thing in S:
    counts[thing] = 0

for v1 in A:
    for v2 in A:
        if v1 == v2 or (v1 - v2) not in S:
            continue
        counts[v1 - v2] += 1
        edges.add((v2, v1))

print(edges)
print(len(edges))
print(counts)