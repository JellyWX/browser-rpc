import rpc
import time
import json
import requests


client_id = '455298663598653446' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module

email = input('Please enter your email: ')

activity = {
    "state": "Not provided",
    "details": "Not provided",
    "timestamps": {
        "start": time.time()
    },
    "assets": {
        "small_text": "Not provided",
        "small_image": "small_image",
        "large_text": "Not provided",
        "large_image": "large_image"
    }
}

while True:

    r = requests.get('https://rpc.jellywx.co.uk/', json={'email' : email})

    activity.update(r.json)

    rpc_obj.set_activity(activity)

    time.sleep(15)
