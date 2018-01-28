from gpiozero import LightSensor

ldr = LightSensor(17, charge_time_limit=0.7 ,threshold=0.5)

def getLight():
    return ldr.light_detected