# Student Learning Analytics Portfolio

A Streamlit web application showcasing exploratory data analysis and interactive dashboards for student learning metrics. Built with Python, Pandas, Plotly, and Streamlit.

**Live App:** [https://cs39aefall25-rwssrrkr62r6cz2cw7jnju.streamlit.app/](https://cs39aefall25-rwssrrkr62r6cz2cw7jnju.streamlit.app/)

---

## 👤 Author

**Eddy Fosso**
- 📧 Email: [efossori@msudenver.edu](mailto:efossori@msudenver.edu)
- 💼 LinkedIn: [linkedin.com/in/eddy-dorian-fosso-djeudon-522932305](https://www.linkedin.com/in/eddy-dorian-fosso-djeudon-522932305)
- 🐙 GitHub: [github.com/Eddyfosso](https://github.com/Eddyfosso)

---

## 📊 Dataset

- **Name:** Student Learning Analytics
- **Records:** 351 students
- **Features:** 12 columns (GPA, major, attendance, exam scores, etc.)
- **Source:** Academic performance dataset from single institution

---

## 🗂️ App Navigation

Navigate using the sidebar to explore:

1. **Home** - Portfolio overview and key metrics
2. **Bio** - Professional background and visualization philosophy
3. **EDA Gallery** - 4 interactive exploratory charts:
   - Average GPA by Major (Bar Chart)
   - GPA Distribution (Histogram)
   - Study Hours vs. Final Score (Scatter Plot)
   - Final Score by Academic Standing (Box Plot)
4. **Dashboard** - Interactive filtered analytics with KPIs:
   - Real-time filters (major, standing, GPA range, scholarship)
   - Dynamic metrics and linked visualizations
   - Raw data preview
5. **Future Work** - Next steps, lessons learned, and resources

---

## ⚙️ Requirements
```
streamlit==1.31.1
pandas==2.2.1
plotly==5.18.0
numpy==1.26.4
```

---

## 🚀 How to Run Locally

### Step 1: Clone the repository
```bash
git clone https://github.com/Eddyfosso/CS39AE_Fall25.git
cd CS39AE_Fall25
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the app
```bash
streamlit run streamlit_CS/app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🌐 Run on Streamlit Cloud

The app is already deployed! Visit: [cs39aefall25-rwssrrkr62r6cz2cw7jnju.streamlit.app](https://cs39aefall25-rwssrrkr62r6cz2cw7jnju.streamlit.app/)

---

## 📁 Project Structure
```
CS39AE_Fall25/
├── streamlit_CS/
│   ├── app.py                           # Home page
│   ├── data/
│   │   └── Student_Learning_Analytics.csv
│   ├── pages/
│   │   ├── 1_Bio.py
│   │   ├── 2_Visualization.py          # EDA Gallery
│   │   ├── 3_Pie.py                    # Dashboard
│   │   └── 4_Future_Work.py
│   └── assets/
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

- **Python 3.13**
- **Streamlit** - Web app framework
- **Pandas** - Data manipulation
- **Plotly** - Interactive visualizations
- **NumPy** - Numerical computing
- **GitHub** - Version control & deployment
- **Streamlit Cloud** - Hosting

---

## ⚠️ Ethics & Data Limitations

This dataset contains student academic records from a **single institution**. Important notes:

- **Generalizability:** Results may not generalize to other universities or diverse student populations
- **Causality:** Patterns shown are correlational, not causal
- **Use Cases:** Visualizations are for institutional research only, NOT individual evaluation
- **Equity:** Achievement gaps may reflect opportunity gaps, not ability differences
- **Responsible Use:** Performance variations are normal and expected across diverse populations

---

## 📈 Key Features

✅ **Interactive Filters** - Filter by major, academic standing, GPA range, scholarship status  
✅ **Real-Time Metrics** - KPIs update dynamically based on filters  
✅ **Hover Details** - Plotly charts show data on hover  
✅ **Responsive Design** - Works on desktop and mobile  
✅ **Ethics-Focused** - Data limitations and responsible use guidelines included  

---

## 🎯 Key Insights from Data

1. Physics majors have highest average GPA (3.41), Business lowest (3.10)
2. Attendance rate is stronger predictor than study hours
3. Dean's List students show tight score distribution, Probation students show high variability
4. Optimal study hours appear to be 10-15 per week
5. 351 unique student records with diverse academic backgrounds

---

## 📝 License

This project is part of a Data Visualization course assignment.

---

## 💬 Questions or Feedback?

Feel free to reach out:
- 📧 Email: efossori@msudenver.edu
- 🔗 LinkedIn: [linkedin.com/in/eddy-dorian-fosso-djeudon-522932305](https://www.linkedin.com/in/eddy-dorian-fosso-djeudon-522932305)

---

**Last Updated:** November 2024
