from playsound import playsound
from os import listdir
from os.path import isfile, join
import json
import sys

# Data structure for Configurations
class Config:
    path = ""

class Player:
    def __init__(self):
        self.refreshSoundList()

    # Loads the configuration file
    def loadConfigFile(self):
        obj = None
        try:
            configFile = open("./config/configuration.txt")
            js = configFile.read()
            obj = json.loads(js)
            print(obj["networkAddress"])
            print(js)
            configFile.close()
            config = Config()
            config.path = obj["soundsPath"]
            return config
        except OSError:
            print("Arquivo de configuracao nao encontrado")
            sys.exit(1)
        except IOError:
            print("Não foi possivel ler o arquivo de configuração")
            sys.exit(1)


    # Loads the list of sounds
    def loadSoundList(self, path):
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

    def play(self, path, file):
        playsound(join(path,file))

    # Refreshs the list of Sounds
    def refreshSoundList(self):
        config = self.loadConfigFile()
        self.loadSoundList(config.path)
