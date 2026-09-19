import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../TASK_1_DATA_CLEANING/cleaned_retail_sales_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])
print("Dataset loaded successfully!")
print(df.head())
print("\n--DATASET SHAPE--")
print(df.shape)
print("\n--CLOUMN NAMES--")
print(df.columns)
print("\n--DATA TYPES--")
print(df.dtypes)
print("\n--DATASET INFORMATION--")
df.info()

print("\n--DESCRIPTIVE STATISTICS--")
print(df.describe())

print("\n--GENDER DISTRIBUTION--")
print(df["Gender"].value_counts())
print("\n--PRODUCT CATEGORY DISTRIBUTION--")
print(df["Product Category"].value_counts())

print("\n--SALES BY PRODUCT CATEGORY--")
category_sales = df.groupby("Product Category")["Total Amount"].sum()
print(category_sales)

print("\n--AVERAGE TRANSACTION VALUE BY CATEGORY--")
category_average = df.groupby("Product Category")["Total Amount"].mean()
print(category_average)

print("\n--SALES BY GENDER--")
gender_sales = df.groupby("Gender")["Total Amount"].sum()
print(gender_sales)

print("\n--AVERAGE SPENDING BY GENDER--")
gender_average = df.groupby("Gender")["Total Amount"].mean()
print(gender_average)

print("\n--AGE STATISTICS--")
print("Minimum Age:", df["Age"].min())
print("Maxmum Age:", df["Age"].max())
print("Average Age:", df["Age"].mean())
print("Median Age:", df["Age"].median())

df["Age Group"] = pd.cut(df["Age"],bins = [17,25,35,45,55,65],labels = ["18-25","26-35","36-45","46-55","56-65"])
print("\n--SALES BY AGE GROUP--")
age_sales = df.groupby("Age Group",observed =True)["Total Amount"].sum()
print(age_sales)

print("\n--TOP 10 TRANSACTIONS--")
top_transactions = df.sort_values(by="Total Amount",ascending =False).head(10)
print(top_transactions[["Transaction ID","Customer ID","Product Category","Quantity","Total Amount"]])

Q1 = df["Total Amount"].quantile(0.25)
Q3 = df["Total Amount"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df["Total Amount"]<lower_bound) | (df["Total Amount"]>upper_bound)]

print("\n--OUTLIER ANALYSIS--")
print("Q1:",Q1)
print("Q3:",Q3)
print("IQR:",IQR)
print("Lower Bound:",lower_bound)
print("Upper Bound:",upper_bound)
print("Number of Outliers:",len(outliers))



print("\n--BUSINESS INSIGHTS--")
print("Total Revenue:",df["Total Amount"].sum())
print("Average Transaction Amount:",df["Total Amount"].mean())
print("Total Quantity Sold:",df["Quantity"].sum())
print("Best Selling Category:",df.groupby("Product Category")["Quantity"].sum().idxmax())
print("Highest Revenue Category:",df.groupby("Product Category")["Total Amount"].sum().idxmax())
print("Most Common Gender:",df["Gender"].mode()[0])
print("Average Customer Age:",df["Age"].mean())