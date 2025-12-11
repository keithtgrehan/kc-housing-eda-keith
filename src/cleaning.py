"""
Cleaning utilities for the King County housing dataset.
"""

from pathlib import Path
import pandas as pd


def load_sales_details(
    sales_path: str | Path,
    details_path: str | Path
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load raw sales and details CSVs."""
    sales = pd.read_csv(sales_path)
    details = pd.read_csv(details_path)
    return sales, details


def merge_sales_details(sales: pd.DataFrame, details: pd.DataFrame) -> pd.DataFrame:
    """Merge sales.house_id with details.id."""
    df = sales.merge(details, left_on="house_id", right_on="id", how="left")
    return df


def standardise_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase, underscore-separated column names."""
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df


def apply_column_mapping(df: pd.DataFrame) -> pd.DataFrame:
    """Apply naming conventions from column_names.md."""
    df = df.copy()

    rename_map = {
        "id_y": "id",
        "id_x": "sales_id",
        "house_id": "house_id",
        "date": "date_date",
        "price": "price_price",
        "bedrooms": "bedrooms_number",
        "bathrooms": "bathrooms_number",
        "sqft_living": "sqft_living_square",
        "sqft_lot": "sqft_lot_square",
        "floors": "floors_total",
        "waterfront": "waterfront",
        "view": "view",
        "condition": "condition",
        "grade": "grade",
        "sqft_above": "sqft_above",
        "sqft_basement": "sqft_basement",
        "yr_built": "yr_built",
        "yr_renovated": "yr_renovated",
        "zipcode": "zipcode",
        "lat": "lat",
        "long": "long",
        "sqft_living15": "sqft_living15",
        "sqft_lot15": "sqft_lot15",
    }

    df = df.rename(columns=rename_map)
    return df


def clean_merged_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full cleaning pipeline:
    - standardise columns
    - apply mapping
    - drop duplicates
    - drop invalid prices
    """
    df = df.copy()

    df = standardise_column_names(df)
    df = apply_column_mapping(df)

    df = df.drop_duplicates()

    if "price_price" in df.columns:
        df = df[df["price_price"] > 0]

    return df
