# 📊 Egypt Data Science Job Market Analysis (Wuzzuf Scraper & Dashboard)

An end-to-end Data Science project that scrapes, cleans, analyzes, and visualizes the labor market for **Data Science** roles in Egypt using data extracted from **Wuzzuf.net**.

---

## 📌 Project Overview
Finding data-driven insights about the local tech job market can be challenging. This project automates the extraction of job listings in Egypt, processes unstructured requirements, extracts numerical experience levels, cleans geographical distributions, and provides an interactive **Streamlit Dashboard** for exploration.

---

## 🛠️ Tech Stack & Tools
* **Web Scraping:** Python, `undetected-chromedriver` (Cloudflare bypass), `BeautifulSoup4`
* **Data Cleaning & Manipulation:** `Pandas`, `Regex`
* **Data Visualization:** `Matplotlib`, `Seaborn`
* **Interactive Web App:** `Streamlit`

---

## 🔑 Key Market Insights
* **Geographic Centralization:** Over 85% of Data Science opportunities are concentrated in **Cairo and Giza**.
* **Top Demanded Skills:** **SQL** and **Python** are the most requested technical skills across job descriptions, followed by general **Software Engineering** and **Data Analysis** capabilities.
* **Experience Requirements:** Entry-level roles typically require less than 1 year of average experience, making the market accessible for fresh graduates with strong technical portfolios.

---

## 📁 Project Structure
```text
├── WUZZUF_SCRAPING.py     # Web scraping pipeline
├── Data_Cleaning.py       # Data parsing & regex logic
├── app.py                 # Streamlit interactive dashboard
├── Wuzzuf_Cleaned_Jobs.csv# Cleaned dataset
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation