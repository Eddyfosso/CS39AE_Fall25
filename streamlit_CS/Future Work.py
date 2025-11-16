import streamlit as st

st.set_page_config(page_title="Future Work", page_icon="🧭", layout="wide")

st.markdown("# Future Work & Roadmap")
st.markdown("""
This page outlines potential enhancements and next steps for this portfolio project.
""")
st.markdown("---")

st.markdown("## Next Steps (Prioritized)")

future_works = [
    {
        "title": "1. Predictive Modeling for At-Risk Students",
        "description": "Build ML models to identify students at risk of academic probation early.",
        "impact": "High",
        "effort": "High",
        "timeline": "3-4 weeks"
    },
    {
        "title": "2. Time-Series Analysis of Semester Trends",
        "description": "Analyze how student performance changes throughout semester.",
        "impact": "High",
        "effort": "Medium",
        "timeline": "2-3 weeks"
    },
    {
        "title": "3. Accessibility Audit & Remediation",
        "description": "Test with screen readers and ensure WCAG 2.1 AA compliance.",
        "impact": "High",
        "effort": "Medium",
        "timeline": "1-2 weeks"
    },
    {
        "title": "4. Comparative Analysis: Benchmarks",
        "description": "Compare institutional performance against national averages.",
        "impact": "Medium",
        "effort": "High",
        "timeline": "3-4 weeks"
    },
    {
        "title": "5. Interactive Cohort Comparison",
        "description": "Allow users to build custom cohorts and compare performance.",
        "impact": "Medium",
        "effort": "High",
        "timeline": "2-3 weeks"
    },
]

for work in future_works:
    col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
    
    with col1:
        st.markdown(f"### {work['title']}")
        st.markdown(work['description'])
    
    with col3:
        impact_colors = {"High": "RED", "Medium": "YELLOW", "Low": "GREEN"}
        st.markdown(f"**Impact:** {work['impact']}")
        st.markdown(f"**Effort:** {work['effort']}")
    
    with col4:
        st.markdown(f"**Timeline:** {work['timeline']}")
    
    st.markdown("---")

st.markdown("## Reflection: From Prototype to Final Build")

st.markdown("""
**What Changed:**

1. **Interactivity** - Static prototype to fully dynamic app with cascading filters
2. **Charts** - 3 basic types expanded to 4+ specialized chart types
3. **Guidance** - Added plain-language "How to Read" guides for each chart
4. **Ethics** - Added ethics notes and data limitations sections
5. **Implementation** - Learned Plotly interactive capabilities and Streamlit caching
""")

st.markdown("---")

st.markdown("## Key Lessons Learned")

lessons = [
    "Iteration Matters - First design was cluttered, simplifying improved clarity",
    "User Testing - Feedback showed need for chart interpretation guides",
    "Performance - Caching reduced load time by 85 percent",
    "Accessibility - Color blindness testing revealed palette issues",
    "Data Quality - Spent 25 percent of time cleaning saved 60 percent debugging",
    "Storytelling - Framing matters for how insights resonate"
]

for i, lesson in enumerate(lessons, 1):
    st.markdown(f"{i}. {lesson}")

st.markdown("---")

st.markdown("## Resources")

st.markdown("""
**Visualization & Design**
- Storytelling with Data by Cole Nussbaumer Knaflic
- Edward Tufte Principles
- ColorBrewer2.0 for palette selection

**Accessibility & Ethics**
- WCAG 2.1 Guidelines
- Data Ethics Canvas
- Colorblind Simulator

**Tools & Documentation**
- Streamlit Docs
- Plotly Documentation
- Pandas User Guide
""")

st.markdown("---")

st.markdown("## Contact & Feedback")

st.info("""
Connect with me:
- Email: efossori@msudenver.edu
- LinkedIn: https://www.linkedin.com/in/eddy-dorian-fosso-djeudon-522932305
- GitHub: https://github.com/Eddyfosso

Made with Python, Pandas, Plotly, Streamlit, GitHub, and Streamlit Cloud
""")
