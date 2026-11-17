import pandas as pd


def financial_chatbot():
    try:
        df = pd.read_csv('processed_financial_data.csv')
    except FileNotFoundError:
        print("Error: 'processed_financial_data.csv' not found! Please run Task 1 notebook first.")
        return

    print("==========================================================")
    print("🤖 Welcome to the BCG Financial Analysis Chatbot!")
    print("==========================================================")
    print("Supported Companies: Microsoft, Apple, Tesla")
    print("Supported Fiscal Years: 2024, 2025, 2026")
    print("Supported Metrics: Total_Revenue, Net_Income, Total_Assets, Total_Liabilities, Cash_Flow_Operating")
    print("\nType your query in the format: <Company> <Year> <Metric>")
    print("Example: Microsoft 2025 Total_Revenue")
    print("Type 'exit' or 'quit' to close the chatbot.\n")

    while True:
        user_query = input("Your Query: ").strip()

        if user_query.lower() in ['exit', 'quit']:
            print("Thank you for using the BCG Financial Chatbot. Goodbye!")
            break

        parts = user_query.split()
        if len(parts) < 3:
            print(
                "⚠️ Invalid format. Please use: <Company> <Year> <Metric> (e.g., Apple 2026 Net_Income)\n")
            continue

        company_input = parts[0].capitalize()
        try:
            year_input = int(parts[1])
        except:
            print(
                "⚠️ Invalid year. Fiscal year must be a number (e.g., 2024, 2025, 2026).\n")
            continue

        metric_input = parts[2]

        result = df[(df['Company'].str.lower() == company_input.lower()) & (
            df["Fiscal_Year"] == year_input)]

        if result.empty:
            print(
                f"❌ No financial records found for '{company_input}' in fiscal year {year_input}.\n")
            continue

        if metric_input not in result.columns:
            print(f"❌ Metric '{metric_input}' is not recognized.")
            print("Available metrics: Total_Revenue, Net_Income, Total_Assets, Total_Liabilities, Cash_Flow_Operating\n")
            continue

        value = result[metric_input].values[0]

        print("\n----------------------------------------------------------")
        print(f"📊 Financial Report: {company_input} (FY {year_input})")
        print(f"• {metric_input.replace('_', ' ')}: ${value:,.2f} Million")

        growth_col = f"{metric_input}_Growth (%)"
        if growth_col in result.columns:
            growth_val = result[growth_col].values[0]
            if pd.notna(growth_val) and growth_val != 0:
                direction = "increase" if growth_val > 0 else "decrease"
                print(
                    f"• Year-over-Year (YoY) Change: {growth_val}% ({direction})")
            else:
                print("• Year-over-Year (YoY) Change: N/A (Base Year)")
        print("----------------------------------------------------------\n")


if __name__ == "__main__":
    financial_chatbot()
