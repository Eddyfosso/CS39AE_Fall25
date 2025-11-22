import streamlit as st
import networkx as nx
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Network Analysis", page_icon="🌐", layout="wide")

st.markdown("# Friendship Network Analysis")
st.markdown("""
Analyzing a college class friendship network using graph theory.
""")
st.markdown("---")

# Create the graph
G = nx.Graph()

nodes = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack']
G.add_nodes_from(nodes)

edges = [
    ('Alice', 'Bob'),
    ('Alice', 'Charlie'),
    ('Bob', 'Charlie'),
    ('Charlie', 'Diana'),
    ('Diana', 'Eve'),
    ('Bob', 'Diana'),
    ('Frank', 'Eve'),
    ('Eve', 'Ian'),
    ('Diana', 'Ian'),
    ('Ian', 'Grace'),
    ('Grace', 'Hannah'),
    ('Hannah', 'Jack'),
    ('Grace', 'Jack'),
    ('Charlie', 'Frank'),
    ('Alice', 'Eve'),
    ('Bob', 'Jack')
]
G.add_edges_from(edges)

st.caption(f"Nodes: {len(G.nodes())} | Edges: {len(G.edges())}")

st.markdown("---")

# Network Visualization
st.markdown("## Network Graph")

betweenness = nx.betweenness_centrality(G)
influential_node = max(betweenness, key=betweenness.get)

pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    mode='lines',
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    showlegend=False
)

node_x = []
node_y = []
node_color = []
node_text = []

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    
    if node == influential_node:
        node_color.append('red')
    else:
        node_color.append('lightblue')
    
    degree = G.degree(node)
    node_text.append(f"<b>{node}</b><br>Degree: {degree}")

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=node_text,
    textposition="top center",
    hoverinfo='text',
    hovertext=node_text,
    marker=dict(size=20, color=node_color),
    showlegend=False
)

node_labels = go.Scatter(
    x=node_x, y=node_y,
    mode='text',
    text=list(G.nodes()),
    textposition="middle center",
    textfont=dict(size=10, color='black'),
    hoverinfo='skip',
    showlegend=False
)

fig = go.Figure(data=[edge_trace, node_trace, node_labels],
    layout=go.Layout(
        title='Friendship Network Graph',
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20, l=5, r=5, t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=500
    )
)

st.plotly_chart(fig, use_container_width=True)

st.markdown(f"**Most Influential: {influential_node}** (red node)")

st.markdown("---")

st.markdown("## Degree Analysis")

degrees = dict(G.degree())
degree_df = pd.DataFrame(list(degrees.items()), columns=['Person', 'Degree']).sort_values('Degree', ascending=False)

st.dataframe(degree_df, use_container_width=True)

st.info(f"**Most Connected:** {degree_df.iloc[0]['Person']} with {int(degree_df.iloc[0]['Degree'])} friends")
