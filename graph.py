import networkx as nx
import matplotlib.pyplot as plt
import random

#Creating a graph
G = nx.Graph()

#Adding nodes the the graph created

# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_node(4)
# G.add_node(5)
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_node(4)
# G.add_node(5)

for i in range(1,11): #Using loop is so easy and clean
    G.add_node(i)

#Adding an edge between two nodes

# G.add_edge(1,2)
# G.add_edge(3,5)
# G.add_edge(4,1)
# G.add_edge(1,3)
# G.add_edge(5,4)

for i in range(1,11): #Using loop reduces our code in number of lines
    G.add_edge(random.randint(1,10),random.randint(1,10))

print(G.edges()) #Prints all edged in the graph

#nx.draw(G) #Displays graph without edges labelled
nx.draw(G,with_labels=1) #Displays graph with edges labelled
plt.show()