import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Eddy Fosso"
PROGRAM = " CS39AE/ Data Science and Machine Learning"
INTRO = (
    "I'm a student at Metropolitant State University of Denver", 
    "What excites me about data science is the ability to turn raw data into actionable insights that solve real-world problems", 
    
)
FUN_FACTS = [
    "I love pancakes",
    "I’m learning python",
    "I want to build website",
]
PHOTO_PATH = "https://1drv.ms/i/c/0c977a7ae1d9e64f/EU_m2eF6epcggAxXAQAAAAAB8CLIH8HCTTTFTBn66nvQkA?e=18nGkA"  # Put a file in repo root or set a URL


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
