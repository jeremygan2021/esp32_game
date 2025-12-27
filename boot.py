from machine import SoftI2C, Pin
from ssd1306 import SSD1306_I2C
from wifi import connect_wifi

import time
from image import display_image, tangledup_ai_logo
from control import GameController
from page import page_control

controller = GameController(button1_pin=0, button2_pin=25)


i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)
oled.font_load("GB2312-12.fon")
oled.fill(0)


SERVER_IP = '106.15.108.125'
SERVER_PORT = 1234
MESSAGE = '这里是单片机'



def screen_fill():
    oled.fill(0)
    oled.show()


def screen_text(text:str, x=20,y=15):
    oled.fill(0)
    oled.text(text, x, y)
    oled.show()

def screen_text_change(text: str, x=5, y=10, max_chars_per_line=10, line_spacing=18):
    oled.fill(0)
    chars_written = 0
    current_line = ""
    
    for char in text:
        # Check if we need to wrap to the next line
        if chars_written >= max_chars_per_line or char == '\n':
            oled.text(current_line, x, y)
            y += line_spacing  # Increase y by line_spacing for the next line
            current_line = ""
            chars_written = 0
        
        if char != '\n':
            current_line += char
            chars_written += 1
    
    # Print any remaining text
    if current_line:
        oled.text(current_line, x, y)
    
    oled.show()


def start_wifi(SSID, PASSWORD):
    res = connect_wifi(SSID, PASSWORD)
    text = str(SSID)
    if res:
        screen_fill()
        oled.text("连接成功！", 20, 15)
        oled.text("网络名称:" + text, 5, 35)  # 修改这一行
        oled.show()
        time.sleep(5)
        screen_fill()
        return True
    else:
        screen_fill()
        oled.text("连接失败", 20, 15)
        oled.show()
        time.sleep(5)
        screen_fill()
        return False
    
def game_control():
    while True:
        action = controller.get_action()
        if action:
            if action == 11:
                print("1键单击")
            elif action == 12:
                print("1键双击")
            elif action == 13:
                print("1键长按")
            elif action == 21:
                print("2键单击")
            elif action == 22:
                print("2键双击")
            elif action == 23:
                print("2键长按")       
        time.sleep(0.1)



def main(SSID, PASSWORD):
    led = Pin(2, Pin.OUT)  # ESP32板载LED，通常在GPIO2上
    while True:
        led.value(not led.value())  # 切换LED状态
        time.sleep(0.5)  # 等待0.5秒
        if start_wifi(SSID, PASSWORD) is True:
            # 调用连接函数
            screen_text_change("欢迎来叠加态智能终端")
            time.sleep(3)
            screen_fill()
            display_image(oled,tangledup_ai_logo)
            time.sleep(3)
            screen_fill()
            screen_text_change("》点击任意按键开始《")
            page_control(oled, controller)
            break
        else:
            screen_text_change(" 连接失败!")
            start_wifi(SSID, PASSWORD)


        

if __name__ == '__main__':
#     game_control()
    main("QSGJ_2.4", "qjgj332211")