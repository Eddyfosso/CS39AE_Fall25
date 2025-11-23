import streamlit as st

st.title("🧭 Future Work & Reflection")

st.header("Next Steps")
st.markdown("""
- Add forecasting module to predict academic outcomes
- Integrate A/B dashboard layouts with feedback collection
- Accessibility audit: Additional tests for font sizes, keyboard navigation
- Enrich dataset with external indicators (e.g., financial aid, course difficulty)
- Explore instructor data and feedback analytics to complement student view
""")

st.header("Reflection on Design Evolution")
st.markdown("""
- Paper prototype included a flow-heavy layout; final app uses a clear sidebar and explicit page design for transparency.
- Early quiz insights drove addition of interactive chart filters and KPIs.
- Switched chart libraries based on usability testing in Labs 4.2 & 4.3—favoring color-safe, readable visuals.
- Finished product supports both casual exploration and deep analysis.
""")

st.header("Accessibility, UDL & Ethics")
st.markdown("""
- Colors and charts use color-blind-safe palettes; layout avoids excessive simultaneous colors.
- Images (profile, charts) include alt-text and descriptive titles.
- Axes, legends, and all metrics are clearly labeled.
""")
st.info("""
This dataset includes real people, so results must be interpreted carefully. Because the data come from a single university, it may contain sampling or selection bias and may not reflect all student experiences.
""")
