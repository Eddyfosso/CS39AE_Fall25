# 🔗 Friendship Network Analysis - Streamlit App
## CS39AE Fall 2025 - Network Analysis Portfolio Project

---

## 📋 Project Overview

This Streamlit application analyzes a friendship network from a college class, performing comprehensive network science analysis including:

✅ **Network Visualization** - Interactive graph showing all connections  
✅ **Degree Analysis** - Identifies most connected individuals  
✅ **Centrality Measures** - Betweenness and closeness centrality calculations  
✅ **Community Detection** - Identifies friendship clusters/groups  
✅ **Influence Analysis** - Determines most influential person in network  

---

## 🎯 Assignment Task Completion

### ✓ Task 1: Visualize the Network
- **Location**: Network Visualization page
- **What it shows**: Interactive graph with nodes (people) and edges (friendships)
- **Finding**: Shows all 10 people and 15 connections in an easy-to-understand layout
- **Code**: Uses NetworkX spring layout algorithm for optimal positioning

### ✓ Task 2: Degree Analysis
- **Location**: Degree Analysis page
- **What it shows**: Bar chart ranking each person by number of friends
- **Finding**: [See your results when you run the app]
- **Code**: Counts degree of each node in the graph

### ✓ Task 3: Centrality Measures
- **Location**: Centrality Measures page
- **What it shows**: Two separate analyses - Betweenness and Closeness
- **Findings**:
  - **Betweenness**: High values indicate people who act as "bridges" connecting different groups
  - **Closeness**: High values indicate people at the "center" of the network
- **Code**: Uses NetworkX centrality algorithms

### ✓ Task 4: Community Detection
- **Location**: Community Detection page
- **What it shows**: Groups of people who are closely connected
- **Finding**: Identifies natural friendship clusters within the class
- **Code**: Uses Greedy Modularity Communities algorithm

### ✓ Task 5: Identify Most Influential
- **Location**: Influence Analysis page & Network Visualization (gold node)
- **What it shows**: 
  - Ranking of all people by influence score
  - Most influential person highlighted in GOLD color
  - Detailed metrics for the most influential person
- **Finding**: Combines degree, betweenness, and closeness for comprehensive influence score
- **Code**: Weighted combination: 40% Betweenness + 40% Closeness + 20% Degree

---

## 🚀 How to Set Up & Deploy

### Step 1: Download the App Files

Navigate to your GitHub repository folder structure:
```
CS39AE_Fall25/
└── streamlit_CS/
    ├── app.py                    (← Our new app file)
    ├── requirements.txt          (← Dependencies)
    ├── README.md                 (← This file)
    └── [other folders/files]
```

### Step 2: Install Dependencies Locally

Before deploying, test locally:

```bash
# Navigate to your project directory
cd CS39AE_Fall25/streamlit_CS

# Create a Python virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

### Step 3: Run Locally to Test

```bash
streamlit run app.py
```

This will open the app in your browser at `http://localhost:8501`

**Test Checklist:**
- [ ] All 6 pages load without errors
- [ ] Visualizations display correctly
- [ ] All metrics calculate properly
- [ ] Most influential person is highlighted in gold

### Step 4: Deploy to Streamlit Cloud (FREE!)

#### Option A: Streamlit Cloud (RECOMMENDED - Easiest)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Add friendship network analysis app"
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit: https://streamlit.io/cloud
   - Click "Sign in with GitHub"
   - Connect your GitHub account

3. **Create New App**
   - Click "New app" button
   - Select repository: `CS39AE_Fall25`
   - Select branch: `main`
   - Set main file path: `streamlit_CS/app.py`
   - Click "Deploy"

4. **Streamlit Cloud will generate your URL**
   - Format: `https://[your-username]-cs39ae-fall25.streamlit.app`
   - Share this link for your submission!

#### Option B: Heroku (Alternative)

If Streamlit Cloud doesn't work:

1. Create `Procfile` in your streamlit_CS folder:
   ```
   web: streamlit run --server.port $PORT app.py
   ```

2. Deploy to Heroku:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

---

## 📊 Understanding the Code

### Key Components

**1. Data Setup**
```python
NODES = ["Alice", "Bob", "Charlie", ...]  # 10 people
EDGES = [("Alice", "Bob"), ...]           # 15 connections
```

**2. Network Creation**
```python
G = nx.Graph()  # Create undirected graph (friendships are mutual)
G.add_nodes_from(NODES)
G.add_edges_from(EDGES)
```

**3. Degree Analysis**
- **What**: Counts friends per person
- **Formula**: Degree = Number of edges connected to a node
- **Interpretation**: Higher degree = more social connections

**4. Betweenness Centrality**
- **What**: How often someone is on shortest paths between others
- **Formula**: NetworkX implementation uses Brandes' algorithm
- **Interpretation**: High value = acts as bridge between groups

**5. Closeness Centrality**
- **What**: Average distance to all other nodes
- **Formula**: 1 / (average shortest path length)
- **Interpretation**: High value = close to everyone

**6. Community Detection**
- **Algorithm**: Greedy Modularity Communities
- **What**: Clusters nodes that are more connected internally than externally
- **Interpretation**: Natural friendship groups

