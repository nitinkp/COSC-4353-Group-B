import pandas as pd
import numpy as np

# Funtion 1
# Return adjacency matrix pandas dataframe
# For Unweighted graph
def df_to_adj_matrix(df_col1, df_col2):
  cross_df = pd.crosstab(df_col1, df_col2)
  idx = cross_df.columns.union(cross_df.index)
  adj_df = cross_df.reindex(index=idx, columns = idx, fill_value = 0)
  return adj_df

# Function 2
# Returns pandas dataframe from adjacency matrix dataframe
# For Unweighted graph
def adj_mat_to_df(adj_df, column_list):
  headers = adj_df.columns
  edge_list = []
  for index, row in adj_df.iterrows():
    header_idx = 0
    for col in row:
      while col > 0:
        edge_list.append([index, headers[header_idx]])
        col -= 1
      header_idx += 1
  df = pd.DataFrame(edge_list, columns=column_list)
  return df

# Unweighted Graph
# Function 3
# Input: File File which consist of standard user graph input
# 1->2
# 2->1,3,4
# 3->2
# 4->2
# 5->2,6,7
# 6->5,7
# 7->5,6
# Output: Return the edge list from the standard input
# [[1, 2], [2, 1], [2, 3], [2, 4], [3, 2], [4, 2], [5, 2], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6]]
def get_edgelist_from_graph(fileName):
  f = open(fileName, "r")
  edge_list = []
  for line in f.readlines():
      node_list = line.strip().split('->')
      from_node = node_list[0]
      to_node_list = node_list[1].strip().split(',');
      for node in to_node_list:
        edge_list.append([int(from_node), int(node)])

  return np.array(edge_list)


# Unweighted graph
# Function 4
# Input : File which consist of standard user graph input and is zero indexed or not
# 1->2
# 2->1,3,4
# 3->2
# 4->2
# 5->2,6,7
# 6->5,7
# 7->5,6
# Output: Return an adjacency matrix of the user input's graph
# [[0 1 0 0 0 0 0]
#  [1 0 1 1 0 0 0]
#  [0 1 0 0 0 0 0]
#  [0 1 0 0 0 0 0]
#  [0 1 0 0 0 1 1]
#  [0 0 0 0 1 0 1]
#  [0 0 0 0 1 1 0]]
def get_adj_mat(fileName, zero_indexed = False):
  edge_list = get_edgelist_from_graph(fileName)
  if not zero_indexed:
    edge_list = [[x - 1 for x in edge] for edge in edge_list]

  size = len(set([n for e in edge_list for n in e])) 
  adjacency = [[0]*size for _ in range(size)]
  for sink, source in edge_list:
      adjacency[sink][source] += 1
      
  return np.array(adjacency)

# Function 5
# Weighted / Unweighted
# Input :  CSV file consisting of adj matrix
# "graph3mat.csv" or "graph1weightedMat.csv"
# Output : Numpy array of adj matrix
def csv_to_numpy_adjmat(fileName):
  adj_mat = np.genfromtxt(fileName, delimiter=',')
  return  np.array(adj_mat, dtype=np.int)

# Funtion 6
# Weighted / Unweighted
# Input : Numpy array of adj matrix
# Output :  CSV file consisting of adj matrix
# "graph3mat.csv" or "graph1weightedMat.csv"
def adj_mat_to_csv(adj_mat, path=""):
  np.savetxt(path + "adjMatrix.csv", adj_mat, delimiter=",", fmt='%i')

