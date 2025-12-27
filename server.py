from socket import socket_conn
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from control import GameController
from config import I2C_SDA_PIN, I2C_SCL_PIN, OLED_ADDR, BUTTON1_PIN, BUTTON2_PIN


controller = GameController(button1_pin=BUTTON1_PIN, button2_pin=BUTTON2_PIN)
i2c = SoftI2C(sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN))
oled = SSD1306_I2C(128, 64, i2c, addr=OLED_ADDR)
oled.font_load("GB2312-12.fon")
oled.fill(0)

SERVER_IP = '106.15.108.125'
SERVER_PORT = 1234
MESSAGE = ["给我说一个笑话","今天的天气是什么？","最近有什么好吃的？","今天的新闻","查询我的邮件！"]


def screen_text(text, x=20,y=15):
    oled.fill(0)
    oled.text(text, x, y)
    oled.show()


def decide_msg(MESSAGE):
    msg = 0
    while True:
        action = controller.get_action()
        if action == 11:
            msg = msg + 1
        elif action == 21:
            msg = msg - 1
        elif action == 23:
            return MESSAGE[msg]
            break
        screen_text(MESSAGE[msg])
    

def socket_com(MESSAGE):
    ret = socket_conn(SERVER_IP, SERVER_PORT, MESSAGE)
    screen_text(str(ret))

def main_server(MESSAGE):
    res = decide_msg(MESSAGE)
    socket_com(res)

# main_server(MESSAGE)
