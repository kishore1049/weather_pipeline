import requests
import json


def fetch_weather_data():
    """
    Fetch weather data from the Weatherstack API.
    Replace the API key with your actual key.
    """
    url = "http://api.weatherstack.com/current"  # Correct API endpoint
    params = {
        "access_key": "6d6243efe1d38a8dc5351338a288c5a2",  # Replace with your actual API key
        "query": "Manchester",  # City to fetch weather for
    }

    try:
        response = requests.get(url, params=params)
        print(f"Status Code: {response.status_code}")

        # Check if the response is successful
        if response.status_code == 200:
            try:
                data = response.json()  # Parse JSON response
                return data
            except requests.exceptions.JSONDecodeError as e:
                print(f"JSON Decode Error: {e}")
                print(f"Response Text: {response.text}")
                return None
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response Text: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None


def process_weather_data(weather_data):
    """
    Process the fetched weather data (example implementation).
    """
    if weather_data:
        print("Processing weather data...")
        try:
            location = weather_data.get("location", {})
            current = weather_data.get("current", {})

            city = location.get("name", "Unknown")
            temperature = current.get("temperature", "Unknown")
            weather_description = current.get("weather_descriptions", ["Unknown"])[0]

            print(f"City: {city}")
            print(f"Temperature: {temperature}°C")
            print(f"Weather Description: {weather_description}")
        except Exception as e:
            print(f"Error while processing data: {e}")
    else:
        print("No weather data to process.")


def save_weather_data_to_file(weather_data):
    """
    Save the weather data to a file.
    """
    try:
        with open("weather_data.json", "w") as file:
            json.dump(weather_data, file, indent=4)
        print("Weather data saved to 'weather_data.json'")
    except Exception as e:
        print(f"Error saving data to file: {e}")


def main():
    """
    Main ETL pipeline to fetch, process, and store weather data.
    """
    print("Starting Weather Data ETL Pipeline...")

    # Fetch data
    weather_data = fetch_weather_data()

    # Process data
    process_weather_data(weather_data)

    # Save data
    if weather_data:
        save_weather_data_to_file(weather_data)

    print("ETL Pipeline Finished.")


if __name__ == "__main__":
    main()
