import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Eddy Fosso"
PROGRAM = "Data Visualization / Major: Data Science and Machine Learning"
INTRO = ( I am a passionate student pursuing my degree in Data Science at Metropolitan State University of Denver. I have a strong interest in data science, machine learning, and web development.I enjoy building interactive applications and solving real-world problems with code.
    
)
FUN_FACTS = [
    "I love pancakes",
    "I’m learning python",
    "I want to build dynamic website",
]
PHOTO_PATH = """f.jpg"""  # Put a file in repo root or set a URL

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
