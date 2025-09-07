from restApi import api_request

def weather_api(lat="51.5085", lng="-0.1257", hourly="temperature_2m", models = "kma_seamless"):

    params = {
    "latitude":lat,
    "longitude":lng,
    "hourly": hourly,
    "models": models,
    }
    url = "https://api.open-meteo.com/v1/forecast"
    resp = api_request(url=url,params=params)
    if resp:
        hourly_weather_info = resp.get("hourly")
        times = hourly_weather_info.get("time")
        temperature = hourly_weather_info.get("temperature_2m")
        if len(times) == len(temperature):
            final_resp = list(zip(times, temperature))
            final_resp = sorted(final_resp, key=lambda x: x[0])
            print(final_resp)
        else:
            ValueError("time and weather are not equal")
    else:
       raise ValueError("no response")

weather_api()