import pyowm

#https://openweathermap.org/appid

myOwn = pyowm.OWM("dbf6aaf008f3591e4eeb64257fd2d985")

location = 'Bergen, Norway'

myWeather = myOwn.weather_at_place(location)

print(myWeather)
print(myWeather.get_weather().get_wind())
print(myWeather.get_weather().get_temperature())
print(myWeather.get_weather().get_humidity())


