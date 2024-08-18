

This project demonstrates a data engineering pipeline that extracts football match data from API-FOOTBALL, loads it into Google BigQuery, transforms it using dbt, and visualizes the results using Google Data Studio.

## Architecture

1. Data Extraction: Python script using requests to fetch data from API-FOOTBALL
2. Data Loading: Google Cloud BigQuery for data storage
3. Data Transformation: dbt for data modeling and transformation
4. Data Visualization: Google Data Studio for creating dashboards

## Setup

1. Clone this repository
2. Set up a Google Cloud Platform account and create a new project
3. Enable the BigQuery API and create a service account with BigQuery Admin access
4. Save the service account key as `service_account_key.json` in the project root
5. Sign up for API-FOOTBALL on RapidAPI and get your API key
6. Set up a Python virtual environment: `python -m venv venv`
7. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix or MacOS: `source venv/bin/activate`
8. Install requirements: `pip install dbt-bigquery python-dotenv pandas requests google-cloud-bigquery`
9. Create a `.env` file with the following contents:
   ```
   API_FOOTBALL_KEY=your_api_key_here
   GCP_PROJECT_ID=your_gcp_project_id_here
   ```
10. Set up dbt profile in `~/.dbt/profiles.yml`

## Usage

1. Run data extraction and loading: `python extract_data.py`
2. Run dbt models: 
   ```
   cd football_dbt
   dbt run
   dbt test
   ```
3. Set up a Google Data Studio dashboard connecting to your BigQuery dataset

## dbt Models

- `team_performance`: Aggregates team statistics from match data

## Looker Visualisations

### 2023 English Premier League Team Performances
![football_team_performance](Looker_Visualisation.png)

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
Copyright (c) 2024, Ye Xiang Chen
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Contact
Adrian Ye Xiang Chen - yexiangchen0311@gmail.com
