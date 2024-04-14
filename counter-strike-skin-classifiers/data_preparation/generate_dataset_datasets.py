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


def save_datasets():
    dataset_prices_path = os.path.join(DATASET_BASE_PATH, "dataset_prices.pkl")
    dataset_qualities_path = os.path.join(DATASET_BASE_PATH, "dataset_qualities.pkl")
    with open(dataset_prices_path, "wb") as f:
        pickle.dump(dataset_prices, f)
    with open(dataset_qualities_path, "wb") as f:
        pickle.dump(dataset_qualities, f)


save_datasets()
print("Datasets saved")
