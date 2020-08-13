# Import modules
import time
from RPLCD.i2c import CharLCD
from typing import List

from uptime_ip import get_uptime_ip
import cpu_mem_tmp_du
from docker_stats import docker_stats
# Define page display time
waitTime = 5

lcd = CharLCD('PCF8574', 0x3f)

progress_start = (
    0b01111,
    0b11000,
    0b10000,
    0b10000,
    0b10000,
    0b10000,
    0b11000,
    0b01111,
)
progress1 = (
    0b01111, 
    0b11000,
    0b10011,
    0b10111,
    0b10111,
    0b10011,
    0b11000,
    0b01111
)
progress2 = (
    0b11111, 
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b11111
)
progress3 = (
    0b11111, 
    0b00000,
    0b11000,
    0b11000,
    0b11000,
    0b11000,
    0b00000,
    0b11111
)
progress4 = (
    0b11111, 
    0b00000,
    0b11011,
    0b11011,
    0b11011,
    0b11011,
    0b00000,
    0b11111
)
progress5 = (
    0b11110, 
    0b00011,
    0b00001,
    0b00001,
    0b00001,
    0b00001,
    0b00011,
    0b11110
)

progress_end = (
    0b11110,
    0b00011,
    0b11001,
    0b11101,
    0b11101,
    0b11001,
    0b00011,
    0b11110,
)

def setup_progressbar_chars():
    lcd.create_char(0, progress_start)
    lcd.create_char(1, progress1)
    lcd.create_char(2, progress2)
    lcd.create_char(3, progress3)
    lcd.create_char(4, progress4)
    lcd.create_char(5, progress5)
    lcd.create_char(6, progress_end)
def get_progress_bar_chars(percent: int):
    chars: List[str] = []
    for i in range(10):
        if(i == 0):
            if(percent > 0):
                chars.append('\x01')
            else:
                chars.append('\x00')

        elif (i == 9):
            if(percent > 90):
                chars.append('\x06')
            else:
                chars.append('\x05')
        
        else:
            if(percent > (i*10) + 5):
                chars.append('\x04')
            elif(percent > (i*10)):
                chars.append('\x03')
            else:
                chars.append('\x02')
    return ''.join(chars)

try:
    setup_progressbar_chars()
    lcd.clear()
    # Loop forever
    while True:
        display_array = []
        mem = cpu_mem_tmp_du.get_mem()
        cpu = cpu_mem_tmp_du.get_cpu()
        temp = cpu_mem_tmp_du.get_temp()
        du = cpu_mem_tmp_du.get_du()
        display_array.append(get_uptime_ip())
        display_array.append(["Memory", get_progress_bar_chars(mem) + ' ' + str(mem) + '%'])
        display_array.append(["CPU - All", get_progress_bar_chars(cpu) + ' ' + str(cpu) + '%'])
        display_array.append(["Disk Usage", get_progress_bar_chars(du) + ' ' + str(du) + '%'])
        display_array.append(["Temperature", get_progress_bar_chars(temp) + ' ' + str(temp) + 'C'])
        display_array.extend(docker_stats())
        # Each page
        for display_item in display_array:
            lcd.clear()
            lcd.write_string(display_item[0] + '\r\n'+ display_item[1])
            time.sleep(waitTime)

# Handle exceptions
except Exception as e:
    print("Error : " + str(e))
    lcd.clear()
