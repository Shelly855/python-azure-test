import requests
import os
from dotenv import load_dotenv  # import dotenv

# Load environment variables from .env file
load_dotenv()

# Get variables from the environment
AZURE_URL = os.getenv("AZURE_URL")
PREDICTION_KEY = os.getenv("PREDICTION_KEY")
IMAGE_PATH = os.getenv("IMAGE_PATH")

# Set headers
headers = {
    "Prediction-Key": PREDICTION_KEY,
    "Content-Type": "application/octet-stream"
}

# Open the image file in binary mode and send request
with open(IMAGE_PATH, "rb") as image:
    response = requests.post(AZURE_URL, headers=headers, data=image.read())

# Print API response
print(response.json())  # JSON output with predictions
