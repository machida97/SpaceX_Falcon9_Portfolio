# SpaceX Launch Dashboard

An **interactive dashboard** built with **Plotly Dash** to visualize SpaceX launch records and explore launch trends beyond the Coursera IBM Applied Data Science Capstone.

This dashboard allows users to filter and analyze SpaceX launches by site, payload, and booster type, and provides visual insights into launch success rates.

---

## Features

- **Multi-select Launch Sites** – compare multiple launch sites simultaneously.  
- **Booster Version Category Filter** – focus on specific booster types.  
- **Success/Failure Pie Charts** – dynamically updates with launch site and booster filters.  
- **Payload Range Slider** – filter launches by payload mass.  
- **Scatter Plot** – correlation between payload and launch success, with hover info including Flight Number and Booster Version.  
- **Success Rate Over Time** – line chart showing success trends across flights.  
- **Summary Statistics Panel** – shows total launches, successes, and success rate for selected filters.  

---

## Live Deployment

This app is deployed on **Render**:

[https://spacex-dash-dashboard.onrender.com/](https://spacex-dash-dashboard.onrender.com/)

---

## Dataset

The dataset (`spacex_launch_dash.csv`) was provided as part of the IBM Data Science Capstone. It includes launch records from multiple boosters (not only Falcon 9). The purpose of this project is to demonstrate building and deploying an **interactive dashboard**, not dataset wrangling.

**Columns:**

- `Flight Number`  
- `Launch Site`  
- `class` (0 = failed, 1 = success)  
- `Payload Mass (kg)`  
- `Booster Version`  
- `Booster Version Category`  

---

## Files

- `app.py` – main Dash app code  
- `spacex_launch_dash.csv` – SpaceX launch data  
- `requirements.txt` – Python dependencies  
- `Procfile` – for deployment on Render 
