import requests


# response = requests.get("https://samples.openweathermap.org/data/2.5/weather?q=Lagos,ng&appid=439d4b804bc8187953eb36d2a8c26a02")

# data = response.json()

# print(data["main"]["temp_max"])


api_key = "336b102582e7d317c464efd5e6ac86aa"
city_id = "2332453"

url = f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={api_key}"
print(url)
fetch = requests.get(f"{url}") # VISIT AND FETCH DATA FROM URL
data = fetch.json() #READ DATA FROM URL AS JSON (ALSO DICTIONARY IN PYTHON)

# print(data) # PRINT URL DATA GOTTEN FROM URL

# print(data.keys())

#  LIST KEY IS WHAT CONTAINS OUR DATA AS SEEN HENCE WE ACCESS IT VIA INDEX

forcasts = data["list"]

# print(type(forcasts)) # CHECK THE TYPE OF DATASTRUCTURE OUR FORCASTS COMES IN 

print("Date".center(25), "Weather".center(25), "Temperature".center(25), "Humidity".center(25), "Pressure".center(25), sep = "|")
for forcast in forcasts:
    # print(forcast)
    # print("-------------------------------------------------")
    # print("-------------------------------------------------")
    # print("-------------------------------------------------")
    # print("-------------------------------------------------")

    temp = forcast["main"]["temp_max"]
    pressure = forcast["main"]["pressure"]
    humidity = forcast["main"]["humidity"]
    weather_description = forcast['weather'][0]["description"]
    date = forcast["dt_txt"]

    print(str(date).center(25), str(weather_description).center(25), str(temp).center(25), str(humidity).center(25), str(pressure).center(25), sep = "|")