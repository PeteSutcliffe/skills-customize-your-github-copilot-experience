import pandas as pd
import numpy as np


def load_data(filename="data.csv"):
    return pd.read_csv(filename)


def main():
    df = load_data()

    print("First 5 rows:")
    print(df.head(), "\n")

    print("Dataset shape:", df.shape)
    print("Columns:", df.columns.tolist(), "\n")

    print("Summary statistics:")
    print(df.describe(), "\n")

    # TODO: Compute statistics using pandas and numpy
    # mean_hours = df["Hours_Studied"].mean()
    # median_score = df["Test_Score"].median()
    # variance_attendance = np.var(df["Attendance"], ddof=1)
    # std_score = np.std(df["Test_Score"], ddof=1)

    # TODO: Calculate correlation and identify the highest variance column


if __name__ == "__main__":
    main()
