import streamlit as st
import networkx as nx
import plotly.graph_objects as go
import pandas as pd
from itertools import combinations

st.set_page_config(page_title="Network Analysis", page_icon="🌐", layout="wide")

st.markdown("# Friendship Network Analysis")
st.markdown("""
Analyzing a college class friendship network using graph theory and network science techniques.
""")
st.markdown("---")

# ============================================================================
# DATASET: Friendship Network in College Class
# ============================================================================

# Create the graph
G = nx.Graph()

# Nodes (10 students)
nodes = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack']
G.add_nodes_from(nodes)

# Edges (16 friendships)
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

st.caption(f"""
**Dataset Overview:**
- Nodes (Students): {len(G.nodes())}
- Edges (Friendships): {len(G.edges())}
- Network Density: {nx.density(G):.3f}
""")

st.markdown("---")

# ============================================================================
# SECTION 1: Network Visualization
# ============================================================================

st.markdown("## 1. Network Graph Visualization")

# Calculate centrality to color nodes
betweenness = nx.betweenness_centrality(G)
max_betweenness = max(betweenness.values())
influential_node = max(betweenness, key=betweenness.get)

# Position layout using spring layout
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

# Create edge traces
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

# Create node traces
node_x = []
node_y = []
node_color = []
node_text = []

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    
    # Color: most influential node in different color
    if node == influential_node:
        node_color.append('red')
    else:
        node_color.append('lightblue')
    
    degree = G.degree(node)
    betweenness_val = betweenness[node]
    node_text.append(f"<b>{node}</b><br>Degree: {degree}<br>Betweenness: {betweenness_val:.3f}")

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=node_x,  # Placeholder
    textposition="top center",
    hoverinfo='text',
    hovertext=node_text,
    marker=dict(
        showscale=True,
        color=node_color,
        size=20,
        line_width=2,
        colorscale='YlOrRd'
    ),
    showlegend=False
)

