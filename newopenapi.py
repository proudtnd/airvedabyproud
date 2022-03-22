import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from typing import Any, Dict, Optional, Tuple

REFRESH_TOKEN_API = 'api/token/refresh/'
TOKEN_API = 'api/token/' 
        
class AirvedaOpenAPI :
    #  openapi = Airveda_Control(ENDPOINT, ACCESS_EMAIL, ACCESS_PASS)
    def __init__(
        self,
        API_ENDPOINT : str,
        ACCESS_EMAIL : str,
        ACCESS_PASS : str
                 ):
        self.session = requests.session()
        
        self.endpoint = API_ENDPOINT
        self.email = ACCESS_EMAIL
        self.secret = ACCESS_PASS
    
    def __request(
        self,
        method: str, # get post
        path: str, # after endpoint
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers : Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        
        # headers = {'Authorization':'Bearer '+ idToken }
        response = self.session.request(
            method, self.endpoint + path, params, body, headers=headers
        )
        result = response.json()
        return result
    
    def connect(
        self,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        result = self.__request("POST",TOKEN_API, params, [('email', self.email), ('password', self.secret)])
        global idToken
        global refreshToken
        idToken = result['idToken']
        refreshToken = result['refreshToken']
        return  'idToken = '+ idToken
    
    def post(
        self,
        path:str,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
    ):
        Headers = {'Authorization':'Bearer '+ idToken }
        result = self.__request("POST",path,params, body, headers= Headers)
        return result
    
    def get(
        self,
        path:str,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
    ):
        Headers = {'Authorization':'Bearer '+ idToken }
        result = self.__request("GET",path,params,body, headers=Headers)
        return result
    
    def plot(
        self,
        data:Optional[Dict[str, Any]] = None,
    ):
        # datatLasthour = self.post("POST",path,params, body)
        result_list= data['data']
        result_len = len(data['data'])
        pm25 = [] 
        pm10 = []
        aqi = []
        co2 = []
        temp = []
        hum = []
        time = []
        time_m = []
        for i in range(0,result_len, 2):
            a = dict(result_list[i])
            pm25.append(a['pm25'])
            pm10.append(a['pm10'])
            aqi.append(a['aqi'])
            co2.append(a['co2'])
            temp.append(a['temperature'])
            hum.append(a['humidity'])
            time.append(a['time'])
            time_m.append(i/2)

        # Prepare the data
        t = np.array(time_m)
        y1 = np.array(pm25)
        y2 = np.array(co2)
        y3 = np.array(pm10)
        y4 = np.array(aqi)
        fig, (axs1,axs2) = plt.subplots(2)
        # Plot the data
        axs2.plot(t, y1, label = 'pm25')
        axs2.plot(t, y3, label = 'pm10')
        axs2.plot(t, y4, label = 'aqi')
        axs1.plot(t, y2, label = 'co2')
        # Add a legend
        axs1.legend()
        axs1.set(xlabel = 'time [m]',ylabel = 'Co2' )
        axs1.grid()
        # axs1.('Co2')

        axs2.legend()
        axs2.set(xlabel = 'time [m]', ylabel = 'multiple of value' )
        axs2.grid()
        # axs2.ylabel('multiple of value')

        plt.suptitle('Life and environment in Proud\'s home in 1 hour')

        # Show the plot
        return plt.show()
