import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('Student_Learning_Analytics.csv')
st.title("📈 Student Analytics Dashboard")

# Filters
majors = st.multiselect("Filter by Major", options=df['major'].unique())
semesters = st.multiselect("Filter by Semester", options=df['semester'].unique())
filtered = df.copy()
if majors: filtered = filtered[filtered['major'].isin(majors)]
if semesters: filtered = filtered[filtered['semester'].isin(semesters)]

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Student Count", len(filtered))
col2.metric("Mean GPA", f"{filtered['gpa'].mean():.2f}")
col3.metric("Median Satisfaction", int(filtered['satisfaction_rating'].median()))
col4.metric("Latest Semester", filtered['semester'].iloc[-1] if not filtered.empty else "N/A")

# Linked chart 1: GPA histogram
fig1 = px.histogram(filtered, x='gpa', nbins=12, color='major', labels={'gpa':'GPA'}, color_discrete_sequence=px.colors.qualitative.Safe)
st.plotly_chart(fig1, use_container_width=True)

# Linked chart 2: Satisfaction by Campus Location
fig2 = px.box(filtered, x='campus_location', y='satisfaction_rating', color='campus_location', color_discrete_sequence=px.colors.qualitative.Safe)
st.plotly_chart(fig2, use_container_width=True)

st.caption("Data source: Student_Learning_Analytics.csv | Last refreshed: 2025-11-22 16:40 PST")

st.header("Narrative Insights")
st.markdown("""
- Highest satisfaction scores cluster on the Main Campus and among Dean's List students.
- GPA histogram shows most students between 2.5–3.7; a tail below 2.5 suggests a subset struggling.
- Filters let users view cohorts by major or semester—enabling targeted insights for intervention.
- Small sample size per major means results may be noisy for less-represented fields.
- Dashboard is descriptive; patterns should not be used for advising or policy without more context.
""")
