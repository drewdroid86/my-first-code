import requests # Import the requests library to make HTTP requests to web APIs.
import datetime # Import the datetime module to work with dates and times, specifically for the current timestamp.

def get_weather(latitude, longitude): # Define a function named get_weather that takes latitude and longitude as arguments.
    """ # Start of a docstring explaining what the function does.
    Fetches current weather data for a given latitude and longitude using Open-Meteo. # Description of the function's purpose.
    """ # End of the docstring.
    weather_url = "https://api.open-meteo.com/v1/forecast" # Define the base URL for the Open-Meteo API.
    params = { # Create a dictionary to hold the parameters for the API request.
        "latitude": latitude, # Set the latitude parameter using the function argument.
        "longitude": longitude, # Set the longitude parameter using the function argument.
        "current_weather": "true", # Request current weather data.
        "temperature_unit": "fahrenheit", # Specify temperature in Fahrenheit.
        "timezone": "America/New_York" # Set the timezone for the location.
    } # End of the parameters dictionary.
    try: # Start a try block to handle potential errors during the API call.
        response = requests.get(weather_url, params=params) # Make an HTTP GET request to the weather API with the defined parameters.
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx status codes).
        weather_data = response.json() # Parse the JSON response body into a Python dictionary.
        current = weather_data.get("current_weather", {}) # Get the "current_weather" dictionary from the response, or an empty dict if not found.
        temperature = current.get("temperature") # Extract the "temperature" from the current weather data.
        windspeed = current.get("windspeed") # Extract the "windspeed" from the current weather data.
        return f"{temperature}°F, Wind: {windspeed} mph" # Return a formatted string with temperature and wind speed.
    except requests.exceptions.RequestException as e: # Catch any request-related exceptions (e.g., network issues, invalid URL).
        return f"Error fetching weather: {e}" # Return an error message if fetching weather fails.

def get_bitcoin_price(): # Define a function named get_bitcoin_price that takes no arguments.
    """ # Start of a docstring explaining what the function does.
    Fetches the current Bitcoin price in USD using CoinGecko. # Description of the function's purpose.
    """ # End of the docstring.
    bitcoin_url = "https://api.coingecko.com/api/v3/simple/price" # Define the base URL for the CoinGecko API.
    params = { # Create a dictionary to hold the parameters for the API request.
        "ids": "bitcoin", # Specify that we want data for Bitcoin.
        "vs_currencies": "usd" # Specify that we want the price in US Dollars.
    } # End of the parameters dictionary.
    try: # Start a try block to handle potential errors during the API call.
        response = requests.get(bitcoin_url, params=params) # Make an HTTP GET request to the Bitcoin price API with the defined parameters.
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx status codes).
        bitcoin_data = response.json() # Parse the JSON response body into a Python dictionary.
        price = bitcoin_data.get("bitcoin", {}).get("usd") # Navigate the dictionary to get the USD price of Bitcoin.
        if price: # Check if a price was successfully retrieved.
            return f"${price:,.2f}" # Return the formatted price with two decimal places and comma separators.
        else: # If no price was found.
            return "N/A" # Return "N/A" indicating the price is not available.
    except requests.exceptions.RequestException as e: # Catch any request-related exceptions.
        return f"Error fetching Bitcoin price: {e}" # Return an error message if fetching Bitcoin price fails.

if __name__ == "__main__": # This block ensures the code inside only runs when the script is executed directly (not imported as a module).
    # Canton, GA coordinates # Comment indicating the following lines define coordinates for Canton, GA.
    canton_ga_latitude = 34.2384 # Define the latitude for Canton, GA.
    canton_ga_longitude = -84.4877 # Define the longitude for Canton, GA.

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Get the current date and time and format it as a string.

    weather_report = get_weather(canton_ga_latitude, canton_ga_longitude) # Call the get_weather function with Canton, GA's coordinates.
    bitcoin_price = get_bitcoin_price() # Call the get_bitcoin_price function.

    print("--- Morning Report ---") # Print a header for the report.
    print(f"Report Time: {current_time}") # Print the current time of the report.
    print("-" * 20) # Print a separator line.
    print(f"Canton, GA Weather: {weather_report}") # Print the weather report for Canton, GA.
    print(f"Bitcoin Price (USD): {bitcoin_price}") # Print the current Bitcoin price.
    print("----------------------") # Print a footer for the report.
