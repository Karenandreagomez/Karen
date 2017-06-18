#import requests. 
import requests

def requestSummonerData(region, summonerName, APIKey):

    #URL
    
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    print (URL)
    #requests.get . It basically goes to the URL we made and gives us back a JSON. Basicamente va a la URL creada y nos devuelve un JSON.
    response = requests.get(URL)
    #Retorna el JSON.
    return response.json()

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    print (URL)
    response = requests.get(URL)
    return response.json()
    

def main():
    print ("\Digita tu region para comenzar")
    print ("Digita una de las siguientes regiones, de lo contrario el programa no funcionara:\n")
    print ("NA EUW EUNE LAN BR KR LAS OCE TR RU PBE\n")

    #Se le pregunta al usuario tres cosas, la region, el nombre de invocador, y el API key.
    #Solo se necesitan esas tres cosas en ese orden para crear la URL y poder obtener el ID.

    region = (str(input('Digita una de las regiones: ')))
    summonerName = (str(input('Escribe tu nombre de invocador y NO INCLUYAS ESPACIOS NI MAYUSCULAS: ')))
    APIKey = (str(input('Copia y pega tu API key aqui: ')))

    #Devuelve un JSON.
    responseJSON  = requestSummonerData(region, summonerName, APIKey)
    
    ID = responseJSON[summonerName]['id']
    ID = str(ID)
    print (ID)
    responseJSON2 = requestRankedData(region, ID, APIKey)
    print (responseJSON2[ID][0]['tier'])
    print (responseJSON2[ID][0]['entries'][0]['division'])
    print (responseJSON2[ID][0]['entries'][0]['leaguePoints'])

#Comienza el programa!
if __name__ == "__main__":
    main()

