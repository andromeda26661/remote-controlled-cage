import machine
import uasyncio as asyncio 
#varibles
led = machine.Pin(32, machine.Pin.OUT) #red led to show errors

def on():
    #turn error led on
    led.value(1)

def off():
    #turn error led off
    led.value(0)
    
def flashing(time):
    #time in ms
    async def bar():
        on()
        await asyncio.sleep(time/1000)  # Pause for time value
        off()
        await asyncio.sleep(time/1000)  # Pause for time value
    asyncio.run(bar())
