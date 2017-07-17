import datetime
import time

from ht1632cpy import HT1632C

interface = HT1632C(2, 0)
interface.pwm(15)

def displayText(x, text, text_color, bg_color, delay):
    interface.clear()

    if text_color == 'text_green':
        c_text = interface.GREEN
    elif text_color == 'text_red':
        c_text = interface.RED
    elif text_color == 'text_orange':
        c_text = interface.ORANGE
    elif text_color == 'text_black':
        c_text = interface.BLACK

    if bg_color == 'bg_green':
        c_bg = interface.GREEN
    elif bg_color == 'bg_red':
        c_bg = interface.RED
    elif bg_color == 'bg_orange':
        c_bg = interface.ORANGE
    elif bg_color == 'bg_black':
        c_bg = interface.BLACK

    if c_text == c_bg:
        c_text = interface.GREEN
        c_bg = interface.BLACK
    
    if not text_color:
        c_text = interface.GREEN
    
    if not bg_color:
        c_bg = interface.BLACK
    
    interface.box(0, 0, interface.width(), interface.height(), c_bg)
    for c in text:
        
        interface.putchar(x, 4, c, interface.font6x8, c_text, c_bg)
        x += interface.fontwidth(interface.font6x8)
    interface.sendframe()
    time.sleep(float(delay))

def clock():
    now = datetime.datetime.now()
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    interface.clear()

    x = 5
    dividers = 2
    for section in (hour, minute, second):
        for c in section:
            interface.putchar(x, 4, c, interface.font7x8num, interface.GREEN, interface.BLACK)
            x += interface.fontwidth(interface.font7x8num)
        if dividers > 0:
            interface.putchar(x, 4, ':', interface.font6x8, interface.GREEN, interface.BLACK)
            x += interface.fontwidth(interface.font6x8) - 1
            dividers -= 1
    interface.sendframe()