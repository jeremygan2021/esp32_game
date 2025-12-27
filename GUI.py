from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from config import I2C_SDA_PIN, I2C_SCL_PIN, OLED_ADDR
import time

class OLEDDrawer:
    def __init__(self, width, height, i2c, addr):
        self.oled = SSD1306_I2C(width, height, i2c, addr=addr)
        self.oled.font_load("GB2312-12.fon")
        self.width = width
        self.height = height

    def clear(self):
        self.oled.fill(0)

    def show(self):
        self.oled.show()

    def draw_icon(self, x=0, y=0, nub=1):
        heart = [
            0b01100110,
            0b10011001,
            0b10000001,
            0b10000001,
            0b01000010,
            0b00100100,
            0b00011000,
            0b00000000
        ]
        sword = [
            0b00010000,
            0b00111000,
            0b00111000,
            0b00111000,
            0b00111000,
            0b01111110,
            0b00011000,
            0b00111100
        ]
        
        draw = heart if nub == 1 else sword
        
        for i, line in enumerate(draw):
            for j in range(8):
                if line & (1 << (7-j)):
                    self.oled.pixel(x + j, y + i, 1)

    def draw_border_with_texture(self):
        self.oled.rect(0, 0, self.width, self.height, 1)
        for i in range(0, self.width, 4):
            self.oled.line(i, self.height-1, i + 2, self.height-3, 1)

    def draw_power_bar(self, x, y, width, height, power):
        self.oled.rect(x, y, width, height, 1)
        self.oled.fill_rect(x, y, min(power, width), height, 1)

    def draw_power_squares(self, x, y, power):
        for i in range(10):
            if i * 8 < power:
                self.oled.fill_rect(x + i*8, y, 6, 7, 1)
            else:
                self.oled.rect(x + i*8, y, 6, 7, 1)

    def draw_text(self, text, x, y):
        self.oled.text(text, x, y)

class DisplayPage:
    def __init__(self, drawer):
        self.drawer = drawer

    def update(self, power_a, power_b):
        self.drawer.clear()
        self.drawer.draw_border_with_texture()
        self.draw_content(power_a, power_b)
        self.drawer.show()

    def draw_content(self, power_a, power_b):
        raise NotImplementedError("Subclasses must implement draw_content method")

class FightPointsPage(DisplayPage):
    def draw_content(self, power_a, power_b):
        self.drawer.draw_icon(115, 5, 2)
        self.drawer.draw_text("战斗力对比", 5, 5)
        self.drawer.draw_text('宋: {}'.format(power_a), 5, 25)
        self.drawer.draw_text('金: {}'.format(power_b), 5, 45)
        self.drawer.draw_power_squares(44, 27, power_a)
        self.drawer.draw_power_squares(44, 47, power_b)

class HealthPointsPage(DisplayPage):
    def draw_content(self, power_a, power_b):
        self.drawer.draw_icon(115, 5, 1)
        self.drawer.draw_text("双方国力对比", 5, 5)
        self.drawer.draw_text('宋: {}'.format(power_a), 5, 25)
        self.drawer.draw_text('金: {}'.format(power_b), 5, 45)
        self.drawer.draw_power_bar(44, 27, 80, 7, power_a)
        self.drawer.draw_power_bar(44, 47, 80, 7, power_b)

def main():
    i2c = I2C(scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN))
    drawer = OLEDDrawer(128, 64, i2c, addr=OLED_ADDR)
    fight_page = FightPointsPage(drawer)
    health_page = HealthPointsPage(drawer)

    power_a = 50
    power_b = 75
    health = 100

    while True:
        fight_page.update(power_a, power_b)
        time.sleep(2)
        health_page.update(power_a, power_b)
        time.sleep(2)
        health += 1
        if health > 100:
            health = 50

if __name__ == '__main__':
    main()
