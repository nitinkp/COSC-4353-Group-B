import pandas as pd
import numpy as np

INF = 999
# number of vertices in graph
nodes = int(input("Enter number of nodes: "))
# creating graph by adjacency matrix method
edges = int(input("Enter number of edges: "))

g = np.array([[0, 19, 5, 0, 0],
              [19, 0, 5, 9, 2],
              [5, 5, 0, 1, 6],
              [0, 9, 1, 0, 1],
              [0, 2, 6, 1, 0]])

df = pd.DataFrame(g)

# print(g)
#
# print(df)

selected_node = [0, 0, 0, 0, 0]

selected_node[0] = True
# print("before",selected_node)

# printing for edge and weight
# print("Edge : Weight\n")
out = []
while edges < nodes - 1:

    minimum = INF
    a = 0
    b = 0
    for m in range(nodes):
        if selected_node[m]:
            for n in range(nodes):
                if (not selected_node[n]) and g[m][n]:
                    # not in selected and there is an edge
                    if minimum > g[m][n]:
                        minimum = g[m][n]
                        a = m
                        b = n
    out += [[str(a) + " - " + str(b)] + [str(g[a][b])]]
    df2 = pd.DataFrame(out,columns=["Edge", "Weight"])
    # print(df2)
    # print(out)
    selected_node[b] = True
    edges += 1

print(df2)
print(selected_node)

