A graph models a set of connections.Each graph is made up of nodes and edges
##G(V,E):Vertices/nodes and edges
##Two types of graphs:
 -directed graphs
 -undirected graphs
 
##Adjacency matrices:
A(i,j):1 if there is a connection between node i and node j
       otherwise 0

##Edge list representation
-create a Vertex class to store the neighbors(nodes) accordingly

- a tree structure must be connected and can never have loops while in the graph there are no such restrictions.

#A Vertex:"Node"
It can have a name:"key"
And also an additional information:"payload"

#An Edge:
 ## connects two vertices
 * may be one-way(directed graph or a digraph) or two-way

#A Cycle:
in a directed graph,it is a path that starts  and ends at the same vertex
#Acyclic Graph: 
a graph with no cycles
#DAG (Directed Acyclic Graph):
A directed graph with no cycles