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
    - Look for: Is distribution skewed? Where are most students?
    """)

fig2 = px.histogram(
    df, 
    x='gpa',
    nbins=15,
    color_discrete_sequence=['#1f77b4'],
    title='Distribution of Student GPAs',
    labels={'gpa': 'GPA', 'count': 'Number of Students'},
    template='plotly_white'
)
fig2.update_layout(height=400, showlegend=False)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
**Observations:**
- GPA distribution is roughly normal (bell-shaped) centered around 3.2-3.3
- No strong left or right skew, indicating balanced academic performance
- Very few students below 2.5 or above 3.9
- The concentration around 3.2-3.5 represents 60 percent of students
""")

st.markdown("---")

# CHART 3
st.markdown("## Chart 3: Study Hours vs. Final Exam Score (Scatter Plot)")

with st.expander("How to Read This Chart", expanded=False):
    st.markdown("""
    - X-axis: Weekly study hours (0-25 hours per week)
    - Y-axis: Final exam score (0-100 points)
    - Color: Academic major
    - Dot size: Represents attendance rate
    - Look for: Do students who study more score higher?
    """)

fig3 = px.scatter(
    df,
    x='study_hours_per_week',
    y='final_score',
    color='major',
    size='attendance_rate',
    hover_data={'study_hours_per_week': True, 'final_score': ':.1f', 'major': True},
    title='Study Hours vs. Final Exam Score',
    labels={'study_hours_per_week': 'Study Hours/Week', 'final_score': 'Final Score'},
    template='plotly_white',
    color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
)
fig3.update_traces(marker=dict(opacity=0.7))
fig3.update_layout(height=400)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
**Observations:**
- Weak positive correlation between study hours and final score
- Students studying 10-15 hours per week show best average outcomes
- Some students with low study hours still score 80 plus
- Study quality matters more than quantity
- Attendance rate shows stronger correlation than study hours
""")

st.markdown("---")

# CHART 4
st.markdown("## Chart 4: Final Exam Score by Academic Standing (Box Plot)")

with st.expander("How to Read This Chart", expanded=False):
    st.markdown("""
    - X-axis: Academic standing categories
    - Y-axis: Final exam scores (0-100)
    - Box: Contains middle 50 percent of data
    - Line in box: The median (middle value)
    - Whiskers: Data range excluding outliers
    - Dots: Individual outliers
    - Look for: Which standing has highest/lowest scores?
    """)

st.markdown("**Interactive Filter:**")
selected_standings = st.multiselect(
    "Select academic standing to display:",
    options=sorted(df['academic_standing'].unique()),
    default=sorted(df['academic_standing'].unique())
)

filtered_df = df[df['academic_standing'].isin(selected_standings)]

fig4 = px.box(
    filtered_df,
    x='academic_standing',
    y='final_score',
    color='academic_standing',
    title='Final Exam Score Distribution by Academic Standing',
    labels={'academic_standing': 'Academic Standing', 'final_score': 'Final Score'},
    template='plotly_white',
    color_discrete_sequence=['#2ca02c', '#1f77b4', '#d62728']
)
fig4.update_layout(height=400, showlegend=False)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
**Observations:**
- Dean's List students have median final score of 85 with tight distribution
- Probation students show median of 71 with large spread (inconsistent)
- Good Standing students center at 78
- Outliers exist in all groups
- Probation group shows most variability
""")

st.markdown("---")

st.markdown("## Key Takeaways from EDA")
st.info("""
1. GPA varies by major but all cluster around 3.1-3.4 average
2. Study hours show weak direct correlation with final scores
3. Attendance rate is a stronger predictor than study hours
4. Academic standing strongly reflects performance
5. Data shows 351 unique student records with diverse backgrounds
""")

st.markdown("---")
st.caption("All visualizations are interactive. Hover to see values, click legend to toggle visibility.")
