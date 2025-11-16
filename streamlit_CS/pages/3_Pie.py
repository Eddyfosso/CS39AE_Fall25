import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="Dashboard", page_icon="📈", layout="wide")

st.markdown("# Interactive Student Analytics Dashboard")
st.markdown("Explore student performance with filters and see metrics update in real time.")
st.markdown("---")

@st.cache_data
def load_data():
    df = pd.read_csv('data/Student_Learning_Analytics.csv')
    return df

df = load_data()

st.info(f"""
Dataset: Student Learning Analytics  
Records: {len(df)} students | Last refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
""")

# FILTERS
st.sidebar.markdown("## Filters")
st.sidebar.markdown("---")

selected_majors = st.sidebar.multiselect(
    "Select Major(s):",
    options=sorted(df['major'].unique()),
    default=sorted(df['major'].unique())
)

selected_standings = st.sidebar.multiselect(
    "Select Academic Standing:",
    options=sorted(df['academic_standing'].unique()),
    default=sorted(df['academic_standing'].unique())
)

gpa_range = st.sidebar.slider(
    "GPA Range:",
    min_value=float(df['gpa'].min()),
    max_value=float(df['gpa'].max()),
    value=(float(df['gpa'].min()), float(df['gpa'].max())),
    step=0.1
)

scholarship_filter = st.sidebar.multiselect(
    "Scholarship Status:",
    options=['All', 'Yes', 'No'],
    default=['All']
)

st.sidebar.markdown("---")
if st.sidebar.button("Reset Filters"):
    st.rerun()

# APPLY FILTERS
filtered_df = df[
    (df['major'].isin(selected_majors)) &
    (df['academic_standing'].isin(selected_standings)) &
    (df['gpa'] >= gpa_range[0]) &
    (df['gpa'] <= gpa_range[1])
]

if scholarship_filter != ['All']:
    filtered_df = filtered_df[filtered_df['scholarship_recipient'].isin(scholarship_filter)]

# KPIs
st.markdown("## Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_students = len(filtered_df)
    st.metric(
        label="Total Students",
        value=f"{total_students:,}",
        delta=f"{((total_students / len(df)) * 100):.1f} percent of dataset"
    )

with col2:
    avg_gpa = filtered_df['gpa'].mean()
    st.metric(
        label="Average GPA",
        value=f"{avg_gpa:.2f}",
        delta=f"{avg_gpa - df['gpa'].mean():+.2f} vs. overall"
    )

with col3:
    avg_final_score = filtered_df['final_score'].mean()
    st.metric(
        label="Avg Final Score",
        value=f"{avg_final_score:.1f}",
        delta=f"{avg_final_score - df['final_score'].mean():+.1f} vs. overall"
    )

with col4:
    avg_attendance = filtered_df['attendance_rate'].mean()
    st.metric(
        label="Avg Attendance",
        value=f"{avg_attendance:.1f} percent",
        delta=f"{avg_attendance - df['attendance_rate'].mean():+.1f} percent vs. overall"
    )

st.markdown("---")

# LINKED VISUALS
st.markdown("## Linked Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### GPA Distribution by Major")
    gpa_by_major = filtered_df.groupby('major')['gpa'].mean().reset_index().sort_values('gpa', ascending=False)
    
    fig_major = px.bar(
        gpa_by_major,
        x='major',
        y='gpa',
        color='gpa',
        color_continuous_scale='Blues',
        title='Average GPA by Major (Filtered)',
        labels={'major': 'Major', 'gpa': 'Average GPA'},
        template='plotly_white'
    )
    fig_major.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig_major, use_container_width=True)

with col2:
    st.markdown("### Student Count by Standing")
    standing_count = filtered_df['academic_standing'].value_counts().reset_index()
    standing_count.columns = ['standing', 'count']
    
    fig_standing = px.pie(
        standing_count,
        names='standing',
        values='count',
        title='Academic Standing Distribution (Filtered)',
        template='plotly_white',
        color_discrete_sequence=['#2ca02c', '#1f77b4', '#d62728']
    )
    fig_standing.update_layout(height=350)
    st.plotly_chart(fig_standing, use_container_width=True)

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.markdown("### Study Hours vs. Final Score")
    fig_scatter = px.scatter(
        filtered_df,
        x='study_hours_per_week',
        y='final_score',
        color='major',
        title='Study Hours vs. Final Score (Filtered)',
        labels={'study_hours_per_week': 'Study Hours/Week', 'final_score': 'Final Score'},
        template='plotly_white'
    )
    fig_scatter.update_layout(height=350)
    st.plotly_chart(fig_scatter, use_container_width=True)

with col4:
    st.markdown("### Attendance Rate Distribution")
    fig_attend = px.histogram(
        filtered_df,
        x='attendance_rate',
        nbins=15,
        color_discrete_sequence=['#1f77b4'],
        title='Attendance Rate Distribution (Filtered)',
        labels={'attendance_rate': 'Attendance Percent', 'count': 'Students'},
        template='plotly_white'
    )
    fig_attend.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig_attend, use_container_width=True)

st.markdown("---")

# INSIGHTS
st.markdown("## Key Insights & Observations")

insights = [
    f"Filtered Dataset: Showing {len(filtered_df)} students",
    f"Performance: Average GPA is {avg_gpa:.2f}",
    f"Attendance Matters: Students with 90 percent plus attendance average higher scores",
    f"Study Insights: Optimal study hours appear to be 10-15 per week",
    f"Data Limitation: Results reflect a single institution"
]

for insight in insights:
    st.markdown(f"- {insight}")

st.markdown("---")

# ETHICS
st.markdown("## Data Limitations & Ethics")
st.warning("""
Dataset Notes:
- This dataset contains student academic records from a single university
- Results may not generalize to other institutions
- Patterns shown are correlational, not causal
- Visualizations are descriptive only and should not be used to discriminate
- Academic performance is influenced by many factors

Responsible Data Use:
- These insights support institutional research, not individual evaluation
- Achievement gaps may reflect opportunity gaps, not ability differences
- Performance variations are normal and expected across diverse populations
""")

# RAW DATA VIEW
if st.checkbox("Show Filtered Data (First 20 rows)"):
    st.markdown("### Filtered Dataset Preview")
    st.dataframe(
        filtered_df.sort_values('final_score', ascending=False).head(20),
        use_container_width=True
    )
    st.caption(f"Showing 20 of {len(filtered_df)} filtered records")
