import streamlit as st

NAME = "Eddy Fosso"
PROGRAM = "CS39AE Data Visualization / Data Science and Machine Learning / Student"
INTRO = (
    "I am a student at Metropolitan State University of Denver. "
    "What excites me about data visualization and computing is the ability to turn raw data into actionable insights that solve real-world problems. "
    "I am passionate about transforming complex datasets into clear, actionable insights through thoughtful data visualization. "
    "With expertise in Python, Streamlit, and exploratory data analysis, I focus on creating accessible, ethical visualizations that tell compelling data stories."
)
HIGHLIGHTS = [
    "Coursework: Data Visualization, Data Science, Machine Learning",
    "Tools: Python, Streamlit, Pandas, Plotly, Altair",
    "Passionate about accessibility, UDL, and ethical analysis",
]
FUN_FACTS = [
    "I love pancakes",
    "I'm learning Python",
    "I want to build websites",
]

PHOTO_URL = "f.jpg"

st.title("👋 My Bio")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.image(PHOTO_URL, caption=f"{NAME} — profile photo", use_container_width=True)

with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Highlights")
for item in HIGHLIGHTS:
    st.write(f"- {item}")

st.markdown("### Fun Facts")
for fact in FUN_FACTS:
    st.write(f"- {fact}")

st.markdown("### Visualization Philosophy")
st.write(
    "I believe every visualization should prioritize clarity, accessibility, and truthfulness. "
    "Visuals should empower users, be colorblind-friendly, and always include clear labeling to avoid misinterpretation or bias."
)

st.divider()
st.caption("Edit `pages/1_📄_Bio.py` to customize your bio page.")
