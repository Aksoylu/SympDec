#-- SympDec API (Machine Learning/Sound Processing Server)--
# Author      : Umit Aksoylu
# Date        : 22.11.2021
# Description : An API Example for Symptom Detection Analyze Server
# Website     : http://umit.space
# Mail        : umit@aksoylu.space
# Github      : https://github.com/Aksoylu

import requests
import json
API_URL = "https://covid.aksoylu.space/API/PROCESS"
API_KEY = "" ### PLACE YOUR API KEY HERE !###

def justSoundAnalyze(path):
    r = requests.post(API_URL, verify=False, 
        data={  'apiKey' : API_KEY,
                
        }, 
        files={ 'audio_file' : open(path, 'rb')

        }
    )

    return r.text


def analyzeWithCoordinates(path, coordinates):
    r = requests.post(API_URL, verify=False, 
        data={  'apiKey' : API_KEY,
                'LAT' : coordinates['lat'],
                'LON' : coordinates['lon']
                
        }, 
        files={ 'audio_file' : open(path, 'rb')

        }
    )

    return r.text


filePath = "ExampleData/positive1.wav"
analyzeResult = justSoundAnalyze(filePath)
analyzeResult = json.dumps(analyzeResult)
print("="*5,"Analyze for following sound file : ",filePath , "="*5)
print(analyzeResult)
print("="*10)


filePath = "ExampleData/negative1.wav"
location = {'lat' :"41.003215", 'lon': "29.092704"} # Istanbul, Atesehir Coordinates 

anotherAnalyzeResult = analyzeWithCoordinates(filePath, location)

print("="*5,"Analyze for following sound file : ",filePath , "="*5)
print(anotherAnalyzeResult)
print("="*10)

