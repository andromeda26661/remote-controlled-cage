import uasyncio  as asyncio
import json
import gc
import uping
import network
import error
from async_websocket_client import AsyncWebsocketClient

isinternet = False

async def bar():
    count = 0
    while True:
        count += 1
        try:
            if uping.ping("1.1.1.1") > 0:
                isinternet = True
            else:
                isinternet = False
        except:
            sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
            if bool(sta_if.isconnected):
                isinternet = False
            else:
                print("no wifi")
        await asyncio.sleep(60)  # Pause 1min
        
asyncio.run(bar())

if not bool(isinternet):
        print("no internet!!")
        error.flashing(250)

# create instance of websocket
ws = AsyncWebsocketClient(config['socket_delay_ms'])
