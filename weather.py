import requests

api_key = "9722baba4f7af43dc75fdb06a1de1bf2"
city = "Dallas"
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(city, api_key)

request = requests.get(url)
json = request.json()
#print(json)

desc = json.get("weather")[0].get("description")
temp_min = int(json.get("main").get("temp_min"))
temp_max = int(json.get("main").get("temp_max"))

print("[{} Weather Information]".format(city))
print("Today's forecast: {}".format(desc))
print("Minimum temperature: {}".format(temp_min))
print("Maximum temperature: {}".format(temp_max))
