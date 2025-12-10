# COVID-19 Data Visualization 📊🦠

This project provides a comprehensive analysis and visualization of COVID-19 data using Python. The dataset is sourced from [Kaggle](https://www.kaggle.com/) and contains global COVID-19 statistics including confirmed cases, deaths, recoveries, and active cases.

---

## 🔹 Dataset

- **Source:** Kaggle (`covid_19_clean_complete.csv`)
- **Columns include:**
  - `Date` – The date of the record
  - `Country/Region` – Country or region name
  - `Confirmed` – Total confirmed COVID-19 cases
  - `Deaths` – Total deaths
  - `Recovered` – Total recoveries
  - `Active` – Active cases
  - `WHO Region` – WHO regional classification
  - `Daily New Cases` – Daily new confirmed cases (if available)

---

## 🔹 Technologies Used

- Python 3.x
- Pandas
- Matplotlib

---

## 🔹 Visualizations

1. **Monthly Confirmed Cases** (Line Graph)  
   Shows the trend of total confirmed COVID-19 cases month by month globally.

2. **Daily New Case Distribution** (Histogram)  
   Visualizes the frequency distribution of daily new cases to identify peaks and patterns.

3. **Top 10 Countries by Total Confirmed Cases** (Bar Graph)  
   Highlights the countries with the highest number of confirmed cases.

4. **Confirmed vs Deaths** (Scatter Plot)  
   Shows the correlation between confirmed cases and deaths across all countries.

5. **Daily Active Cases Trend** (Line Graph)  
   Tracks the trend of active COVID-19 cases over time globally.

6. **WHO Region-wise Confirmed Cases** (Pie Chart)  
   Shows the proportion of confirmed cases in different WHO regions.

7. **Daily COVID-19 Deaths Trend** (Line Graph)  
   Illustrates the progression of daily deaths over time globally.

8. **Top 10 Countries by Recovered Cases** (Bar Graph)  
   Highlights countries with the highest number of recoveries.

---

## 🔹 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/covid19-visualization.git
2. Install the required libraries:
   ```bash
   pip install pandas matplotlib
3. Place the dataset covid_19_clean_complete.csv in the project folder.
4. Run the Python script:
  ```bash
   python covid_visualizations.py

