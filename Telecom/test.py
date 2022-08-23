import streamlit as st
import os
import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Define the number of nodes
nodes = np.array(["v1", "v2", "v3", "v4", "v5"])
# Define the distance between nodes
row = np.array(["v1", "v1", "v2", "v3", "v2", "v3", "v3", "v4", "v5", "v5", "v5","v4"])
col = np.array(["v2", "v3", "v3", "v2", "v4", "v4", "v5", "v5", "v4", "v1", "v2","v1"])
value = np.array([10, 5, 2, 3, 1, 9, 2, 4, 6, 7, 4,8])
# Generate undirected graph
G = nx.Graph()
# Add a node to the graph
for i in range(0, np.size(nodes)):
    G.add_node(nodes[i])
# Add weighted edges
for i in range(0, np.size(row)):
    G.add_weighted_edges_from([(row[i], col[i], value[i])])
# Set network layout
pos = nx.shell_layout(G)
# Draw a network image
nx.draw(G, pos, with_labels=True, node_color='white', edge_color='b', node_size=800, alpha=0.5)
#plt.show()
#plt.ion() # Turn on interactive mode
#plt.title("slfe_Net")
#plt.ioff()
#plt.savefig("Graph.png", format="PNG")
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels)
#nx.draw_networkx_edge_labels(G, pos, edge_labels)
#image = Image.open('Graph.png')
plt.draw()
plt.pause(1)  # Interval seconds: 3s
plt.close()



'''
Shortest Path with dijkstra_path
'''

# dijkstra method to find the shortest path
start,end  = input("Please enter the start and end nodes separated by spaces:").split()
path = nx.dijkstra_path(G, source=start, target=end)
print('Path from node {} to {}:'.format(start, end), path)
distance = nx.dijkstra_path_length(G, source=start, target=end)
print('The distance from node {} to {} is: '.format(start, end), distance)
#print(f"The distance from {start} to {end} is: ...")
