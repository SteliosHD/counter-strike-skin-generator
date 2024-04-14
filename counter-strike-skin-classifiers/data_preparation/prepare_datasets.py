import os
from shutil import copy

DATASET_BASE_PATH = os.path.join(
    ".",
    "datasets",
)


def image_path_name_category_finder(image_path: str, path_type: str = "price") -> int:
    if path_type == "price":
        return get_price_class_from_image_path(image_path)
    return get_quality_class_from_image_path(image_path)


def get_quality_class_from_image_path(image_path: str) -> int:
    quality = image_path.split("_")[0]
    return int(quality)


def get_price_class_from_image_path(image_path: str) -> int:
    price = image_path.split("_")[1]
    return int(price)


def get_category_subfolder_path(dataset_path: str, category: int, path_type) -> str:
    return os.path.join(dataset_path, f"{'P' if path_type == 'price' else 'Q'}{category}")


def split_images_to_train_test_eval(
    data_path: str = os.path.join(
        DATASET_BASE_PATH,
        "skin_images_price_labeled",
        "price_image_datasets",
    ),
    train_size: float = 0.7,
    test_size: float = 0.2,
    path_type: str = "price",
):
    train_path = os.path.abspath(os.path.join(data_path, "train"))
    test_path = os.path.abspath(os.path.join(data_path, "test"))
    eval_path = os.path.abspath(os.path.join(data_path, "eval"))
    images = os.listdir(data_path)
    for index, image in enumerate(images):
        print(f"Processing image {index + 1}/{len(images)} - {image}")
        image_path = os.path.join(data_path, image)
        try:
            if index % 10 < train_size * 10:
                image_category = image_path_name_category_finder(image, path_type)
                category_path = get_category_subfolder_path(train_path, image_category, path_type)
                os.makedirs(category_path, exist_ok=True)
                print(f"Copying {image} to {category_path}")
                copy(image_path, category_path)
            elif index % 10 < (train_size + test_size) * 10:
                image_category = image_path_name_category_finder(image, path_type)
                category_path = get_category_subfolder_path(test_path, image_category, path_type)
                os.makedirs(category_path, exist_ok=True)
                print(f"Copying {image} to {category_path}")
                copy(image_path, category_path)
            else:
                image_category = image_path_name_category_finder(image, path_type)
                category_path = get_category_subfolder_path(eval_path, image_category, path_type)
                os.makedirs(category_path, exist_ok=True)
                print(f"Copying {image} to {category_path}")
                copy(image_path, category_path)
        except Exception as e:
            print(f"Error processing image {image}: {e}")
    print(f"Done copying images to subfolders for {path_type}")


def copy_images_to_subfolders():
    # split_images_to_train_test_eval()
    split_images_to_train_test_eval(
        data_path=os.path.join(DATASET_BASE_PATH, "skin_images_quality_labeled", "quality_image_datasets"),
        path_type="quality",
    )


if __name__ == "__main__":
    copy_images_to_subfolders()
