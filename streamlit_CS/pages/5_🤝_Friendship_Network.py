import streamlit as st
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# --- Data setup ---
nodes = [
    "Alice", "Bob", "Charlie", "Diana", "Eve",
    "Frank", "Grace", "Hannah", "Ian", "Jack"
]
edges = [
    ("Alice","Bob"), ("Alice","Charlie"), ("Bob","Charlie"), ("Charlie","Diana"),
    ("Diana","Eve"), ("Bob","Diana"), ("Frank","Eve"), ("Eve","Ian"),
    ("Diana","Ian"), ("Ian","Grace"), ("Grace","Hannah"), ("Hannah","Jack"),
    ("Grace","Jack"), ("Charlie","Frank"), ("Alice","Eve"), ("Bob","Jack")
]

# --- Graph creation ---
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# --- Degree Analysis ---
degree_dict = dict(G.degree())
max_degree = max(degree_dict.values())
most_connected = [n for n, d in degree_dict.items() if d == max_degree]

# --- Centrality ---
betweenness = nx.betweenness_centrality(G)
closeness = nx.closeness_centrality(G)

# --- Community Detection (greedy modularity) ---
from networkx.algorithms.community import greedy_modularity_communities
communities = list(greedy_modularity_communities(G))
community_map = {}
for i, comm in enumerate(communities):
    for node in comm:
        community_map[node] = i

# --- Influence (Highest Betweenness) ---
influencer = max(betweenness, key=betweenness.get)

# --- Visualization ---
pos = nx.spring_layout(G, seed=42)

fig, ax = plt.subplots(figsize=(8,6))
colors = ['#FFDD57','#4CAF50','#2196F3','#FF5722','#9C27B0','#03A9F4']
node_colors = [colors[community_map[node]%len(colors)] for node in G.nodes()]
nx.draw_networkx_edges(G, pos, ax=ax)
nx.draw_networkx_nodes(
    G, pos, nodelist=G.nodes(), node_color=node_colors, edgecolors='k',
    node_size=[800 if node==influencer else 500 for node in G.nodes()],
    linewidths=2
)
nx.draw_networkx_labels(G, pos, font_weight='bold')
nx.draw_networkx_nodes(
    G, pos, nodelist=[influencer], node_color='#F44336', node_size=1000, label='Most Influential', edgecolors='black'
) # highlight influencer
plt.title("Friendship Network in a College Class")
plt.axis('off')
st.pyplot(fig)

# --- Findings Table ---
df_metrics = pd.DataFrame({
    "Degree": pd.Series(degree_dict),
    "Betweenness": pd.Series(betweenness),
    "Closeness": pd.Series(closeness),
    "Community": pd.Series(community_map)
}).sort_values(by="Degree", ascending=False)
st.subheader("Node Metrics")
st.dataframe(df_metrics, use_container_width=True)

# --- Key Findings Comments ---
st.markdown("### Key Findings")
st.markdown(f"""
- **Most Connected Individual(s):** {', '.join(most_connected)} (each with {max_degree} connections).
- **Top Influencer (Betweenness Centrality):** {influencer} (marked in red above).
- **Community Clusters:** Nodes are grouped by friendship communities (color-coded above).
- **Network Structure:** The network is moderately connected, with {G.number_of_nodes()} students and {G.number_of_edges()} friendships.
- **Observations:** Individuals like {influencer} play crucial roles in connecting multiple groups and spreading information. Community structure shows 2-3 friendship clusters in the class.
""")
