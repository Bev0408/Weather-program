# Weather App ⛅

## Overview
This is a weather program that I've created within Python that utilises data from the OpenWeatherMap API to retrieve weather data for a city specified by the user. 
The code begins by importing the necessary libraries:  requests for making HTTP requests and load_dotenv along with os for handling environment variables, particularly the OpenWeatherMap API key.

## Features 💡
- **API Integration:** Utilises the OpenWeatherMap API to fetch weather data
- **User Interaction:** prompts the user to input the desired city they'd like to know the  specific weather details for.
- **Version Control:** Both Git and GitHub have been utilised for version control 

## Requirements ✔️
- Python 3.10.6
- Python packages: 'dotenv' 'requests'
  
## Setup 🚀:
1. Clone the repository: `git clone [https://github.com/Bev0408/Weather-program]`
   
2. Install dependencies: `pip install -r requirements.txt`
   
3. Create a `.env` file and add your OpenWeatherMap API key:
    ```
    api_key=[Your_API_Key]
    ```
4. Run the application: `python weather_app.py`
## How To Use Program 🗒️
1. Run the application.
2. Enter the city when prompted.
3. View detailed weather information.
4. Optionally, choose to receive weather information for another city.
5. Exit the application when done.
## Error handling :warning:
The application includes error handling to manage situations where the API key is missing (will be prompted to add API key to .env file), an invalid city is entered, or network/API request failures occur.

## Licence 📜:

This project is licenced under the [MIT License](LICENCE).

