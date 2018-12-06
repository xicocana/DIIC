# importing the requests library 
import requests, time

interval = 10 #seconds
  
# api-endpoint 
URL = "http://maps.googleapis.com/maps/api/geocode/json"
  
# location given here 
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
params = {'location':location} 
  
while True:
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = params) 
    
    # extracting data in json format 
    data = r.json() 
    
    # extracting latitude, longitude and formatted address  
    # of the first matching location 
    loc = data['results'][0]['location']
    
    # printing the output 
    print("Location: " + loc) 

    time.sleep(interval)
    