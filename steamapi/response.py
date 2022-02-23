import requests, math
import constants

key = constants.STEAM_API_KEY

def playtime(id: int):
    response = requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&format=json&input_json={{"steamid":{id}, "appids_filter": [1599340]}}')
    test = response.json()
    playtime = test["response"]["games"][0]["playtime_forever"]
    return math.trunc(playtime / 60)
