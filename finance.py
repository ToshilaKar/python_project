import pandas as pd
import streamlit as st
from pathlib import Path
from streamlit.runtime.scriptrunner_utils.script_run_context import get_script_run_ctx

CSV_PATH = Path(r"C:\Users\LUCKY\OneDrive\Desktop\finance_data\finance_data.csv")


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        st.error(f"CSV file not found: {path}")
        st.stop()

    df = pd.read_csv(path)
    required_columns = {"Date", "Category", "Type", "Amount"}
    missing_columns = required_columns.difference(df.columns)

    if missing_columns:
        st.error(f"Missing required columns: {', '.join(sorted(missing_columns))}")
        st.stop()

    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df = df.dropna(subset=["Date", "Amount"])
    return df


def main() -> None:
    st.set_page_config(
        page_title="Personal Finance Dashboard",
        page_icon="💰",
        layout="wide",
    )

    st.markdown(
        """
        <style>
        .main {
            background-color: #F5F7FA;
        }
        h1,h2,h3 {
            color: #1E3A8A;
        }
        div[data-testid="metric-container"] {
            background: #FFFFFF;
            border: 2px solid #E5E7EB;
            padding: 18px;
            border-radius: 15px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.08);
        }
        section[data-testid="stSidebar"] {
            background: #1E293B;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------
    # LOAD DATA
    # -----------------------------
    df = load_data(CSV_PATH)

    # -----------------------------
    # SIDEBAR
    # -----------------------------
    st.sidebar.title("📂 Filters")

    categories = sorted(df["Category"].dropna().astype(str).unique())
    transaction_types = sorted(df["Type"].dropna().astype(str).unique())

    selected_categories = st.sidebar.multiselect(
        "Select Category",
        categories,
        default=categories,
    )

    selected_types = st.sidebar.multiselect(
        "Transaction Type",
        transaction_types,
        default=transaction_types,
    )

    filtered = df[
        df["Category"].astype(str).isin(selected_categories)
        & df["Type"].astype(str).isin(selected_types)
    ].copy()

    # -----------------------------
    # CALCULATIONS
    # -----------------------------
    income = float(filtered.loc[filtered["Type"].astype(str) == "Income", "Amount"].sum())
    expense = float(filtered.loc[filtered["Type"].astype(str) == "Expense", "Amount"].sum())
    savings = income - expense

    # -----------------------------
    # TITLE
    # -----------------------------
    st.title("💰 Personal Finance Tracker Dashboard")
    st.write("Track expenses, visualize spending, and predict monthly savings.")

    # -----------------------------
    # METRICS
    # -----------------------------
    c1, c2, c3 = st.columns(3)

    c1.metric("💵 Total Income", f"₹{income:,.0f}")
    c2.metric("💸 Total Expense", f"₹{expense:,.0f}")
    c3.metric("💰 Savings", f"₹{savings:,.0f}")

    st.divider()

    # -----------------------------
    # CHARTS
    # -----------------------------
    left, right = st.columns(2)

    expense_df = filtered[filtered["Type"].astype(str) == "Expense"].copy()

    with left:
        st.subheader("🥧 Expense by Category")
        if not expense_df.empty:
            category_summary = (
                expense_df.groupby("Category", as_index=False)["Amount"].sum()
                .sort_values("Amount", ascending=False)
            )
            st.bar_chart(category_summary.set_index("Category")["Amount"])

    with right:
        st.subheader("📈 Daily Expense Trend")
        if not expense_df.empty:
            daily_summary = (
                expense_df.groupby("Date", as_index=False)["Amount"].sum()
                .sort_values("Date")
            )
            st.line_chart(daily_summary.set_index("Date")["Amount"])

    st.divider()

    # -----------------------------
    # BAR CHART
    # -----------------------------
    st.subheader("📊 Income vs Expense")
    summary = (
        filtered.groupby("Type", as_index=False)["Amount"].sum()
        .sort_values("Amount", ascending=False)
    )
    st.bar_chart(summary.set_index("Type")["Amount"])

    st.divider()

    # -----------------------------
    # TRANSACTION TABLE
    # -----------------------------
    st.subheader("📋 Recent Transactions")
    st.dataframe(
        filtered.sort_values("Date", ascending=False),
        use_container_width=True,
    )

    st.divider()

    # -----------------------------
    # SAVINGS GOAL
    # -----------------------------
    goal = 50000
    progress = min(savings / goal, 1.0) if goal else 0.0

    st.subheader("🎯 Savings Goal")
    st.progress(progress)
    st.write(f"₹{savings:,.0f} / ₹{goal:,.0f}")

    st.divider()

    # -----------------------------
    # PREDICTION
    # -----------------------------
    st.subheader("📈 Monthly Prediction")

    days = int(filtered["Date"].dt.day.max()) if not filtered.empty else 0

    if days > 0:
        avg = expense / days
        predicted_expense = avg * 30
        predicted_savings = income - predicted_expense

        a, b, c = st.columns(3)
        a.success(f"Average Daily Expense\n\n₹{avg:.2f}")
        b.info(f"Predicted Monthly Expense\n\n₹{predicted_expense:.2f}")
        c.warning(f"Estimated Savings\n\n₹{predicted_savings:.2f}")

    st.divider()
    st.caption("Developed using Python • Pandas • Streamlit")


if __name__ == "__main__":
    if get_script_run_ctx() is None:
        print("Run this dashboard with: streamlit run finance.py")
    else:
        main()
