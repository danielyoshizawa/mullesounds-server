from playsound import playsound
from os import listdir
from os.path import isfile, join
import json

# Reading the configuration file
configFile = open("./config/configuration.txt")
js = configFile.read()

obj = json.loads(js)

print(obj["networkAddress"])

print(js)

configFile.close()

#path = '/Users/daniel/Documents/Development/Projects/mullesounds/sounds/'

path = obj["soundsPath"]

soundList = [f for f in listdir(path) if (isfile(join(path, f)) and (f.endswith(".mp4") or f.endswith(".wav")))]
print(soundList)

soundListJson = {"sounds" : []}

for soundName in soundList:
    soundStruct = {
        "Filename": soundName
    }
    print(json.dumps(soundStruct))
    soundListJson["sounds"].append(soundStruct)

print(json.dumps(soundListJson))

with open("./config/soundsList.txt", "w+") as writeFile:
    json.dump(soundListJson, writeFile)

def play(path, file):
    playsound(join(path,file))

for f in soundList:
    play(path,f)
