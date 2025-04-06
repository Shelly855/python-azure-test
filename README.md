# Azure Prediction Test Script

This Python script was created as part of the [Animal Custom Vision project](https://github.com/animal-vision/animal-custom-vision) to test integration between Python and Azure Custom Vision. It sends a local image to a trained model and prints out prediction results in JSON format.

## Prerequisites

- Python 3.8 or higher  
- The `requests` Python package  
  Install it with:
  ```bash
  pip install requests

- An active Azure Custom Vision resource:
  - A trained and published model  
  - A Prediction key  
  - A Prediction endpoint URL  

- A local image file to use for prediction

- You’ll also need to configure the following environment variables:
  - `AZURE_URL` – your Custom Vision prediction endpoint  
  - `PREDICTION_KEY` – your Azure prediction key  
  - `IMAGE_PATH` – path to the image you want to test

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/Shelly855/python-azure-test.git
   cd python-azure-test
2. Run `cp .env.example .env` to create your environment file.
3. Add your Azure credentials and image path to `.env`:
   - `AZURE_URL`
   - `PREDICTION_KEY`
   - `IMAGE_PATH`

The script uses `requests` to send a POST request to the model endpoint with image data, and prints the response containing prediction tags and confidence levels.
