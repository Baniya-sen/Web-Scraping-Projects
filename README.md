# Python Web Scraping Projects

This collection features Python scripts that utilize web scraping techniques to extract data from various online sources. Each project serves a specific purpose and demonstrates the power of web scraping for retrieving valuable information.

## Billboard Top 100 Songs Playlist Creator

The Billboard Top 100 Songs Playlist Creator is a Python script designed to scrape the Billboard website for the top 100 songs on a specified date provided by the user. It then retrieves the corresponding songs from Spotify using the Spotify API (OAuth authentication), and finally, creates a private playlist with those songs on the user's Spotify account.

## Pre-requisites
Install:
```Python
pip install beautifulsoup4
pip install spotipy
```
If installation fails, try updating Python to the 3.12 version!

### Usage

1. Add your credentials for Spotify by getting the client ID and secret from the `developer.spotify.com` website.
2. It will generate a token for the current session. Keep it secret.
3. **Run the Script**: Execute the `billboard_to_spotify.py` file and follow the on-screen prompts to enter the desired date and authenticate with Spotify.
4. **Playlist Creation**: The script will automatically scrape the Billboard website, fetch the top songs, search for them on Spotify, and create a private playlist with those songs in your Spotify account.
5. If the token is expired, then it will automatically generate a new one.
6. It will list the songs that weren't found.

### Output

Below is an example of the created private playlist on Spotify:

![Playlist Created](https://github.com/Baniya-sen/Web-Scraping-Projects/assets/144620117/83c77564-db13-44a3-ad4e-9462abe573bf)

![Spotify Playlist](https://github.com/Baniya-sen/Web-Scraping-Projects/assets/144620117/ceca3d17-8584-4b6e-977d-37b4382cd7fa)


## Weather Checker

The Weather Checker script is a simple Python application that retrieves weather information for a specified latitude and longitude. It checks if today is a rainy day based on the weather forecast for the provided location.

## Pre-requisites
Install:
```Python
pip install requests
```

### Usage

1. **Set Location**: Modify the latitude and longitude constants in the script to specify the desired location for weather checking.
2. **Run the Script**: Execute the `weather_checker.py` file.
3. **Check Weather**: The script will retrieve the weather information for the specified location and notify if today is expected to be rainy.

Feel free to explore and utilize these web scraping projects for your own purposes. Happy coding!
