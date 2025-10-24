import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Eddy Fosso"
PROGRAM = "CS39AE/ Data Science and Machine Learning / Student"
INTRO = (
    "I'm a student at Metropolitant State University of Denver, "
    "What excites me about data computing is the ability to turn raw data into actionable insights that solve real-world problems."
)
FUN_FACTS = [
    "I love pancakes",
    "I’m learning python",
    "I want to build website",
]
PHOTO_PATH = ""C:/Users/Eddy/OneDrive/Pictures/f.jpg""  # Put a file in repo root or set a URL

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info(""C:/Users/Eddy/OneDrive/Pictures/f.jpg" to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(Eddy Fosso)
    st.write(Data Visualization)
    st.write("I'm a student at Metropolitant State University of Denver, 
    What excites me about data computing is the ability to turn raw data into actionable insights that solve real-world problems."
)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write("I love pancakes",
    "I’m learning python",
    "I want to build website",)

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
