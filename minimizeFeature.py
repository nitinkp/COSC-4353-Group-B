import pandas as pd
import numpy as np
import os

INF = 999
# number of vertices in graph
nodes = int(input("Enter number of nodes: "))
# creating graph by adjacency matrix method
edges = int(input("Enter number of edges: "))

# g = np.array([[0, 19, 5, 0, 0],
#               [19, 0, 5, 9, 2],
#               [5, 5, 0, 1, 6],
#               [0, 9, 1, 0, 1],
#               [0, 2, 6, 1, 0]])

input_folder = 'Minimizing-inputs'

inputs_list = []

for f1, f2, f3 in os.walk(input_folder):
    for file in f3:
        inputs_list.append(os.path.join(f1, file))

# print(inputs_list)
given_num = int(input("choose one file from the available inputs as a number between 0 - 4: "))

file_name = ""

for i in range(given_num):
    if i == 0:
        file_name = inputs_list[0]
    elif i == 1:
        file_name = inputs_list[1]
    elif i == 2:
        file_name = inputs_list[2]
    elif i == 3:
        file_name = inputs_list[3]
    elif i == 4:
        file_name = inputs_list[4]

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

# cons.replace("'", "[")
li = cons.split('\n')
li2 = [e.split(',') for e in li]
g = []
for e in li2:
    li4 = []
    for j in e:
        li4.append(int(j))
    g.append(li4)
# print(li3)

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
    df2 = pd.DataFrame(out, columns=["Edge", "Weight"])
    # print(df2)
    # print(out)
    selected_node[b] = True
    edges += 1

try:
    print("The dataframe for minimum spanning tree graph is: ")
    print(df2)
    # print(df2.values.tolist())
    print(selected_node)
except:
    print("Enter appropriate values for nodes and edges and try again")
