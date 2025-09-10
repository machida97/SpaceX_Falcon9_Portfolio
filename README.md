# SpaceX Falcon 9 Launch Analysis Portfolio

This repository is a **portfolio project** showcasing end-to-end data science skills, using SpaceX Falcon 9 launch data. It builds on the **Coursera IBM Applied Data Science Capstone**, extending the work with additional data, EDA, visualizations, interactive maps, and predictive modeling.  

The project demonstrates:

- Data wrangling and cleaning
- SQL-based exploratory data analysis
- Visual EDA with matplotlib and seaborn
- Interactive geospatial analytics with Folium
- Predictive modeling for booster landing success
- Deployment of a Plotly Dash interactive dashboard

---

## 📁 Repository Structure


```text
SpaceX_Falcon9_Portfolio/
│
├── datasets/
│ ├── dataset_part_1.csv # Generated from data collection & wrangling
│ ├── dataset_part_2.csv # Cleaned dataset
│ └── dataset_part_3.csv # Feature-selected dataset for modeling
│
├── notebooks/
│ ├── 1_SpaceX_Falcon9_Data_Collection_and_Enrichment.ipynb
│ ├── 2_SpaceX_Falcon_9_Data_Wrangling_and_Preparation.ipynb
│ ├── 3_SpaceX_Falcon_9_SQL_EDA.ipynb
│ ├── 4_Spacex_Falcon_9_Visualisation_EDA.ipynb
│ ├── 5_SpaceX_Falcon_9_Interactive_Visual_Analytics_with_Folium.ipynb
│ └── 6_SpaceX_Predictive_Analysis_(Classification).ipynb
│
├── models/
│ └── spacex_logreg_model.pkl # Saved Logistic Regression model
│
├── dash_app/
│ ├── Procfile
│ ├── Readme.rtf
│ ├── app.py
│ ├── requirements.txt
│ └── spacex_launch_dash.csv # Dataset for the Dash app
│
├── README.md
└── requirements.txt
```
---

## 📖 Project Background

This project started as the **IBM Applied Data Science Capstone** on Coursera, which uses SpaceX Falcon 9 launch data to explore landing success.  

I extended the project by:  
- Using addtional weather data
- Performing additional **SQL-based exploratory data analysis**  
- Adding additional **interactive geospatial and weather visualizations** with Folium  
- Creating a **full predictive modeling pipeline** with multiple classification algorithms  
- Conducting **feature importance analysis and model interpretability studies**  
- Deploying a **Plotly Dash interactive dashboard** with additional features hosted online  

---

## 🛠 Skills & Learning Outcomes

- End-to-end data science pipeline: **Data Collection → Wrangling → EDA → Modeling → Deployment**  
- SQL querying and database management  
- Data visualization with **Matplotlib, Seaborn, Folium, Plotly Dash**  
- Machine learning with **Scikit-Learn**  
- Model evaluation, feature importance, and interpretability  

> Builds on the IBM Applied Data Science Capstone by extending the analysis and adding advanced features and interactive tools.

---

## 📊 Highlights

1. **Data Wrangling & Cleaning:** Generating clean datasets ready for analysis.  
2. **SQL EDA:** Landing outcomes, success rates, and feature interactions explored in SQL.  
3. **Visual EDA:** Insights via Matplotlib and Seaborn plots, examining payloads, orbits, and weather effects.  
4. **Interactive Mapping:** Folium-based geospatial visualizations of launch sites, proximity to landmarks, and weather overlays.  
5. **Predictive Modeling:** Logistic Regression, Random Forest, SVM, Decision Tree, KNN, Neural Networks, and Naive Bayes applied to predict landing success.  
6. **Dashboard Deployment:** Interactive Plotly Dash app for exploring launch outcomes and features online.  

---

## 🔗 Deployment

- **Plotly Dash App:** [Hosted on Render](YOUR_DASH_APP_URL_HERE)  
- **Saved Model:** `models/spacex_logreg_model.pkl` for predictive inference  

---

## 📌 References

- Original Capstone Reference: [IBM Applied Data Science Capstone](https://www.coursera.org/learn/applied-data-science-capstone)  
- SpaceX Open Data: [SpaceX API](https://github.com/r-spacex/SpaceX-API)  

---

## 💡 Notes

- The repository is **self-contained**; all data and models required to run the notebooks and dashboard are included.  
- The project demonstrates **how to go from raw data to interactive dashboards and predictive modeling**, suitable for portfolio presentation.
