Features:
1. Allows users to read in a text file or csv file adjacency matrix and create a graph data structure from it. The graph data structure read in can be turned into an adjacency matrix which can be used with out graph data structure. The 

2. Allows users to input a multi-line string from a file and then convert it into an adjacency matrix. This adjacency matrix can be used with both the graph data structure, which provides several base graph functions (insertion, deletion, etc.) as well as can be used with the bfs and kruscal's algorithms programs. Both of which perform functions on the graph data structure.

3. Graph Quest's main features revolve around the graph data structure. Graph Quest does most of its work through adjacency matrices which can represent a multitude of node and  edge graphs. These graphs include unweighted, weighted, and directional graphs.
Along with representing the graphs through adjacency matrices, Graph Question can also:
 -Insert nodes
 -Remove nodes
 -Insert edges
 -Remove edges
 -Set edge weights
 -Set the graph name
 -Get the node and edge count

4. Allows the user to perform Breadth First Search (BFS), Kruscal's minimum spanning tree (msp), and Djikstra's algorithm on graph data structure as an adjacency matrix. All of these functions also use the same adjacency matrix that can be worked with in the graph class.
   
5. Allows users to create visualizations of their graphs. Graph Quest uses the NetworkX library to allow you to visualize your graphs. In the code you can take your adjacency matrix and feed it into one of our functions to produce a visualization with the NetworkX library. This feature supports both weighted and unweighted graphs.

6. Allows user to perform cycle detection on directed graphs. The graph class allows for directed graphs and can be used to manipulate the directed graph just like a weighted or unweighted one. Cycle detection allows you to check for a circular path in a directed graph.
