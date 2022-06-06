#all required modules for boot (why do i have to have the ones here for the other scritps when im not using it)
import wifi
import machine
import sys
import os
import webrepl
import conf
import error
from conf import settings
led2 = machine.Pin(33, machine.Pin.OUT) #blue red for testing
#turn on led during bootup
led2.value(1)
#force reconfigeration button
forceconfig = machine.Pin(35, machine.Pin.IN)
#check if config excist 
execfile("error.py")
try:
    execfile("conf.py")
except:
    #setup recovery mode/first time setup
    settings.config()

if not forceconfig.value():
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
    error.on()
    if bool(sta_if.isconnected):
            print("Connected to wifi")
            error.off()
    debug = True #hidden dev mode UwU
    if bool(debug):
        webrepl.start()
else:
    settings.config()