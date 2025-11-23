import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

df = pd.read_csv('Student_Learning_Analytics.csv')

st.title("📊 EDA Gallery")

st.subheader("1. Distribution of Majors (Bar Chart)")
major_counts = df['major'].value_counts()
fig1 = px.bar(major_counts, x=major_counts.index, y=major_counts.values, labels={'y':'Count','x':'Major'}, color=major_counts.index, color_discrete_sequence=px.colors.qualitative.Safe)
st.plotly_chart(fig1, use_container_width=True)
st.markdown("**Question:** How are students distributed across majors?")
st.markdown("""
- X-axis: Academic majors; Y-axis: number of students
- Color: Unique for each major
- The chart shows how many students are enrolled in each major
""")
st.markdown("**Observation:** Engineering and Business are the largest cohorts. Mathematics, Data Science, Physics, and Computer Science are also well represented.")

st.subheader("2. GPA by Major (Box Plot, Interactive)")
fig2 = px.box(df, x='major', y='gpa', color='major', color_discrete_sequence=px.colors.qualitative.Safe)
st.plotly_chart(fig2, use_container_width=True)
st.markdown("**Question:** What does GPA distribution look like across majors?")
st.markdown("""
- X-axis: Major; Y-axis: GPA (0–4 scale)
- Boxes show the spread; lines indicate outliers
- Interactive: Hover for quartile breakdown per major
""")
st.markdown("**Observation:** Most majors have GPAs clustering in the 2.5–3.7 range with a few outliers. Physics and Computer Science show slightly more GPA variance.")

st.subheader("3. Satisfaction by Academic Standing (Violin Plot, Interactive)")
fig3 = px.violin(df, x='academic_standing', y='satisfaction_rating', box=True, points='all', color='academic_standing', color_discrete_sequence=px.colors.qualitative.Safe)
st.plotly_chart(fig3, use_container_width=True)
st.markdown("**Question:** How do students feel (satisfaction) in different standing?")
st.markdown("""
- X-axis: Academic Standing (Good, Dean's List, Probation)
- Y-axis: Satisfaction, scale 1–5
- Shapes: Distribution, box overlays
- Interactive: Hover for stats, click for sample points
""")
st.markdown("**Observation:** Students on Dean's List tend to report higher satisfaction. Probation students cluster in lower satisfaction groups.")

st.subheader("4. Study Hours vs. GPA (Scatter Plot with Filters, Interactive)")
min_hours = int(df['study_hours_per_week'].min())
max_hours = int(df['study_hours_per_week'].max())
study_range = st.slider("Filter: Study Hours per Week", min_hours, max_hours, (min_hours,max_hours))
filtered = df[(df['study_hours_per_week'] >= study_range[0]) & (df['study_hours_per_week'] <= study_range[1])]

fig4 = px.scatter(filtered, x='study_hours_per_week', y='gpa', color='major', hover_data=['age', 'campus_location'], color_discrete_sequence=px.colors.qualitative.Safe)
st.plotly_chart(fig4, use_container_width=True)
st.markdown("**Question:** Is there a relationship between hours studied and GPA?")
st.markdown("""
- X-axis: Weekly study hours; Y-axis: GPA
- Color: Major
- Interactive filter: Change the hour window to see trends in different populations
""")
st.markdown("**Observation:** Positive trend—students who study more generally show higher GPAs. Some outliers achieve high GPA at low study hours.")

st.caption("Data source: Student_Learning_Analytics.csv (See repo)")

