import adafruit_sgp30
from machine import I2C, Pin
import time


sdaPIN=machine.Pin(16)
sclPIN=machine.Pin(17)
i2c_1=machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=40000)
sgp = adafruit_sgp30.Adafruit_SGP30(i2c_1, address=0x58)




while True:

    co2eq, tvoc = sgp.iaq_measure()
    if co2eq == 400:
        print("initializing mdodule")

    else:
        while True:
            try:
                co2eq, tvoc = sgp.iaq_measure()
                print("CO2 concentration = %d ppm \t TVOC = %d ppb" % (co2eq, tvoc))
                
                csv=open("data.csv","at")
                csv.write(f"{co2eq},{tvoc}\n")
                csv.close()
                
                time.sleep(0.05)
            except OSError as e:
                pass
