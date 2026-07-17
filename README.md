# python_project
basic python project
# Personal Finance Tracker Dashboard – README

````markdown
# 💰 Personal Finance Tracker Dashboard

A **Personal Finance Tracker Dashboard** built using **Python, Pandas, and Streamlit**. This application helps users manage their finances by tracking income and expenses, analyzing spending patterns, monitoring savings, and predicting monthly expenses.

---

## 📌 Features

- 📂 Filter transactions by **Category** and **Transaction Type**
- 💵 Display Total Income
- 💸 Display Total Expenses
- 💰 Calculate Total Savings
- 📊 Expense analysis by category
- 📈 Daily expense trend visualization
- 📋 View all transactions in a responsive table
- 🎯 Savings goal progress tracker
- 🔮 Monthly expense and savings prediction
- 🎨 Clean and interactive Streamlit interface

---

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- Pandas

---

## 📂 Project Structure

```
Finance_Dashboard/
│
├── finance.py              # Main Streamlit application
├── finance_data.csv        # Dataset
├── README.md               # Project documentation
└── requirements.txt        # Required libraries
```

---

## 📁 Dataset Format

The CSV file should contain the following columns:

| Column | Description |
|----------|-------------|
| Date | Transaction Date |
| Category | Expense/Income Category |
| Type | Income or Expense |
| Amount | Transaction Amount |

### Example

| Date | Category | Type | Amount |
|------|----------|---------|--------|
|2026-07-01|Salary|Income|50000|
|2026-07-02|Food|Expense|500|
|2026-07-03|Shopping|Expense|1500|
|2026-07-04|Freelancing|Income|7000|

---



Displays:

- Total Income
- Total Expense
- Total Savings

---

### 📊 Expense by Category

Visualizes expenses using a bar chart grouped by category.

---

### 📈 Daily Expense Trend

Shows daily spending patterns using a line chart.

---

### 📊 Income vs Expense

Compares total income and total expenses using a bar chart.

---

### 📋 Transaction History

Displays all filtered transactions in a searchable table.

---

### 🎯 Savings Goal

Tracks progress toward a predefined savings target.

Default Goal:

```
₹50,000
```

---

### 🔮 Monthly Prediction

Calculates:

- Average Daily Expense
- Predicted Monthly Expense
- Estimated Monthly Savings

---

## 🎨 User Interface

- Responsive layout
- Sidebar filters
- Metric cards
- Interactive charts
- Progress bar
- Clean color theme

---

## 📦 Required Libraries

```
streamlit
pandas
```

Install manually:

```bash
pip install streamlit pandas
```

---

## 📈 Future Improvements

- Login Authentication
- Expense Editing & Deletion
- Export Reports to PDF
- Monthly & Yearly Analytics
- Budget Alerts
- Pie Charts
- AI-Based Spending Insights
- Database Integration (SQLite/MySQL)
- Cloud Deployment
- Mobile Responsive Dashboard

---

## 👨‍💻 Author

**Toshila Kar**

B.Tech (Computer Science & Engineering)

Centurion University of Technology and Management (CUTM), Bhubaneswar

---

## 📄 License

This project is developed for educational and learning purposes.

Free to use and modify.

---

## ⭐ Project Highlights

✔ Interactive Dashboard

✔ Expense Tracking

✔ Income Monitoring

✔ Savings Calculation

✔ Monthly Prediction

✔ Goal Tracking

✔ Data Filtering

✔ Streamlit Web Application

✔ Pandas Data Analysis

✔ Clean UI Design
````
