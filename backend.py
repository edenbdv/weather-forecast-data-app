import requests

API_KEY = "d38782a85c73189b7e855ca377eaf388"


def get_data(place, forecast_days=None, kind=None):
    # get JSON data for any city for the next five days
    # at an interval of 3 hours
    url = f"http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]

    # the length of the list is 40 because the data at an interval of 3 hours.
    # we need 8 data points (intervals) for one day (24 hours)
    # we got 5 days, that mean 8*5 = 40 observations.
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))
