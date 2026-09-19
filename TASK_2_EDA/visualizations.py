import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")


df = pd.read_csv("../TASK_1_DATA_CLEANING/cleaned_retail_sales_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])
print("Dataset loaded successfully!")


os.makedirs("charts",exist_ok=True)


# 1. Revenue by Product Category

category_sales = df.groupby("Product Category")["Total Amount"].sum()
plt.figure(figsize=(8,5))
category_sales.sort_values(ascending = False).plot(kind="bar",color=["#4C78A8","#F58518","#54A24B"])
plt.title("Total Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation = 0)
plt.tight_layout()
plt.savefig("charts/01_revenue_by_category.png",
            dpi=300,
            bbox_inches="tight"
            )
plt.close()



# 2. Number of Transactions by Category

category_count = df["Product Category"].value_counts()
plt.figure(figsize=(8,5))
category_count.plot(kind ="bar",
                    color=["#4C78A8","#F58518","#54A24B"])
plt.title("Number of Transactions by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/02_transactions_by_category.png",
            dpi=300,
            bbox_inches="tight"
            )
plt.close()




# 3. Revenue by Gender

gender_sales = df.groupby("Gender")["Total Amount"].sum()
plt.figure(figsize=(7,5))
gender_sales.plot(kind= "bar",
                  color=["#4C78A8","#F58518"])
plt.title("Total Revenue by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/03_revenue_by_gender.png",
            dpi=300,
            bbox_inches="tight"
            )
plt.close()



# 4. Revenue by Age Group


df["Age Group"] = pd.cut(df["Age"],bins = [17,25,35,45,55,65],labels = ["18-25","26-35","36-45","46-55","56-65"])
age_sales = df.groupby("Age Group",observed = True)["Total Amount"].sum()
plt.figure(figsize=(9,5))
age_sales.plot(kind="bar",
               color = ["#54A24B","#E45756","#72B7B2","#B279A2","#FF9DA6"])
plt.title("Total Revenue by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/04_revenue_by_age_group.png",
            dpi=300,
            bbox_inches="tight"
            )
plt.close()




# 5. Quantity vs Total Amount

plt.figure(figsize=(8,5))
sns.scatterplot(data =df, x="Quantity",y="Total Amount", color =  "#4C78A8")
plt.title("Quantity vs Total Amount")
plt.xlabel("Quantity")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.savefig("charts/05_quantity_vs_total_amount.png",
            dpi=300,
            bbox_inches="tight"
            )
plt.close()



 

# 6. Category vs Gender Revenue

category_gender = df.groupby(["Product Category", "Gender"])["Total Amount"].sum().unstack()
category_gender.plot(kind="bar",figsize=(8,5), color= ["#4C78A8","#F58518"])
plt.title("Revenue by Product Category and Gender")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.legend(title="Gender")
plt.tight_layout()
plt.savefig("charts/06_category_vs_gender_revenue.png",
            dpi=300,
            bbox_inches="tight"
            )
plt.close()




print("\nAll 6 charts have been generated successfully!")
print("\nCharts are saved inside the 'charts' folder.")