**7. Influence Score**
```python
Influence = 0.4 × Betweenness + 0.4 × Closeness + 0.2 × Degree
```
- Weights can be adjusted based on importance
- Current weights: Bridges and central people are equally important

---

## 🔍 How to Interpret Results

### Degree Analysis Results
```
Person: Degree (number of friends)
Alice:  3 friends
Bob:    4 friends (highest = most connected)
Charlie: 4 friends
...
```
**Interpretation**: Bob and Charlie have the most direct friendships.

### Centrality Results

**High Betweenness:**
- Acts as information bottleneck
- Removing them would disconnect network
- Good candidate for spreading news

**High Closeness:**
- Central position in network
- Can reach everyone quickly
- Good candidate for organization roles

**High Degree + High Betweenness:**
- Influential connector
- Bridges different friend groups

### Community Results
```
Community 1: Alice, Bob, Charlie, Diana, Eve
Community 2: Frank, Ian
Community 3: Grace, Hannah, Jack
```
**Interpretation**: These groups have tighter internal connections.

---

## 💻 Customization Guide

### Want to modify the influence formula?
Find this line in the code:
```python
influence_score[node] = (
    0.4 * betweenness[node] +
    0.4 * closeness[node] +
    0.2 * degree_normalized[node]
)
```

Change the weights (0.4, 0.4, 0.2) to your preference. They must sum to 1.0:
- **Increase betweenness weight**: Emphasize bridge roles
- **Increase closeness weight**: Emphasize central positions
- **Increase degree weight**: Emphasize direct connections

### Want to change the color scheme?
Find this line:
```python
colors = px.colors.qualitative.Set3
```

Options: `Set1`, `Set2`, `Set3`, `Pastel1`, `Dark2`, etc.

### Want to add more people or connections?
Modify the NODES and EDGES lists at the top:
```python
NODES = ["Alice", "Bob", ..., "NewPerson"]
EDGES = [("Alice", "Bob"), ..., ("NewPerson", "OtherPerson")]
```

---

## 📤 Submission Instructions

### For Your Portfolio:

1. **Deploy the app** (follow Step 4 above)

2. **Get your Streamlit URL**
   - Format: `https://[your-username]-[app-name].streamlit.app`
   - Example: `https://eddyfosso-friendship-network.streamlit.app`

3. **Submit your app with a report**
   - Include the app URL
   - Add findings from each analysis
   - Document any customizations made
   - Include code comments explaining your analysis

4. **Example Submission Format:**
   ```
   Project: Friendship Network Analysis
   
   Live App URL: https://[your-url].streamlit.app
   
   Key Findings:
   - Most Connected Person: [Name] with [X] friends
   - Most Influential Person: [Name] (Influence Score: [X])
   - Number of Communities Detected: [X]
   - [Your observations about the network]
   
   Features Implemented:
   ✅ Network Visualization
   ✅ Degree Analysis
   ✅ Centrality Measures (Betweenness & Closeness)
   ✅ Community Detection
   ✅ Influence Analysis with Visual Highlighting
   ```

---

## 🐛 Troubleshooting

### App won't start locally
```bash
# Make sure all dependencies are installed
pip install -r requirements.txt

# Check Python version (should be 3.8+)
python --version
```

### Deployment fails on Streamlit Cloud
- Make sure `requirements.txt` is in the same folder as `app.py`
- Check that all file paths are relative, not absolute
- Verify GitHub repo is public

### Visualizations not showing
- Refresh your browser
- Clear cache: `streamlit cache clear`
- Restart the app: Press Ctrl+C and run `streamlit run app.py` again

---

## 📚 Resources & References

- **NetworkX Documentation**: https://networkx.org/
- **Streamlit Documentation**: https://docs.streamlit.io/
- **Network Science Concepts**: https://en.wikipedia.org/wiki/Network_science
- **Centrality Measures**: https://networkx.org/documentation/stable/reference/algorithms/centrality.html

---

## ✨ Additional Features You Could Add

1. **Node Filtering**: Let users select which people to analyze
2. **Shortest Path**: Find shortest path between any two people
3. **Network Statistics**: Average clustering coefficient, diameter, etc.
4. **Social Distance**: Calculate how many degrees of separation between people
5. **Export**: Download analysis results as CSV or PDF
6. **Custom Network**: Upload your own network data
7. **Animation**: Animate how the network changes over time

---

## 📝 Comments on Findings

### General Observations:
- **Network Density**: The friendship network is moderately sparse (not fully connected)
- **Social Hubs**: A few people emerge as central connectors
- **Clustering**: Natural friend groups form without forced partitioning
- **Information Spread**: The most influential person can reach diverse groups
- **Network Resilience**: Removing high-influence nodes would impact connectivity

### Real-World Applications:
- **Social Organizing**: Identify key people for spreading announcements
- **Crisis Communication**: Who needs to be informed to reach everyone?
- **Team Formation**: Build teams with natural communication paths
- **Influence Analysis**: Who can sway opinion across diverse groups?

---

**Created for CS39AE Fall 2025**
**Network Analysis & Visualization**
