import requests
import sys
import re

def weather(query):
    try:
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b8aaa2e74c5e9ba9f1cf5b4e060789dc&units=metric');
        return res.json()
    except:
        print("error")


''' Function: print_weather
This function just prints the forecast
Parameters
----------
result : JSON
   Gets the Json response from api.
city : TEXT or INT
    Gets the city name or the zip code.

Returns
-------
None.

'''

def print_weather(weatherdata,city):
    try:
    	print("{}'s temperature: {}°F ".format(city,(weatherdata['main']['temp']*(9/5)+32)))
    	print("Details: {}".format(weatherdata['weather'][0]['description']))
    	print("Weather: {}".format(weatherdata['weather'][0]['main']))
    except:
        print("Incorrect city entered")


''' Function: main
    Returns
    -------
    None.
'''

def main():
    city=input('Enter the name of the city:')
    print()
    try:
        zipcode = int(city)
        if len(str(zipcode)) == 5:
             qparam='q='+city;
             wresp=weather(qparam);
             print_weather(wresp, city)
        else:
             print("Incorrect zipcode. Please re-enter the valid data.")
    except ValueError:
         try:
             
             if len(city) > 1:
                 if re.match("^[a-zA-Z]*$", city):
                     qparam='q='+city;
                     wresp=weather(qparam);
                     print_weather(wresp, city)
                 elif not re.match("^[a-zA-Z0-9]*$", city):
                     print("Special characters not allowed")
                 elif re.match("^[a-zA-Z0-9]*$", city):
                     print("Alpha-numeric data is not allowed")
             else:
                 print("You have not entered anything. Please enter city details. ")

         except ValueError:
             print("This is not a Zip code or City name. Please enter a valid input")             
      
if __name__=='__main__':
    while True:
        main()
        check=input("Do you want to continue? Enter y or n :")
        
        if check.lower() !="y":
            print("Exiting. Have a great day!")
            sys.exit()
        
