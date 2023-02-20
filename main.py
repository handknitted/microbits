import time

from libs.ssd1306 import initialize, clear_oled
from libs.ssd1306_bitmap import show_bitmap
from libs.ssd1306_text import add_text

initialize()
clear_oled()
show_bitmap("libs/microbit_logo")
time.sleep(5)
clear_oled()
add_text(0, 2, "Hello, world")