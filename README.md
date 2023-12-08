This is a weather program that I've created within Python that utilises data from the OpenWeatherMap API to retrieve weather data for a city specified by the user. 
The code begins by importing the necessary libraries: requests for making HTTP requests and load_dotenv along with os for handling environment variables, particularly the OpenWeatherMap API key.

The program proceeds to load the API key from the .env file using load_dotenv. Following this, it checks the availability of the API key. If the key is missing, the program displays an error message and exits gracefully.

The main functionality is encapsulated within an infinite loop. Within each iteration, the user is prompted to input a city. The program then sends a request to the OpenWeatherMap API to obtain weather data for the specified city.

Error handling is implemented to check if the API response indicates an error, specifically an HTTP status code of 404. In such cases, the user is prompted to enter a valid city.

Upon a successful API response, the program parses the JSON data to extract various weather details, including the weather description, temperature, feels-like temperature, minimum and maximum temperature, humidity, and wind speed.

The extracted weather information is then presented in a formatted manner, providing the user with a comprehensive breakdown of the weather conditions for the entered city.

To enhance user interaction, the program prompts the user to decide whether they would like to receive weather information for another city. If the user chooses not to continue, a thank-you message is displayed, and the program gracefully exits the infinite loop.

