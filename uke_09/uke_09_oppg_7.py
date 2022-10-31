def weather_report(weather_stations, city):
    station = weather_stations[city]
    wind_speed = station["Wind speed"]
    wind_dir = station["Wind direction"]
    precipitation = station["Precipitation"]
    device = station["Device"]
    print(f"The weather in {city}:\nThe wind speed is {wind_speed}m/s in the {wind_dir} direction and the precipitation is {precipitation}mm.\nThe measurement was done using the {device} weather station.")

weather_stations = {
    "Bergen": {
        "Wind speed": 3.6,
        "Wind direction": "northeast",
        "Precipitation": 5.2,
        "Device": "WeatherMaster500"
    },
    "Trondheim": {
        "Wind speed": 8.2,
        "Wind direction": "northwest",
        "Precipitation": 0.2,
        "Device": "ClimateDiscoverer3000"
    },
    "Svalbard": {
        "Wind speed": 7.5,
        "Wind direction": "southwest",
        "Precipitation": 1.1,
        "Device": "WeatherFinder5.0"
    },
}

weather_report(weather_stations, "Bergen")