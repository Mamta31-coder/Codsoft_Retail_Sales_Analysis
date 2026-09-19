import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../TASK_1_DATA_CLEANING/cleaned_retail_sales_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])
print("Dataset loaded successfully!")

os.makedirs("charts",exist_ok=True)

sns.set_theme(style="whitegrid")



# 1. REVENUE BY PRODUCT CATEGORY - BAR CHART

category_revenue = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

colors = ["#4C78A8", "#F58518", "#54A24B"]

bars = plt.bar(
    category_revenue.index,
    category_revenue.values,
    color=colors
)

plt.title(
    "Total Revenue by Product Category",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Product Category")
plt.ylabel("Total Revenue")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    "charts/01_revenue_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()



# 2. TRANSACTIONS BY PRODUCT CATEGORY - BAR CHART

category_count = df["Product Category"].value_counts()

plt.figure(figsize=(9, 6))

bars = plt.bar(
    category_count.index,
    category_count.values,
    color=["#4C78A8", "#F58518", "#54A24B"]
)

plt.title(
    "Number of Transactions by Product Category",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Product Category")
plt.ylabel("Number of Transactions")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    "charts/02_transactions_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# 3. REVENUE BY GENDER - BAR CHART

gender_revenue = (
    df.groupby("Gender")["Total Amount"]
    .sum()
)

plt.figure(figsize=(8, 6))

bars = plt.bar(
    gender_revenue.index,
    gender_revenue.values,
    color=["#E15759", "#4C78A8"]
)

plt.title(
    "Total Revenue by Gender",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Gender")
plt.ylabel("Total Revenue")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    "charts/03_revenue_by_gender.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# 4. REVENUE BY AGE GROUP - BAR CHART


df["Age Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65"]
)

age_revenue = (
    df.groupby("Age Group", observed=True)["Total Amount"]
    .sum()
)

plt.figure(figsize=(9, 6))

bars = plt.bar(
    age_revenue.index.astype(str),
    age_revenue.values,
    color="#72B7B2"
)

plt.title(
    "Total Revenue by Age Group",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Age Group")
plt.ylabel("Total Revenue")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    "charts/04_revenue_by_age_group.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()



# 5. REVENUE DISTRIBUTION - PIE CHART

plt.figure(figsize=(8, 8))

plt.pie(
    category_revenue.values,
    labels=category_revenue.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#4C78A8", "#F58518", "#54A24B"]
)

plt.title(
    "Revenue Distribution by Product Category",
    fontsize=15,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    "charts/05_revenue_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# 6. QUANTITY VS TOTAL AMOUNT - SCATTER PLOT

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df,
    x="Quantity",
    y="Total Amount",
    hue="Product Category",
    palette=["#4C78A8", "#F58518", "#54A24B"],
    s=70,
    alpha=0.7
)

plt.title(
    "Quantity vs Total Amount",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Quantity")
plt.ylabel("Total Amount")

plt.legend(title="Product Category")

plt.tight_layout()

plt.savefig(
    "charts/06_quantity_vs_total_amount.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()



# 7. AGE DISTRIBUTION - HISTOGRAM


plt.figure(figsize=(9, 6))

plt.hist(
    df["Age"],
    bins=12,
    color="#59A14F",
    edgecolor="black",
    alpha=0.85
)

plt.title(
    "Customer Age Distribution",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "charts/07_age_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# 8. MONTHLY REVENUE - LINE CHART

monthly_revenue = (
    df.set_index("Date")
    .resample("ME")["Total Amount"]
    .sum()
)

plt.figure(figsize=(11, 6))

plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o",
    linewidth=2.5,
    color="#4C78A8"
)

plt.title(
    "Monthly Revenue Trend",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Total Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "charts/08_monthly_revenue_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# 9. CATEGORY VS GENDER REVENUE

category_gender = (
    df.groupby(["Product Category", "Gender"])["Total Amount"]
    .sum()
    .unstack()
)

plt.figure(figsize=(10, 6))

category_gender.plot(
    kind="bar",
    figsize=(10, 6),
    color=["#4C78A8", "#E15759"]
)

plt.title(
    "Revenue by Product Category and Gender",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Product Category")
plt.ylabel("Total Revenue")

plt.xticks(rotation=0)

plt.legend(title="Gender")

plt.tight_layout()

plt.savefig(
    "charts/09_category_vs_gender_revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()



# 10. CORRELATION HEATMAP

numeric_columns = [
    "Age",
    "Quantity",
    "Price per Unit",
    "Total Amount"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues",
    fmt=".2f",
    linewidths=0.5
)

plt.title(
    "Correlation Heatmap",
    fontsize=15,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    "charts/10_correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()



# COMPLETION MESSAGE


print("\nAll visualizations created successfully!")

print("\nCharts saved in:")
print("TASK_3_DATA_VISUALIZATION/charts/")