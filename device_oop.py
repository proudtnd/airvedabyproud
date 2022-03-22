from newopenapi import (
    AirvedaOpenAPI
)
# set up
ACCESS_EMAIL = "YOUR_EMAIL" 
ACCESS_PASS = "YOUR_PASSWORD" 
API_ENDPOINT = "https://dashboard.airveda.com/"

LASTEST_DATA = 'api/data/latest/'
LAST_HOUR_DATA = 'api/data/last-hour/'
DEVICE_DETAIL = 'api/data/devices/'

# Set up device_id
DEVICE_ID ="YOUR_DEVICE_ID" 
        
param = ''     
openapi = AirvedaOpenAPI(API_ENDPOINT, ACCESS_EMAIL, ACCESS_PASS)
b = openapi.connect()
# print(b)

# lastest data

c = openapi.post('api/data/latest/',param, [('deviceIds', DEVICE_ID)])
# print(c)

# last hour data
d = openapi.post('api/data/last-hour/',param, [('deviceId', DEVICE_ID)])
print(d)
f = openapi.plot(d)
# print(f)

# info every device
e = openapi.get('api/data/devices/')
# print(e)
