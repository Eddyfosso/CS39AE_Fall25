import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="EDA Gallery", page_icon="📊", layout="wide")

st.markdown("# Exploratory Data Analysis Gallery")
st.markdown("""
Exploring patterns, distributions, and relationships in student learning data.
Each chart includes a "How to Read" guide and key observations.
""")
st.markdown("---")

@st.cache_data
def load_data():
    df = pd.read_csv("data/Student_Learning_Analytics.csv")
    return df

df = load_data()

st.caption(f"""
Data Source: Student Learning Analytics  
Records: {len(df)} students | Features: {len(df.columns)} columns  
Last Updated: November 2024
""")

# CHART 1
st.markdown("## Chart 1: Average GPA by Major (Bar Chart)")

with st.expander("How to Read This Chart", expanded=False):
    st.markdown("""
    - X-axis: Different academic majors
    - Y-axis: Average GPA (0-4.0 scale)
    - Bar height: Average performance in that major
    - Look for: Which majors have highest/lowest average GPA?
    """)

gpa_by_major = df.groupby('major')['gpa'].mean().reset_index().sort_values('gpa', ascending=False)

fig1 = px.bar(
    gpa_by_major, 
    x='major', 
    y='gpa',
    color='gpa',
    color_continuous_scale='Blues',
    title='Average GPA by Major',
    labels={'major': 'Major', 'gpa': 'Average GPA'},
    template='plotly_white'
)
fig1.update_layout(showlegend=False, height=400)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
**Observations:**
- Physics majors have the highest average GPA at 3.41
- Business majors have the lowest average GPA at 3.10
- The 0.31 GPA spread indicates major choice correlates with performance
- Data Science shows consistently high performance (3.39)
""")

st.markdown("---")

# CHART 2
st.markdown("## Chart 2: Overall GPA Distribution (Histogram)")

with st.expander("How to Read This Chart", expanded=False):
    st.markdown("""
    - X-axis: GPA ranges (bins) from 2.3 to 4.0
    - Y-axis: Number of students in each GPA range
    - Bar height: How many students in that GPA band
    - Look for: Is distribution skewed? Where are most s
