import os

import pandas as pd

DATASET_BASE_PATH = os.path.join(
    ".",
    "datasets",
)


def load_image_file_based_on_name_pattern(name_pattern_params: list[str]):
    skin_images_relative_path = os.path.join(
        DATASET_BASE_PATH,
        "skin_images",
    )
    skin_images_path = os.path.abspath(skin_images_relative_path)
    for file in os.listdir(skin_images_path):
        pattern_params_in_file = all(param in file for param in name_pattern_params)
        if pattern_params_in_file:
            return file
    raise FileNotFoundError(f"File with name pattern {name_pattern_params} not found in {skin_images_path}")


def price_string_to_float(price_string: str):
    expected_symbols = ["€", ",", "-", "."]
    symbols_in_string = any(symbol in price_string for symbol in expected_symbols)
    digits_in_string = any(char.isdigit() for char in price_string)
    if not symbols_in_string or not digits_in_string:
        return None
    return float(price_string.replace("€", "").replace(",", ".").replace("-", "0").replace(" ", ""))


def quality_class_to_int(quality_class: str):
    quality_classes = {
        "Consumer Grade": 0,
        "Industrial Grade": 1,
        "Mil-Spec": 2,
        "Restricted": 3,
        "Classified": 4,
        "Covert": 5,
        "Contraband": 6,
        "knives": 7,
    }
    for quality, quality_class_int in quality_classes.items():
        if quality in quality_class:
            return quality_class_int
    raise ValueError(f"Quality class {quality_class} not found in {quality_classes}")


def clean_raw_skin_data(
    skins_raw_path: str, return_raw_df: bool = False
) -> pd.DataFrame or tuple[pd.DataFrame, pd.DataFrame]:
    skins_raw_df = pd.read_csv(skins_raw_path)
    skin_processed_df = skins_raw_df.copy()
    # Format prices and quality classes
    skin_processed_df["factory_new_price"] = skin_processed_df["factory_new_price"].apply(price_string_to_float)
    skin_processed_df["quality"] = skin_processed_df["quality"].apply(quality_class_to_int)
    if return_raw_df:
        return skin_processed_df, skins_raw_df
    return skin_processed_df


def clean_data(
    raw_data_path: str = os.path.join(
        DATASET_BASE_PATH,
        "skins_no_images_raw.csv",
    ),
    cleaned_data_path: str = os.path.join(
        DATASET_BASE_PATH,
        "skins_no_images_cleaned.csv",
    ),
    save: bool = True,
    drop_na: bool = False,
) -> pd.DataFrame:
    cleaned_df = clean_raw_skin_data(raw_data_path)
    if save:
        cleaned_df.to_csv(cleaned_data_path, index=False)
    if drop_na:
        cleaned_df = cleaned_df.dropna()
    return cleaned_df


def skin_no_knives(
    data_path: str = os.path.join(
        DATASET_BASE_PATH,
        "skins_no_images_cleaned.csv",
    ),
    cleaned_data_path: str = os.path.join(
        DATASET_BASE_PATH,
        "skins_no_images_no_knives.csv",
    ),
    save: bool = True,
    drop_na: bool = False,
) -> pd.DataFrame:
    df = pd.read_csv(data_path)
    no_knives_df = df[df["quality"] != 7]
    if drop_na:
        no_knives_df = no_knives_df.dropna()
    if save:
        no_knives_df.to_csv(cleaned_data_path, index=False)
    return no_knives_df


if __name__ == "__main__":
    cleaned_df = clean_data()
    print(f"Cleaned {cleaned_df.shape[0]} skins to \n{cleaned_df}")
    skins_with_no_missing_values_path = os.path.join(
        DATASET_BASE_PATH,
        "skins_no_images_no_missing_prices.csv",
    )
    cleaned_df_with_no_missing_values = clean_data(drop_na=True, cleaned_data_path=skins_with_no_missing_values_path)
    print(
        f"Cleaned no missing prices {cleaned_df_with_no_missing_values.shape[0]} skins to "
        f"\n{cleaned_df_with_no_missing_values}"
    )
