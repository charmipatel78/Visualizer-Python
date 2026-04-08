import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = None

print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("==================== Data Analysis & Visualization Program ====================")

while True:
    print("\nPlease select an option : ")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operation")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("===============================================================================")

    try:
        c = int(input("Enter the Choice -> ").strip())
    except ValueError:
        print("Invalid input! Please enter a number between 1–8.")
        continue

    # ----------------- Load Dataset -----------------
    if c == 1:
        path = input("Enter the path of csv file -> ").strip().strip('"')
        if os.path.exists(path):
            try:
                df = pd.read_csv(path)
                print("Dataset Loaded Successfully!\n")
            except Exception as e:
                print("Error loading dataset:", e)
        else:
            print("File not found. Please check path again.")

    # ----------------- Explore Data -----------------
    elif c == 2:
        if df is None:
            print("Please load dataset first (choice 1).")
            continue

        while True:
            print("\n=== Explore Data ===")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Exit")
            try:
                i = int(input("Enter your Choice -> "))
            except ValueError:
                print("Invalid input.")
                continue

            if i == 1:
                print(df.head(5))
            elif i == 2:
                print(df.tail(5))
            elif i == 3:
                print(df.columns.tolist())
            elif i == 4:
                print(df.dtypes)
            elif i == 5:
                print(df.info())
            elif i == 6:
                break
            else:
                print("Invalid Choice")

    # ----------------- DataFrame Operations -----------------
    elif c == 3:
        if df is None:
            print("Please load dataset first (choice 1).")
            continue

        while True:
            print("\n=== Perform DataFrame Operation ===")
            print("1. Check missing values")
            print("2. Describe Dataset")
            print("3. Exit")
            try:
                m = int(input("Enter your choice -> "))
            except ValueError:
                print("Invalid input.")
                continue

            if m == 1:
                print(df.isnull().sum())
            elif m == 2:
                print(df.describe())
            elif m == 3:
                break
            else:
                print("Invalid Choice")

    # ----------------- Handle Missing Data -----------------
    elif c == 4:
        if df is None:
            print("Please load dataset first (choice 1).")
            continue

        while True:
            print("\n=== Handle Missing Data ===")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Exit")
            try:
                h = int(input("Enter the choice -> "))
            except ValueError:
                print("Invalid input.")
                continue

            if h == 1:
                print(df[df.isnull().any(axis=1)])
            elif h == 2:
                df.fillna(df.mean(numeric_only=True), inplace=True)
                print("Missing values filled with column mean.")
            elif h == 3:
                df.dropna(inplace=True)
                print("Rows with missing values dropped.")
            elif h == 4:
                val = input("Enter the value to replace missing values -> ")
                df.fillna(val, inplace=True)
                print("Missing values replaced.")
            elif h == 5:
                break
            else:
                print("Invalid Choice")

    # ----------------- Descriptive Statistics -----------------
    elif c == 5:
        if df is None:
            print(" Please load dataset first (choice 1).")
        else:
            print(df.describe())

    # ----------------- Data Visualization -----------------
    elif c == 6:
        if df is None:
            print("Please load dataset first (choice 1).")
            continue

        while True:
            print("\n=== Data Visualization ===")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Exit")
            try:
                v = int(input("Enter your Choice -> "))
            except ValueError:
                print("Invalid input.")
                continue

            if v == 7:
                break

            x = input("Enter x-axis column name -> ")
            y = input("Enter y-axis column name -> ")

            try:
                if v == 1:
                    df.groupby(x)[y].sum().plot(kind="bar", figsize=(8,7), title="Bar Plot")
                    plt.show()
                elif v == 2:
                    plt.figure(figsize=(8, 7))
                    plt.plot(df[x], df[y], marker='o')
                    plt.title("Line Plot")
                    plt.show()
                elif v == 3:
                    plt.scatter(df[x], df[y])
                    plt.title("Scatter Plot")
                    plt.show()
                elif v == 4:
                    plt.pie(df[y], labels=df[x], autopct='%1.1f%%')
                    plt.title("Pie Chart")
                    plt.show()
                elif v == 5:
                    sns.histplot(data=df, x=x)
                    plt.title("Histogram")
                    plt.show()
                elif v == 6:
                    plt.stackplot(df[x], df[y])
                    plt.title("Stack Plot")
                    plt.show()
                else:
                    print("Invalid Choice")
            except Exception as e:
                print("Visualization error:", e)

    # ----------------- Save Visualization -----------------
    elif c == 7:
        try:
            save = input("Enter File Name To save Plot (with .png) -> ").strip()
            plt.savefig(save)
            print("Plot saved as", save)
        except Exception as e:
            print("Error saving plot:", e)

    # ----------------- Exit -----------------
    elif c == 8:
        print("Thank You! Visit Again.")
        break

    else:
        print("Invalid Choice")


