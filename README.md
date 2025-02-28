# Day 1 Weather App

This project is a weather application that fetches current weather and forecast data for various cities using the OpenWeather API and stores the data in an AWS S3 bucket.

## Project Structure

weather-dashboard/
  src/
    __init__.py
    weather_dashboard.py
    services/
      s3.py
      openweather.py
  tests/
  data/
    cities.json
  .env
  .gitignore
  requirements.txt

## Prerequisites
- Python 3.x
- AWS account with S3 access
- OpenWeather API key

## Setups

1. Clone the repository:
--bash
git clone https://github.com/Haiyuecheng/Weatherdashboard.git

2. Change directory:
--bash
cd day-1-weather-app

3. Create a virtual environment:
--bash
python -m venv venv

4. Activate the virtual environment:
--bash
.\venv\Scripts\Activate          # for windows
source venv/bin/activate         # for mac/linux

5. Install the required packages:
--bash
pip install -r requirements.txt



## Create a .env file in the root directory with the following content:
OPEN_WEATHER_API_KEY=your_openweather_api_key
AWS_BUCKET_NAME=your_bucket_name
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_DEFAULT_REGION=your_aws_region


## Ensure you have a cities.json file in the data directory with the following structure and Replace City1, City2, and City3 with the names of the cities you want to fetch weather data for.
{
    "cities": ["City1", "City2", "City3"]
}

## To run the application, execute the following command
python src/__init__.py


