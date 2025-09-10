# SpaceX Falcon 9 Launch Analysis Portfolio

This repository is an **extended and enhanced version** of the Coursera **IBM Applied Data Science Capstone Project**, focusing on SpaceX Falcon 9 launch data. It demonstrates an **end-to-end data science workflow**, including data wrangling, SQL and visual EDA, interactive geospatial mapping, predictive modeling, and deployment-ready dashboards.

---

## 📁 Repository Structure

SpaceX_Falcon9_Portfolio/
│
├── data/
│ ├── dataset_1.csv # Generated from data wrangling notebook
│ ├── dataset_2.csv # Cleaned version of dataset_1
│ └── dataset_3.csv # Feature-selected dataset for modeling
│
├── notebooks/
│ ├── 1_Data_Wrangling.ipynb
│ ├── 2_SQL_EDA.ipynb
│ ├── 3_Visual_EDA.ipynb
│ ├── 4_Interactive_Folium.ipynb
│ └── 5_Predictive_Modeling.ipynb
│
├── models/
│ └── spacex_logreg_model.pkl # Saved Logistic Regression model
│
├── dashboards/
│ └── SpaceX_Dash_App/ # Plotly Dash app folder
│
├── README.md
└── requirements.txt


---

## 📖 Project Background

This project started as the **IBM Applied Data Science Capstone** on Coursera, which uses SpaceX Falcon 9 launch data to explore landing success.  

I extended the project by:  
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
