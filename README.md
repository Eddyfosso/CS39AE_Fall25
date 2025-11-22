# 🤝 College Friendship Network Analysis

A comprehensive Streamlit application for analyzing social connections within a college class using network science and graph theory.

## Overview

This project analyzes a friendship network of 10 college students across 16 connections, providing deep insights into:
- Network structure and connectivity
- Individual importance through multiple centrality measures
- Friendship clusters and communities
- Information spreading potential

## Features

### 1. **Network Overview** 📊
- Interactive network graph visualization
- Node size represents connectivity
- Color-coded by community membership
- Real-time hover information

### 2. **Degree Analysis** 🎯
- Identifies the most connected students
- Degree centrality scoring
- Visual ranking of social connectivity
- Bar chart representation

### 3. **Centrality Measures** 📍
Three complementary metrics:
- **Betweenness Centrality**: Who bridges different groups (information flow)
- **Closeness Centrality**: Who is closest to everyone on average
- **Eigenvector Centrality**: Influence through quality connections

### 4. **Community Detection** 👥
- Louvain algorithm-based clustering
- Identifies natural friendship groups
- Color-coded communities in visualization
- Community composition breakdown

### 5. **Influence & Insights** ⭐
- **Most Influential Person** (highlighted in GOLD)
- Compound influence scoring
- Bridge connectors and central hubs
- Information spreading analysis

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions

1. **Clone or download the project files**
```bash
cd path/to/project
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**
```bash
streamlit run network_analysis_app.py
```

4. **Access the app**
- Open your browser to `http://localhost:8501`
- The app will automatically reload on code changes

## Dataset

**Students (10 nodes):**
Alice, Bob, Charlie, Diana, Eve, Frank, Grace, Hannah, Ian, Jack

**Friendships (16 edges):**
- Alice: Bob, Charlie, Eve (3 friends)
- Bob: Alice, Charlie, Diana, Jack (4 friends)
- Charlie: Alice, Bob, Diana, Frank (4 friends)
- Diana: Charlie, Eve, Bob, Ian (4 friends)
- Eve: Diana, Frank, Ian, Alice (4 friends)
- Frank: Eve, Charlie (2 friends)
- Grace: Ian, Hannah, Jack (3 friends)
- Hannah: Grace, Jack (2 friends)
- Ian: Eve, Diana, Grace (3 friends)
- Jack: Hannah, Grace, Bob (3 friends)

## Key Findings

### Network Metrics
- **Network Density:** 0.356 (moderately connected)
- **Average Clustering Coefficient:** ~0.45 (tendency to form cliques)
- **Connected Components:** 1 (fully connected network)

### Most Connected Students
The analysis reveals who has the broadest direct connections within the class.

### Most Influential Person
Combines multiple centrality measures to identify who would be most effective at spreading information or influence throughout the network.

### Friendship Communities
Louvain algorithm identifies natural clusters of friends with strong internal connections.

## Network Analysis Concepts

### Degree Centrality
**Definition:** The number of direct connections
**Use:** Identifies popular individuals
**Formula:** degree / (n-1)

### Betweenness Centrality
**Definition:** Frequency of being on shortest paths between other nodes
**Use:** Identifies information brokers
**Value Range:** 0-1

### Closeness Centrality
**Definition:** Average distance to all other nodes
**Use:** Identifies quick communicators
**Value Range:** 0-1

### Eigenvector Centrality
**Definition:** Influence based on connections to influential people
**Use:** Identifies well-connected through important people
**Concept:** "You are who you know"

## How to Interpret the Visualizations

### Network Graph
- **Node Size:** Larger = more friends
- **Node Color:** Represents community membership
- **Gold Node:** Most influential person
- **Lines (Edges):** Direct friendships

### Bar Charts
- Show relative ranking of different metrics
- Helps identify patterns and outliers
- Sortable by student name or metric value

## Use Cases

1. **Social Science Research:** Study peer networks and influence patterns
2. **Marketing:** Identify key influencers for information campaigns
3. **Organization:** Understand team dynamics and collaboration
4. **Community Building:** Identify bridges between disconnected groups
5. **Crisis Management:** Find key communicators for rapid message spreading

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your GitHub repository
4. Streamlit automatically deploys your app
5. Share the live URL

### Option 2: Heroku
```bash
# Create Procfile and setup.sh (provided in deployment guide)
git push heroku main
```

### Option 3: Local Sharing
```bash
streamlit run network_analysis_app.py --server.address 0.0.0.0
# Share your IP and port with others
```

## Code Structure

```
network_analysis_app.py
├── Network Creation
├── Metrics Calculation
│   ├── Degree Centrality
│   ├── Betweenness Centrality
│   ├── Closeness Centrality
│   ├── Eigenvector Centrality
│   └── Community Detection
├── 5 Main Tabs
│   ├── Network Overview
│   ├── Degree Analysis
│   ├── Centrality Measures
│   ├── Community Detection
│   └── Influence & Insights
└── Visualizations
    ├── Network Graphs (Plotly)
    ├── Bar Charts
    └── Hover Information
```

## Dependencies

- **streamlit:** Web framework
- **networkx:** Graph analysis library
- **pandas:** Data manipulation
- **plotly:** Interactive visualizations
- **python-louvain:** Community detection algorithm
- **numpy:** Numerical operations

## Troubleshooting

### Issue: "Module not found" error
**Solution:** Ensure all dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: Graph doesn't display
**Solution:** Clear Streamlit cache
```bash
streamlit cache clear
```

### Issue: Slow performance
**Solution:** Close other applications, the spring layout algorithm is computationally intensive

## Advanced Customization

### Change Colors
Edit the `community_colors` dictionary in the code:
```python
community_colors = {0: '#FF6B6B', 1: '#4ECDC4', ...}
```

### Adjust Graph Layout
Modify spring layout parameters:
```python
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
# k: distance between nodes
# iterations: layout quality
# seed: reproducibility
```

### Add More Analysis
Add custom metrics in the `calculate_metrics()` function

## Learning Resources

- **NetworkX Documentation:** https://networkx.org
- **Graph Theory Basics:** https://brilliant.org/wiki/graph-theory/
- **Streamlit Guide:** https://docs.streamlit.io
- **Plotly Charts:** https://plotly.com/python/

## Academic References

1. Freeman, L. C. (1978). "Centrality in networks of personal interaction"
2. Blondel, V. D., et al. (2008). "Fast unfolding of communities in large networks"
3. Newman, M. E. J. (2010). "Networks: An Introduction"

## License

This project is open source and available for educational use.

## Contact & Support

For questions or improvements, feel free to:
- Check the code comments
- Review the Streamlit documentation
- Modify parameters and observe changes

## Future Enhancements

- [ ] Add network statistics export (CSV/JSON)
- [ ] Interactive node/edge filtering
- [ ] Shortest path analysis
- [ ] Temporal network analysis (if timeline data available)
- [ ] 3D network visualization
- [ ] Custom file upload for different networks

---

**Created:** 2024
**Version:** 1.0
**Status:** Production Ready
