import network
import webrepl
networks = [""]
password = [""]
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
i = 0
for ssid in networks:
    print(f"trying: {ssid}")
    sta_if.connect(ssid, password[i])
    i = i + 1

print("may have not connected yet but will enable webrepl")
webrepl.start()