import pandas as pd
import os


def initial_import(csv_path: str):
    # Load the CSV into a DataFrame
    df = pd.read_csv(csv_path)

    # convert dollar columns to numeric
    dollar_columns = [
        "Total Net Worth",
        "Gross Income",
        "Net Income",
        "Total Monthly Income",
        "Total Spend",
        "Net Cash Savings",
        "IRA",
        "Taxable Accounts",
        "401k",
        "Total Liquid Assets",
    ]

    # remove dollar sign and commas from specified columns and then convert to numeric
    for col in dollar_columns:
        # Remove $ and commas
        df[col] = df[col].str.replace(r"[$,]", "", regex=True)
        # Convert to numeric, coercing errors to NaN
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # output generated dataframe
    return df


if __name__ == "__main__":
    # get current working directory
    current_directory = os.getcwd()

    # Go up one directory
    parent_path = os.path.join("..", current_directory)

    # construct the path to the CSV file
    path = parent_path + r"\storage\initial_import.csv"

    # generate the DataFrame from the CSV file
    df_initial_import = initial_import(path)

    # Dummy var to throw in break point for debug
    debug_here = True
