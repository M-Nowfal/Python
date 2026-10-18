# PROGRAM 11 – Program to demonstrate the operations of pandas library.

import numpy as np
import pandas as pd

raw_data = {
  "Employee_ID": [101, 102, 103, 104, 105],
  "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
  "Department": ["HR", "IT", "IT", "Finance", "HR"],
  "Salary": [55000, 85000, np.nan, 72000, 60000],
  "Years_Exp": [3, 7, 5, 2, 4]
}

df = pd.DataFrame(raw_data)

print(df)

print("\n" + "=" * 30 + "\n")

print("\nData Frame Shape (Rows, Columns):", df.shape)

df.info()

print(df.describe())

print("\n" + "=" * 30 + "\n")

print("Selecting 'Name' Column:")

print(df["Name"])

print("\nFiltering Employees with Salary > 60,000:")

high_earners = df[df["Salary"] > 60000]

print(high_earners)

print(df.loc[0:2, ["Name", "Department"]])

print("\n" + "=" * 30 + "\n")

print(df.isnull().sum())

mean_salary = df["Salary"].mean()

df["Salary"] = df["Salary"].fillna(mean_salary)

print(df)

print("\n" + "=" * 30 + "\n")

df["Bonus"] = df["Salary"] * 0.10

print(df)

df_sorted = df.sort_values(
  by="Salary",
  ascending=False
)

print(df_sorted)

print("\n" + "=" * 30 + "\n")

dept_summary = df.groupby("Department")[
  ["Salary", "Years_Exp"]
].mean()

print(dept_summary)

print("\n" + "=" * 30 + "\n")

output_filename = "processed_employee_data.csv"

df.to_csv(output_filename, index=False)