# Add node labels
node_labels = go.Scatter(
    x=node_x, y=node_y,
    mode='text',
    text=nodes,
    textposition="middle center",
    textfont=dict(size=10, color='black', family='Arial Black'),
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

st.markdown("""
**Key Observation:**
- **Red node** = Most influential person (highest betweenness centrality)
- **Blue nodes** = Other network members
- **Lines** = Friendship connections
- Hover over nodes to see detailed metrics
""")

st.markdown("---")

# ============================================================================
# SECTION 2: Degree Analysis
# ============================================================================

st.markdown("## 2. Degree Analysis - Most Connected People")

degrees = dict(G.degree())
degree_df = pd.DataFrame(list(degrees.items()), columns=['Person', 'Degree']).sort_values('Degree', ascending=False)

st.markdown("**Who has the most friends?**")
col1, col2 = st.columns([2, 1])

with col1:
    fig_degree = go.Figure(data=[
        go.Bar(
            x=degree_df['Person'],
            y=degree_df['Degree'],
            marker=dict(color='#1f77b4'),
            text=degree_df['Degree'],
            textposition='outside'
        )
    ])
    fig_degree.update_layout(
        title='Number of Friends by Person',
        xaxis_title='Person',
        yaxis_title='Number of Friends (Degree)',
        height=400,
        showlegend=False,
        template='plotly_white'
    )
    st.plotly_chart(fig_degree, use_container_width=True)

with col2:
    st.markdown("**Top 3 Most Connected:**")
    for idx, (person, degree) in enumerate(degree_df.head(3).values, 1):
        st.metric(f"#{idx}", person, f"{int(degree)} friends")

st.markdown(f"""
**Insights:**
- **Most connected:** {degree_df.iloc[0]['Person']} with {int(degree_df.iloc[0]['Degree'])} friends
- **Least connected:** {degree_df.iloc[-1]['Person']} with {int(degree_df.iloc[-1]['Degree'])} friend(s)
- **Average degree:** {degree_df['Degree'].mean():.2f} friends per person
""")

st.markdown("---")

# ============================================================================
# SECTION 3: Centrality Measures
# ============================================================================

st.markdown("## 3. Centrality Analysis - Who Bridges Groups?")

# Calculate different centrality measures
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
degree_centrality = nx.degree_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# Create summary dataframe
centrality_df = pd.DataFrame({
    'Person': nodes,
    'Degree': [betweenness_centrality[node] for node in nodes],
    'Betweenness': [betweenness_centrality[node] for node in nodes],
    'Closeness': [closeness_centrality[node] for node in nodes],
    'Eigenvector': [eigenvector_centrality[node] for node in nodes]
}).sort_values('Betweenness', ascending=False)

st.markdown("**Centrality Measures Explained:**")
st.markdown("""
- **Degree Centrality:** How many direct friends you have
- **Betweenness Centrality:** How much you bridge different groups (high = important connector)
- **Closeness Centrality:** How close you are to everyone else (high = central position)
- **Eigenvector Centrality:** How connected your friends are (high = friends with important people)
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Betweenness Centrality (Bridge Effect)")
    fig_between = go.Figure(data=[
        go.Bar(
            y=centrality_df['Person'],
            x=centrality_df['Betweenness'],
            orientation='h',
            marker=dict(color='#d62728'),
            text=centrality_df['Betweenness'].round(3),
            textposition='outside'
        )
    ])
    fig_between.update_layout(height=400, showlegend=False, template='plotly_white')
    st.plotly_chart(fig_between, use_container_width=True)

with col2:
    st.markdown("### Closeness Centrality (Central Position)")
    fig_close = go.Figure(data=[
        go.Bar(
            y=centrality_df['Person'],
            x=centrality_df['Closeness'],
            orientation='h',
            marker=dict(color='#2ca02c'),
            text=centrality_df['Closeness'].round(3),
            textposition='outside'
        )
    ])
    fig_close.update_layout(height=400, showlegend=False, template='plotly_white')
    st.plotly_chart(fig_close, use_container_width=True)

st.dataframe(centrality_df.round(3), use_container_width=True)

st.markdown(f"""
**Key Finding:**
- **Most influential connector:** {centrality_df.iloc[0]['Person']} (Betweenness: {centrality_df.iloc[0]['Betweenness']:.3f})
  - This person connects different friendship groups
  - Critical for information spreading
""")

st.markdown("---")

# ============================================================================
# SECTION 4: Community Detection
# ============================================================================

st.markdown("## 4. Community Detection - Friendship Groups")

# Detect communities using Louvain algorithm
from networkx.algorithms import community
communities = list(community.greedy_modularity_communities(G))

st.markdown(f"**Detected {len(communities)} friendship groups:**")

community_info = []
for idx, comm in enumerate(communities, 1):
    members = list(comm)
    st.markdown(f"**Group {idx}:** {', '.join(members)} ({len(members)} members)")
    community_info.append({'Group': f'Group {idx}', 'Members': len(members), 'Names': ', '.join(members)})

community_df = pd.DataFrame(community_info)

fig_comm = go.Figure(data=[
    go.Bar(
        x=community_df['Group'],
        y=community_df['Members'],
        marker=dict(color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'][:len(community_df)]),
        text=community_df['Members'],
        textposition='outside'
    )
])
fig_comm.update_layout(
    title='Group Sizes',
    yaxis_title='Number of Members',
    height=300,
    showlegend=False,
    template='plotly_white'
)
st.plotly_chart(fig_comm, use_container_width=True)

st.markdown("""
**Insights:**
- Students naturally cluster into friendship groups
- Some people bridge multiple groups (bridges)
- Groups may share common interests or classes
""")

st.markdown("---")

# ============================================================================
# SECTION 5: Information Influence & Spreading
# ============================================================================

st.markdown("## 5. Most Influential Person for Information Spreading")

st.markdown(f"### 🌟 **{influential_node} is the Most Influential!**")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Betweenness Centrality", f"{betweenness[influential_node]:.3f}", "Bridges groups")

with col2:
    st.metric("Degree", G.degree(influential_node), "Direct connections")

with col3:
    st.metric("Closeness", f"{closeness_centrality[influential_node]:.3f}", "Close to all")

st.markdown(f"""
**Why {influential_node} is Most Influential:**

1. **Bridge Effect:** High betweenness means {influential_node} connects different friendship groups
2. **Direct Reach:** {influential_node} can directly contact {G.degree(influential_node)} people
3. **Information Spread:** If {influential_node} shares information:
   - It reaches multiple groups efficiently
   - Information doesn't get stuck in one cluster
   - Shortest paths to many people go through {influential_node}

**Real-World Example:**
- If organizing a campus event, {influential_node} is the key person to tell
- Information will spread fastest through {influential_node}
- {influential_node} can coordinate between different friendship groups
""")

st.markdown("---")

# ============================================================================
# SUMMARY & FINDINGS
# ============================================================================

st.markdown("## 📊 Summary of Findings")

st.info(f"""
**Network Statistics:**
- Total students: {len(G.nodes())}
- Total friendships: {len(G.edges())}
- Network density: {nx.density(G):.3f}
- Average connections: {sum(dict(G.degree()).values()) / len(G.nodes()):.1f} per person
- Number of communities: {len(communities)}

**Key People:**
1. **Most Connected:** {degree_df.iloc[0]['Person']} ({int(degree_df.iloc[0]['Degree'])} friends)
2. **Most Influential Bridge:** {influential_node} (connects different groups)
3. **Centrally Located:** {centrality_df.iloc[0]['Person']} (closest to everyone)

**Recommendations:**
- {influential_node} should be involved in any campus-wide initiatives
- {degree_df.iloc[0]['Person']} can help organize within their direct circle
- Focus on maintaining bridges between groups for network cohesion
""")

st.markdown("---")

st.caption("Network analysis using NetworkX and graph theory principles.")
```

---

## 5️⃣ Add This to Your Portfolio

### **Step 1: Create the File**
1. Go to: `https://github.com/Eddyfosso/CS39AE_Fall25/tree/main/streamlit_CS/pages`
2. Click **"Add file"** → **"Create new file"**
3. Filename: `5_🌐_Network_Analysis.py`
4. Paste the code above
5. Commit: `Add network analysis page`

---

### **Step 2: Update requirements.txt**

Add `networkx` to your root `requirements.txt`:
```
streamlit==1.31.1
pandas==2.2.1
plotly==5.18.0
numpy==1.26.4
networkx==3.2
```

Commit: `Add networkx dependency`

---

### **Step 3: Reboot App**

1. Go to: https://share.streamlit.io/
2. Click **"Manage app"**
3. Click **"Reboot app"**
4. Wait 3-5 minutes

---

## ✅ What This Page Includes:

- ✅ Network graph visualization (most influential node in RED)
- ✅ Degree analysis (who has most friends)
- ✅ Betweenness & Closeness centrality
- ✅ Community detection (friendship groups)
- ✅ Influence analysis & information spreading
- ✅ Summary findings with insights
- ✅ Well-commented code

---

## 🚀 Submit Your Updated App:

Once deployed:
```
Streamlit App: https://cs39aefall25-rwssrrkr62r6cz2cw7jnju.streamlit.app/

GitHub: https://github.com/Eddyfosso/CS39AE_Fall25
