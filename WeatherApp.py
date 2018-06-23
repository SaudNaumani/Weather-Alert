import json
import urllib
from twilio.rest import Client

#WeatherType = raw_input("Would you like Current Weather Data, or a 5 Day forecast; Please enter either 'current weather' or '5 day forecast'")
city = raw_input("Please enter a city: ")

CurrWeather_endpoint = "http://api.openweathermap.org/data/2.5/weather"
#Forecast_endpoint = "http://api.openweathermap.org/data/2.5/forecast/daily"
apiKey = "86fbce96f62946f56cdf25010a57440c"

CurrWeatherURL = CurrWeather_endpoint + "?q=" + city + "&appid=" + apiKey
Curr_response = urllib.urlopen(CurrWeatherURL)
parseResponse = json.loads(Curr_response.read())

#Parse JSON into and output meaningful data
Temperature = parseResponse['main']['temp']
Description = parseResponse['weather'][0]['description']
High = parseResponse['main']['temp_max']
Low = parseResponse['main']['temp_max']
#ForecastURL = Forecast_endpoint + "?q=" + city + "&appid=" + apiKey
print "Temperature: " + str(Temperature - 273.15) + " degrees C"
print "Weather: " + Description
print "High Of: " + str(High - 273.15) + " degrees C"
print "Low Of: " + str(Low - 273.15) + " degrees C"
print '\n'
print "For more info, visit: " + CurrWeatherURL

custom_Message = "The weather in " + city + "is " + str(Temperature - 273.15) + " degrees C with " + Description

# Twilio authentication codes
Account_sid = "ACcb957c08834b15aecea5cef20b9f3e21"
Auth_Token = "df88acf8c820264e2d15d0f530d74dc7"
client = Client(Account_sid, Auth_Token)# Twilio Client Object
#we can now use our twilio client object, and our number to make an api call
Text_Alert = client.messages.create(to = "+16475443657", from_ = "+15813334090", body = custom_Message)


