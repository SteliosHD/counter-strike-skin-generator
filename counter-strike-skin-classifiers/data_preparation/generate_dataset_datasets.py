import os
import pickle

from datasets import load_dataset

DATASET_BASE_PATH = os.path.join(
    ".",
    "datasets",
)

price_images_path = os.path.join(DATASET_BASE_PATH, "skin_images_price_labeled", "price_image_datasets")
absolute_price_images_path = os.path.abspath(price_images_path)
dataset_prices = load_dataset("imagefolder", data_dir=absolute_price_images_path)
quality_images_path = os.path.join(DATASET_BASE_PATH, "skin_images_quality_labeled", "quality_image_datasets")
absolute_quality_images_path = os.path.abspath(quality_images_path)
dataset_qualities = load_dataset("imagefolder", data_dir=absolute_quality_images_path)
quality_images_path_2 = os.path.join(DATASET_BASE_PATH, "skin_images_quality_labeled", "quality_image_datasets_2")
absolute_quality_images_path_2 = os.path.abspath(quality_images_path_2)
dataset_qualities_2 = load_dataset("imagefolder", data_dir=absolute_quality_images_path_2)


def save_datasets():
    dataset_prices_path = os.path.join(DATASET_BASE_PATH, "dataset_prices.pkl")
    dataset_qualities_path = os.path.join(DATASET_BASE_PATH, "dataset_qualities.pkl")
    with open(dataset_prices_path, "wb") as f:
        pickle.dump(dataset_prices, f)
    with open(dataset_qualities_path, "wb") as f:
        pickle.dump(dataset_qualities, f)


if __name__ == "__main__":
    # save_datasets()
    # print("Datasets saved")
    # dataset_prices.push_to_hub("stelioshd/counter_strike_skins_prices")
    # dataset_qualities.push_to_hub("stelioshd/counter_strike_skins_quality")
    dataset_qualities_2.push_to_hub("stelioshd/counter_strike_skins_quality_2")
