Features for Graph Quest:
1. Turns user input from standard input into a graph of nodes and edges
2. Can filter graph/data frame through searches/minimum spanning trees and produce new graph/data frame
3. Allow for graph manipulation such as adding adn removing nodes, adding and removing edges, and saving data to specific nodes

Work in progress: 
4. Implements NetworkX to graph pandas data frame

1.
2. 
3. Allows users to manipulate graph data structures:
   -Graph Quest's main features revolve around the graph data structure. Graph Quest does most of its work through adjacency matrices which can represent a multitude of node and      edge graphs. These graphs include unweighted, weighted, and directional graphs.
   Along with representing the graphs through adjacency matrices, Graph Question can also:
   -Insert nodes
   -Remove nodes
   -Insert edges
   -Remove edges
   -Set edge weights
   -Set the graph name
   -Get the node and edge count
4. 
5. Allows user to perform search and other graph algorithms:
   -Graph Quest has a growing library of algorithms that you can perform on your graph datastructure. 
    Right now Graph quest can perform:
   -Breathd First Search (BFS)
   -Depth First Search (DPS)
   -Kruscal's Minimum Spanning tree (MST)
   -Cycle Detection
6. Allows users to create visualizations of their graphs.
   -Graph Quest uses the NetworkX library to allow you to visualize your graphs. In the code you can take your adjacency matrix and feed it into one of our functions to produce a     with the NetworkX library. This feature supports both weighted and unweighted graphs.
