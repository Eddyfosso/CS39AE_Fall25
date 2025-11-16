import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Student Analytics Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #555;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown('<p class="main-header">📊 Student Analytics Portfolio</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Data Visualization & Educational Analytics</p>', unsafe_allow_html=True)

with col2:
    st.image("https://via.placeholder.com/150", use_column_width=True, caption="Eddy Fosso")

st.markdown("""
## Welcome 👋

This portfolio showcases my work in **data visualization** and **educational analytics**. 
Navigate using the sidebar to explore:

- **📄 Bio** — My professional background and visualization philosophy
- **📊 EDA Gallery** — Exploratory analysis with 4 interactive charts
- **📈 Dashboard** — Filtered analytics dashboard with KPIs
- **🧭 Future Work** — Next steps and project reflections
""")

st.markdown("### 🎯 Key Highlights")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Charts", "4+")
with col2:
    st.metric("Students Analyzed", "351")
with col3:
    st.metric("Interactive Elements", "5+")

st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #888; font-size: 0.9rem;">
    <p>Last updated: {datetime.now().strftime('%B %d, %Y')}</p>
    <p><a href="https://www.linkedin.com/in/eddy-dorian-fosso-djeudon-522932305">LinkedIn</a> | 
    <a href="mailto:efossori@msudenver.edu">Email</a> | 
    <a href="https://github.com/Eddyfosso">GitHub</a></p>
</div>
""", unsafe_allow_html=True)
```

### **Step 7.3: Commit**
Type:
```
Update home page with personal info
```
Click **"Commit directly to main"**

✅ **Home page updated!**

---

## **STEP 8: Update requirements.txt**

### **Step 8.1: Edit File**
Go to `streamlit_CS` folder
Click on **`requirements.txt`**
Click the **pencil icon**

### **Step 8.2: Replace Content**
Delete everything and paste:
```
streamlit==1.28.1
pandas==2.0.3
plotly==5.17.0
numpy==1.24.3
```

### **Step 8.3: Commit**
Type:
```
Update dependencies
```
Click **"Commit directly to main"**

✅ **All files added!**

---

## ✅ FINAL CHECKLIST

After all 8 steps, your GitHub should look like:
```
✅ README.md
✅ app.py (updated)
✅ requirements.txt (updated)
✅ pages/
   ✅ 1_📄_Bio.py
   ✅ 2_📊_Charts_Gallery.py
   ✅ 3_📈_Dashboard.py
   ✅ 4_🧭_Future_Work.py
✅ data/
   ✅ Student_Learning_Analytics.csv
