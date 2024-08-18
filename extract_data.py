import os
import requests
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API-FOOTBALL configuration
API_KEY = os.getenv('API_FOOTBALL_KEY')
API_HOST = "api-football-v1.p.rapidapi.com"
BASE_URL = f"https://{API_HOST}/v3"

# BigQuery configuration
PROJECT_ID = os.getenv('GCP_PROJECT_ID')
DATASET_ID = "football_data"
TABLE_ID = "matches"

def get_matches(league_id, season):
    url = f"{BASE_URL}/fixtures"
    querystring = {"league": league_id, "season": season}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # This will raise an exception for HTTP errors
    data = response.json()
    if 'response' not in data:
        print(f"Unexpected API response: {data}")
        return []
    return data['response']

def process_matches(matches):
    processed_data = []
    for match in matches:
        processed_data.append({
            'match_id': match['fixture']['id'],
            'date': match['fixture']['date'],
            'home_team': match['teams']['home']['name'],
            'away_team': match['teams']['away']['name'],
            'home_goals': match['goals']['home'],
            'away_goals': match['goals']['away']
        })
    return pd.DataFrame(processed_data)

def load_to_bigquery(df):
    credentials = service_account.Credentials.from_service_account_file(
        'service_account_key.json',
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
    
    # Create dataset if it doesn't exist
    dataset_ref = client.dataset(DATASET_ID)
    try:
        client.get_dataset(dataset_ref)
    except Exception:
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US"
        client.create_dataset(dataset)
    
    # Load data to BigQuery
    table_ref = dataset_ref.table(TABLE_ID)
    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.source_format = bigquery.SourceFormat.CSV
    
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # Wait for the job to complete

if __name__ == "__main__":
    league_id = 39  # English Premier League
    season = 2023
    
    try:
        matches = get_matches(league_id, season)
        if matches:
            df = process_matches(matches)
            load_to_bigquery(df)
            print("Data loaded to BigQuery successfully!")
        else:
            print("No matches data retrieved from the API.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from the API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")