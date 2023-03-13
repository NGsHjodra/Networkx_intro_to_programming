# import libraries

import networkx as nx
from matplotlib import pyplot as plt

# create a graph with networkx library
G = nx.Graph()

# add 6 nodes
G.add_nodes_from([1,2,3,4,5,6])

# kruskal's algorithm

# # add edges with weights
G.add_weighted_edges_from([(1,2,1),(2,3,6),(3,6,2),(1,4,1),(4,5,4),(5,6,6)])

# create a layout
vertices_pos = nx.spring_layout(G)

print(vertices_pos)

vertices_pos[1] = [0, 0]
vertices_pos[2] = [1, 0]
vertices_pos[3] = [2, 0]
vertices_pos[4] = [0, 1]
vertices_pos[5] = [1, 1]
vertices_pos[6] = [2, 1]

nx.draw(G, with_labels=True, pos=vertices_pos)
nx.draw_networkx_edge_labels(G, pos=vertices_pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

plt.savefig('graph-without.png')

# clean the graph
plt.clf()

T = nx.minimum_spanning_tree(G)

nx.draw(T, with_labels=True, pos=vertices_pos)
nx.draw_networkx_edges(T, pos=vertices_pos, edgelist=T.edges(), edge_color='r', width=2)
nx.draw_networkx_edge_labels(T, pos=vertices_pos, edge_labels=nx.get_edge_attributes(T, 'weight'))

plt.savefig('graph-with-mst-2.png')

plt.show()

# python cmd to create requirements.txt
# pip freeze > requirements.txt