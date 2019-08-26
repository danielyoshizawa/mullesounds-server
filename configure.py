import json

soundsPath = input("Diretorio das midias : ")
print(soundsPath)

networkAddress = input("Endereco da rede : ")
print(networkAddress)

networkPort = input("Porta da rede : ")
print(networkPort)

js = {
    "soundsPath" : soundsPath,
    "networkAddress": networkAddress,
    "networkPort" : networkPort
}

print(json.dumps(js))

configFile = open("./config/configuration.txt", "w+")
configFile.write(json.dumps(js))
configFile.close()
