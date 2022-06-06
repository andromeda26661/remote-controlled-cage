import network
import sys
import ubinascii
import time
import wifi
import machine
#you should only need to edit the top of this file if you edit other parts your device may not function properly
#password is for the passwords of the ssid Note! the password has to be the same array number as the ssid
networks = [""]
password = [""]

# storage for passwords and device hashes
class settings:

    #class for storing wifi and device settings
    #networks is for all wifi network usernames/ssids
    #password is for the passwords of the ssid Note! the password has to be the same array number as the ssid

    def __init__(self):
        pass
    
    def network_list():
        return(networks)
    
    def passwords():
        return(password)

    def config():
        #reconfig mode
        print("In configuration mode please connect to a computer or phone")
        wifi.host()



