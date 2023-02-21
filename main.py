import time
from microbit import *
import math

from ssd1306 import initialize, clear_oled
from ssd1306_bitmap import show_bitmap
from ssd1306_text import add_text

display.off()

leeway = 50
initialize()
clear_oled()
show_bitmap("microbit_logo")
time.sleep(1)
clear_oled()
add_text(0, 2, "Input:")
while True:
    control_value = pin2.read_analog()
    power_level = int(math.fabs(control_value - (1023/2)) * 2)
    add_text(8, 0, str(control_value) + '   ')

    add_text(8, 1, str(power_level) + '   ')
    pin8.write_analog(power_level)
    add_text(0, 3, "Pulse:" + str(pin8.get_analog_period_microseconds()))

    if control_value > (1023/2) + leeway:
        # forward motor
        add_text(0, 2, "Forward")
        pin6.write_digital(1)
        pin7.write_digital(0)
    elif control_value < (1023/2) - leeway:
        add_text(0, 2, "Reverse")
        pin6.write_digital(0)
        pin7.write_digital(1)
    else:
        add_text(0, 2, "Stop   ")
        pin6.write_digital(0)
        pin7.write_digital(0)