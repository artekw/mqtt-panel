# MQTT LED Panel

The goal is create message board to display clock and MQTT messages.
To create I use Raspberry Pi and HT1632c Sure Electronic LED Boards. 
LED matrix have 32x16 pixels.

![LED Board](https://github.com/artekw/mqtt-panel/blob/master/docs/board.jpg?raw=true)

## Connection

Using a Raspberry PI model B2, you need to connect some GPIO pins to the
LED BR1 port, the input port, like this:


| RPI Label      | Pin | SURE Label | Pin |
|----------------|-----|------------|-----|
| GND            | 6   | GND        | 8   |
| 5V             | 4   | 5V         | 16  |
| GPIO 10 (MOSI) | 19  | DATA       | 7   |
| GPIO 11 (SCLK) | 23  | WR         | 5   |
| GPIO 8  (CE0)  | 24  | CLK        | 2   |
| GPIO 7  (CE1)  | 26  | CS         | 1   |


## Instalation

- Clone

      git clone https://github.com/artekw/mqtt-panel.git

- Run

      python app.py

    
- Profit!
