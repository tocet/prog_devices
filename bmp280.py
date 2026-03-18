import time as t
import board
import busio
import adafruit_bmp280 as bmp

i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = bmp.Adafruit_BMP280_I2C(i2c, address = 0x76)

bmp280.sea_level_pressure = 1013.25

while True:
    temp_c = bmp280.temperature
    press_hpa = bmp280.pressure
    
    print(f'Temperature = {temp_c:.2f} degC')
    print(f'Pressure = {press_hpa:.2f} hPa')
    t.sleep(2)