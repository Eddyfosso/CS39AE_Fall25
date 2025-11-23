import streamlit as st

st.title("👋 My Bio")

NAME = "Eddy Fosso"
PROGRAM = "CS39AE Data Visualization / Data Science and Machine Learning / Student"
INTRO = (
    "I am a student at Metropolitan State University of Denver. "
    "What excites me about data visualization and computing is the ability to turn raw data into actionable insights that solve real-world problems. "
    "I am passionate about transforming complex datasets into clear, actionable insights through thoughtful data visualization. "
    "With expertise in Python, Streamlit, and exploratory data analysis, I focus on creating accessible, ethical visualizations that tell compelling data stories."
)

FUN_FACTS = [
    "I love pancakes",
    "I'm learning Python",
    "I want to build websites",
]

PHOTO_PATH = "assets/f.jpg"

col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    st.image(PHOTO_PATH, caption=NAME, use_container_width=True)

with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun Facts")
for i, fact in enumerate(FUN_FACTS, start=1):
    st.write(f"- {fact}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
