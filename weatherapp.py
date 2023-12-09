
import requests

from dotenv import load_dotenv #loads dotenv library and loads .env file
import os

load_dotenv() #take environment variables from .env file

api_key = os.getenv("api_key") #environment variable

if not api_key: #Check if api key is avalable
    print("API key is missing. Make sure to set it in the .env file.")
    exit()


while True:
    user_city = input("Enter city: ")

    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&units=imperial&APPID={api_key}")

    if weather_data.json()["cod"] == '404':
        print("Please enter a valid city")
    else:

        #all the weather specifics put into variables
        weather = weather_data.json()['weather'][0]['description']
        temp = weather_data.json()['main']['temp']
        feels_like = weather_data.json()['main']['feels_like']
        temp_min = weather_data.json()['main']['temp_min']
        temp_max = weather_data.json()['main']['temp_max']
        humidity = weather_data.json()['main']['humidity']
        wind_speed = weather_data.json()['wind']['speed']

        
    print(f"Heres a full breakdown of the weather in {user_city}.\nSkies: {weather}\nFeels like: {feels_like}°F\nMin temp: {temp_min}°F\nMax temp: {temp_max}°F\nHumidity: {humidity}%\nWind speed: {wind_speed}mph")

    #this will ask the user if they wish to continue or quit the program
    predict_additional_weather = input("Would you like to receive the weather from another city? (yes/no): ")
    if predict_additional_weather !="yes":
        print("Thanks for using my applictaion!")
        break #edns loop after thanking user





'''
print(weather_data.json()) #will return all data from any given city
'''