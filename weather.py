import requests

def get_desc_and_temp():
    api_key = "9722baba4f7af43dc75fdb06a1de1bf2"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format("Dallas", api_key)

    request = requests.get(url)
    json = request.json()
    #print(json)

    desc = json.get("weather")[0].get("description")
    temp_min = int(json.get("main").get("temp_min"))
    temp_max = int(json.get("main").get("temp_max"))
    city = json.get("name")
    return {"description": desc, "temp_min": temp_min, "temp_max": temp_max, "city": city}

def main():
    #Results
    weather_dict = get_desc_and_temp()
    print("[{} Weather Information]".format(weather_dict.get("city")))
    print("Today's forecast: {}".format(weather_dict.get('description')))
    print("Minimum temperature: {}".format(weather_dict.get('temp_min')))
    print("Maximum temperature: {}".format(weather_dict.get('temp_max')))


main()
