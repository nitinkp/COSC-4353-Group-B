import pandas as pd
import os

input_folder = 'Adjacency matrices'

inputs_list = []

for f1, f2, f3 in os.walk(input_folder):
    for file in f3:
        inputs_list.append(os.path.join(f1, file))

print(inputs_list)
given_num = int(input("choose one file from the available inputs as a number starting with 0: "))

file_name = ""

for i in range(given_num):
    print(i)
    try:
        file_name = inputs_list[i + 1]
    except:
        print("Provide input from given files")

# print(file_name)
# cons = []
# con = ""
with open(file_name) as r:
    try:
        cons = r.read()
        # print(cons)
        # con += cons
    except:
        pass
i = i + 1

li = cons.split('\n')
li2 = [e.split(',') for e in li]
g = []
for e in li2:
    li4 = []
    for j in e:
        li4.append(int(j))
    g.append(li4)


def matrix_to_list(g):
    graph = {}
    for i, node in enumerate(g):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
        graph[i] = adj
    return graph


# matrix = [[0, 19, 5, 0, 0],
#           [19, 0, 5, 9, 2],
#           [5, 5, 0, 1, 6],
#           [0, 9, 1, 0, 1],
#           [0, 2, 6, 1, 0]]


def bfs(graph, v):
    visited = []
    Q = [v]
    while Q:
        v = Q.pop(0)
        visited.append(v)
        for n in graph[v]:
            if n not in Q and \
                    n not in visited:
                Q.append(n)
    return visited


gr = matrix_to_list(g)
print(bfs(gr, 4))
