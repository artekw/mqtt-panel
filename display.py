from ht1632cpy import HT1632C

interface = HT1632C(2, 0)
interface.pwm(15)

def displayText(x, text):
    interface.clear()

    for c in text:
        interface.putchar(x, 4, c, interface.font6x8, interface.GREEN, interface.BLACK)
        x += interface.fontwidth(interface.font6x8)
    interface.sendframe()