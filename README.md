# 📊 Automated Multi-Source Data Pipeline & Power BI Dashboard

### 🚀 Overview

This project demonstrates a **complete data automation pipeline** that integrates multiple data sources (SQL, CSV/Excel, APIs, and web-scraped data) into a **centralized database** and visualizes insights via **Power BI dashboards**.

It simulates a real-world BI/Data Engineering workflow — from **data ingestion → cleaning → transformation → storage → visualization → automation**.

---

## 🔑 Features

✅ **Multi-Source Data Integration** – PostgreSQL, CSV/Excel, APIs, and web scraping
✅ **Python ETL Pipeline** – Data cleaning, transformation, and loading into PostgreSQL
✅ **Automated Data Refresh** – Scheduled weekly data generation via Python + Task Scheduler
✅ **Data Simulation** – Python-based data generator for continuous transaction data
✅ **Interactive Dashboards** – Revenue trends, customer demographics, product performance
✅ **Custom UI/UX** – Dashboard designed in **Figma** for a professional look

---

## 🛠️ Tech Stack

* **Languages:** Python, SQL
* **Database:** PostgreSQL
* **Libraries:** Pandas, SQLAlchemy, Requests, BeautifulSoup, Faker
* **Visualization:** Power BI, Excel
* **Automation:** Windows Task Scheduler (weekly jobs)
* **Design:** Figma

---

## 📊 Dashboards & KPIs

* **Total Revenue & ARPC (Average Revenue Per Customer)**
* **Revenue Trends (Monthly/Quarterly)**
* **Product Category Performance**
* **Customer Demographics (Age, Gender Segmentation)**
* **Quantity Sold & Average Purchase Value**

---

## ⚡ Automation Workflow

1. **Data Ingestion:** Fetch data from CSV, APIs, and web scraping.
2. **Data Cleaning & Transformation:** Python (Pandas) handles missing values, formatting, and normalization.
3. **Database Storage:** Load processed data into PostgreSQL.
4. **Data Simulation:** Generate new fake transaction data every Sunday (auto-scheduled).
5. **Visualization:** Power BI dashboard refreshes with latest data.

---

### 📈 Dashboard

* Open the `.pbix` file in **Power BI Desktop**
* Refresh to load the latest data

---

## 🎨 Dashboard Preview

<img width="1309" height="735" alt="image" src="https://github.com/user-attachments/assets/d2cc1b97-fdd7-49f5-a850-8d51366d21b4" />
<img width="1315" height="739" alt="image" src="https://github.com/user-attachments/assets/3f6b0a77-b65f-4d61-bea4-ad629f6da605" />
<img width="1309" height="735" alt="image" src="https://github.com/user-attachments/assets/7d615e5a-e729-44ce-a742-318afd7f953f" />
<img width="1315" height="734" alt="image" src="https://github.com/user-attachments/assets/74d25eab-244d-4636-a2b3-0bdc066b8150" />




---

## 📌 Future Improvements

* Deploy dashboards online (Power BI Service / Streamlit / Flask).
* Containerize ETL pipelines using Docker.
* Add CI/CD for automated testing and deployment.

---

## 👨‍💻 Author

**Ritam Jaiswal**

* 🎓 BCA Graduate | Aspiring Data Analyst
* 💡 Passionate about Data Analytics, Automation, and BI
* 🌐 [LinkedIn Profile](https://www.linkedin.com/in/ritam-jaiswal-06191933a/)

---
