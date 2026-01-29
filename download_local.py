import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Configuration
COMPETITION_NAME = 'ai-mathematical-olympiad-progress-prize-3'
WORK_DIR = r'D:\Kaggle\ai-mathematical-olympiad-progress-prize-3'

def download_with_local_key():
    print(f"Working Directory: {WORK_DIR}")
    
    # 1. Force Kaggle to look for config (kaggle.json) ONLY in this directory
    os.environ['KAGGLE_CONFIG_DIR'] = WORK_DIR
    
    # Check if kaggle.json exists here
    json_path = os.path.join(WORK_DIR, 'kaggle.json')
    if not os.path.exists(json_path):
        print(f"ERROR: kaggle.json not found in {WORK_DIR}")
        print("Please copy your kaggle.json file to this folder and run the script again.")
        return

    try:
        print("Authenticating using local kaggle.json...")
        api = KaggleApi()
        api.authenticate()
        print("Authentication successful!")

        print(f"Downloading data for {COMPETITION_NAME}...")
        api.competition_download_files(COMPETITION_NAME, path=WORK_DIR, quiet=False)
        print("Download complete.")

        print("Extracting files...")
        zip_filename = f"{COMPETITION_NAME}.zip"
        zip_path = os.path.join(WORK_DIR, zip_filename)
        
        if os.path.exists(zip_path):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(WORK_DIR)
            print("Extraction complete.")
            
            # Cleanup zip
            try:
                os.remove(zip_path)
                print("Removed zip file.")
            except:
                pass
        else:
            print("Zip file not found. Skipping extraction.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_with_local_key()
