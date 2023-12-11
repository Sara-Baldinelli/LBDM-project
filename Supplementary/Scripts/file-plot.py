import math
import networkx as nx
import matplotlib.pyplot as plt
import operator
from matplotlib.pyplot import figure, text

G = nx.read_edgelist("network.txt")
print(G)
if len(G.nodes()) == 0:
    print("Error: The graph is empty or contains no nodes.")

# SAVE ONLY CONNECTED COMPONENTS
components = nx.connected_components(G)
largest_component = max(components, key=len)
H = G.subgraph(largest_component)

# NODE LENGTH BASED ON CENTRALITY MEASURES
centrality = nx.betweenness_centrality(H, k=20, endpoints=True)
node_size = [v * 10000 for v in centrality.values()]

# SELECT LABELS
print(centrality.items())
sorted_cen = dict(sorted(centrality.items(), key=operator.itemgetter(1), reverse=True))


def create_new_dictionary(old_dict, num_elements):
    keys = list(old_dict.keys())
    selected_keys = keys[:num_elements]
    new_dict = {key: key for key in selected_keys}
    return new_dict


new_dict = create_new_dictionary(sorted_cen, num_elements=45)  # num labels
H = nx.relabel_nodes(H, new_dict)

# NODE COLOR
lpc = nx.community.label_propagation_communities(H)
community_index = {n: i for i, com in enumerate(lpc) for n in com}
node_color = [community_index[n] for n in H]

# label_to_color = {'ACTR3B': 'purple', 'EBF1': 'purple', 'FAM156A': 'purple', 'GADD45G': 'purple', 'KCTD5': 'purple',
#                   'KIAA0319L': 'purple', 'MAOA': 'purple', 'PRDM2': 'purple'}
# label_to_size = {'ACTR3B': 1000, 'EBF1': 1000, 'FAM156A': 1000, 'GADD45G': 1000, 'KCTD5': 1000,
#                  'KIAA0319L': 1000, 'MAOA': 1000, 'PRDM2': 1000}
# node_color = [label_to_color.get(node, 'gray') for node in H.nodes]
# node_size = [label_to_size.get(node, 100) for node in H.nodes]

for i in H.nodes:
    print(i)
# PLOT
# pos = nx.spring_layout(H)
pos = nx.kamada_kawai_layout(H)
# pos = nx.spectral_layout(H)

fig, ax = plt.subplots(figsize=(20, 15))

nx.draw(H, pos, with_labels=True, labels=new_dict, font_weight='bold', node_size=node_size,
        node_color=node_color, font_size=8, edge_color='gray', alpha=0.7)

# nx.draw(H, pos, with_labels=False, font_weight='bold', node_size=node_size,
#         node_color=node_color, font_size=8, edge_color='gray', alpha=0.5)
# for node, (x, y) in pos.items():
#     text(x, y, node, fontsize=10, ha='center', va='center')
# nx.draw_networkx_labels(H, pos, font_size=6.5, labels=new_dict)

# nx.draw_networkx(H, pos, with_labels=True, labels=new_dict, font_weight='bold', node_size=node_size,
#         node_color=node_color, font_size=8, edge_color='gray', alpha=0.4)

# font = {"color": "k", "fontweight": "bold", "fontsize": 15}
# ax.set_title("MB HSG: Causal relations Network", font)
ax.margins(0.05, 0.05)
fig.tight_layout()
plt.axis("off")
plt.show()
