from sense_emu import SenseHat
import time


#
# Raspberry Pi's Sensor initialization
sense = SenseHat()


#
# Execution loop
while True:
    print("Temperatura:", sense.temperature,
            "; Pressão:", sense.pressure,
            "; Umidade:", sense.humidity)
    time.sleep(4)
