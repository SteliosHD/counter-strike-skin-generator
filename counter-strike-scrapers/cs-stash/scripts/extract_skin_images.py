import os
import sqlite3

import pandas as pd


def convert_data(data, file_path):
    with open(file_path, "wb") as file:
        file.write(data)


def extract_all_skins_without_images_to_csv():
    csv_skins_relative_path = os.path.join(
        "..",
        "..",
        "..",
        "counter-strike-skin-classifiers",
        "data_preparation",
        "datasets",
    )
    csv_skins_path = os.path.abspath(os.path.join(csv_skins_relative_path, "skins_no_images_raw.csv"))
    con = sqlite3.connect("../db/cs-stash.db")
    fields = "id,skin_name,weapon_name,stat_trak,factory_new_price,quality"
    skins = pd.read_sql_query(f"SELECT {fields} FROM skins WHERE texture_image IS NOT NULL", con)
    skins.to_csv(csv_skins_path, index=False, header=fields.split(","))
    con.close()
    print(f"Extracted {skins.shape[0]} skins to {csv_skins_path}")


def extract_all_images():
    skin_images_relative_path = os.path.join(
        "..",
        "..",
        "..",
        "counter-strike-skin-classifiers",
        "data_preparation",
        "datasets",
        "skin_images",
    )
    skin_images_path = os.path.abspath(skin_images_relative_path)
    con = sqlite3.connect("../db/cs-stash.db")
    cursor = con.cursor()
    fields = "id,skin_name,quality,texture_image,weapon_name"
    query = f"SELECT {fields} FROM skins WHERE texture_image IS NOT NULL"
    cursor.execute(query)
    records = cursor.fetchall()

    for record in records:
        skin_id, skin_name, quality, texture_image, weapon_name = record
        file_path = os.path.join(
            skin_images_path,
            f"{skin_name.replace(' ', '')}_{skin_id}_{quality.replace(' ', '')}_{weapon_name.replace(' ', '')}.png",
        )
        convert_data(texture_image, file_path)
        print(f"Extracted {file_path} for {skin_name} ({quality}) with id {skin_id}")
    con.close()


if __name__ == "__main__":
    # extract_all_skins_without_images_to_csv()
    extract_all_images()
