#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

sdpserver_address = "http://127.0.0.1:5000/"
faf_ice_adapter_address = "http://127.0.0.1:8080/"

my_host_id=1234

r = requests.get(sdpserver_address + "get_games")
print(r.json())

r = requests.get(sdpserver_address + "create_game/" + str(my_host_id))
print(r.text)

r = requests.get(sdpserver_address + "get_games")
games = r.json()
if (len(games) < 1):
  exit(1)
first_game_id = next(iter(games))

print("joining game", first_game_id)

r = requests.get(faf_ice_adapter_address + "join_game",
                 params={"game_id": first_game_id})
print(r.text)
