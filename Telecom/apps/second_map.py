import streamlit as st
import os
import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
def app():
 # Define the number of nodes
 nodes = np.array(["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"])
 # Define the distance between nodes
 row = np.array(["a1", "a1", "a3", "a4", "a5", "a2", "a8", "a7", "a3", "a7", "a7", "a6", "a3","a8","a1","a5","a3","a5","a5","a1"])
 col = np.array(["a3", "a4", "a2", "a6", "a3", "a8", "a2", "a1", "a5", "a8", "a3", "a7", "a1","a1","a2","a6","a4","a4","a7","a6"])
 value = np.array([4, 5, 7, 9, 3, 10, 8, 6, 10, 2, 8, 4, 7,4.5,3,7,12,7,9,4.3,5.1])
 # Generate undirected graph
 G = nx.DiGraph()
 # Add a node to the graph
 for i in range(0, np.size(nodes)):
    G.add_node(nodes[i])
 # Add weighted edges
 for i in range(0, np.size(row)):
    G.add_weighted_edges_from([(row[i], col[i], value[i])])
 # Set network layout
 pos = nx.shell_layout(G)
 # Draw a network image
 nx.draw(G, pos, with_labels=True, node_color='green', edge_color='b', node_size=800, alpha=0.5)
 #plt.ion() # Turn on interactive mode
 #plt.title("slfe_Net")
 #plt.ioff()
 edge_labels = nx.get_edge_attributes(G, 'weight')
 nx.draw_networkx_edge_labels(G, pos, edge_labels)
 # nx.draw_networkx_edge_labels(G, pos, edge_labels)
 plt.draw()

 plt.savefig("Graph.png", format="PNG")
 image = Image.open('Graph.png')
 st.image(image)

 plt.pause(1)  # Interval seconds: 3s
 plt.close()

 # dijkstra method to find the shortest path
 start = st.text_input("Please enter the start nodes separated by spaces:")
 end = st.text_input("Please enter the end nodes separated by spaces:")
 path = nx.dijkstra_path(G, source=start, target=end)
 st.write('Path from node {} to {}:'.format(start, end), path)
 distance = nx.dijkstra_path_length(G, source=start, target=end)
 st.write('The distance from node {} to {} is: '.format(start, end), distance)
 st.write(f"The distance from {start} to {end} is: ...")