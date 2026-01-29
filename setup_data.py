import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Configuration
COMPETITION_NAME = 'ai-mathematical-olympiad-progress-prize-3'
DOWNLOAD_PATH = r'D:\Kaggle\ai-mathematical-olympiad-progress-prize-3'

def download_and_extract_data():
    try:
        # 以前の設定(環境変数)が残っていて干渉する場合があるため、
        # スクリプト実行中のみ環境変数を無視して kaggle.json を読み込ませます。
        env_vars = ['KAGGLE_USERNAME', 'KAGGLE_KEY', 'KAGGLE_CONFIG_DIR']
        for var in env_vars:
            if var in os.environ:
                print(f"Debug: Ignoring environment variable {var} to force using local kaggle.json")
                del os.environ[var]
        
        # Force using local kaggle.json
        current_dir = os.path.dirname(os.path.abspath(__file__))
        os.environ['KAGGLE_CONFIG_DIR'] = current_dir
        print(f"Debug: Set KAGGLE_CONFIG_DIR to {current_dir}")

        # Authenticate using default kaggle.json location (~/.kaggle/kaggle.json)
        api = KaggleApi()
        api.authenticate()
        print("Authentication successful.")

        print(f"Downloading competition data for: {COMPETITION_NAME}...")
        # Change to the target directory
        if not os.path.exists(DOWNLOAD_PATH):
            os.makedirs(DOWNLOAD_PATH)
        os.chdir(DOWNLOAD_PATH)

        # Download all files
        api.competition_download_files(COMPETITION_NAME, path=DOWNLOAD_PATH, quiet=False)
        print("Download complete.")

        # Unzip files
        print("Extracting files...")
        zip_filename = f"{COMPETITION_NAME}.zip"
        zip_path = os.path.join(DOWNLOAD_PATH, zip_filename)
        
        if os.path.exists(zip_path):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(DOWNLOAD_PATH)
            print("Extraction complete.")
            # Optional: Remove zip file after extraction
            # os.remove(zip_path) 
        else:
            print(f"Zip file not found: {zip_path}")
            # Sometimes it downloads individual files if there's no single zip, but usually competitions are zipped.

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure you have accepted the competition rules on Kaggle's website.")

if __name__ == "__main__":
    download_and_extract_data()
