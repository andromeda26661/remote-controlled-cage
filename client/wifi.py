import network
import conf
import time
import error
network_list = conf.settings.network_list()

def host():
    #turn off wifi
    ap = network.WLAN(network.AP_IF)
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    ssid = "cage " + mac
    ap.active(True)
    ap.config(essid=ssid)

def connect(ssid):
    #connect to wifi and turn off error led
    #if it fails setup a wifi network with the mac addr for reconfig
    #networks is for all wifi network usernames/ssids
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
    print("connecting to wifi")
    error.on()
    try:
        isconnected = False
        i = 5
        length = len(network_list)
        passwords = conf.settings.passwords()
        if not bool(isconnected):
            for attempt in range(5):
                for x in range(length):
                    print(f"trying: {ssid}, {passwords[x]}")
                    sta_if.connect(ssid, passwords[x])
                    i = i + 1
                    time.sleep(5)  
                    isconnected = sta_if.isconnected()
            
    except:
        time.sleep(5)
        if not bool(sta_if.isconnected):
            print("Could not connect to wifi! making wifi for reconfig")
            conf.settings.config()
    return(sta_if.isconnected())

#scan for networks at all times 
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
if not bool(sta_if.isconnected()):
    buf = sta_if.scan()
    i = 0
    for data in buf:
        y = data[0].decode("ASCII")
        length = len(network_list)
        for x in range(length):
            if y == network_list[x]:
                connect(network_list[x])
