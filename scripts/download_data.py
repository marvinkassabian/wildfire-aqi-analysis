import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

dataset_slug = "vijayveersingh/the-california-wildfire-data"
download_path = "../data/raw/california-wildfires"

os.makedirs(download_path, exist_ok=True)

api.dataset_download_files(dataset_slug, path=download_path, unzip=True)
print(f"Dataset downloaded to: {os.path.abspath(download_path)}")

dataset_slug = "calebreigada/us-air-quality-1980present"
download_path = "../data/raw/us-air-quality"

os.makedirs(download_path, exist_ok=True)

api.dataset_download_files(dataset_slug, path=download_path, unzip=True)
print(f"Dataset downloaded to: {os.path.abspath(download_path)}")