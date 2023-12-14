from dotenv import load_dotenv
load_dotenv()
import os
import json
from credit_default.constant.environment.variable_key import MONGO_DB_URL_ENV_KEY,KAGGLE_DIR
kaggle_config_dir = os.getenv(KAGGLE_DIR)
print (kaggle_config_dir)

url = os.getenv(MONGO_DB_URL_ENV_KEY)
print (url)


# os.environ['KAGGLE_CONFIG_DIR'] = kaggle_config_dir
# os.chdir("../")
# Load environment variables from the .env file


# json_path = os.environ.get("KAGGLE_CONFIG_DIR") 

# print (json_path)
# with open(json_path) as f:
#     creds = json.load(f)

# print (creds)

from kaggle.api.kaggle_api_extended import KaggleApi