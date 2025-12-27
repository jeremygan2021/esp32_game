from machine import I2C, Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import utime
from control import GameController
from func_image import GPT_app, function, server ,data
from server import main_server
from config import I2C_SDA_PIN, I2C_SCL_PIN, OLED_ADDR, BUTTON1_PIN, BUTTON2_PIN

controller = GameController(button1_pin=BUTTON1_PIN, button2_pin=BUTTON2_PIN)
i2c = SoftI2C(sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN))
oled = SSD1306_I2C(128, 64, i2c, addr=OLED_ADDR)
oled.font_load("GB2312-12.fon")
oled.fill(0)

def display_image(oled, img, text):
    oled_width = 128
    oled_height = 64
    for y in range(oled_height // 8):
        for x in range(oled_width):
            oled.buffer[y * oled_width + x] = img[y * oled_width + x]
    oled.text(text, 0, 28)  # 假设文字显示在左上角，你可以根据需要调整位置
    oled.show()

# 平滑滑动类
class SmoothSlider:
    def __init__(self,pages):
        self.pages = pages
        self.current_page = 0
        self.target_page = 0
        self.offset = 0
        self.speed = 8  # 调整这个值来改变滑动速度
        self.oled = oled

    def slide_to(self, page):
        self.target_page = page
        while self.current_page != self.target_page:
            if self.current_page < self.target_page:
                self.offset -= self.speed
                if self.offset <= -128:
                    self.offset = 0
                    self.current_page += 1
            else:
                self.offset += self.speed
                if self.offset >= 128:
                    self.offset = 0
                    self.current_page -= 1
            self.draw()
            utime.sleep_ms(16)  # 约60fps
        # 滑动结束后显示 GPT_app 和当前页面文字
        self.draw_image_with_text(self.current_page)
        return self.current_page

    def slide_left(self):
        page = self.slide_to((self.current_page - 1) % len(self.pages))
        return page

    def slide_right(self):
        page = self.slide_to((self.current_page + 1) % len(self.pages))
        return page

    def draw(self):
        oled.fill(0)
        x = self.offset
        # 当前页面
        self.oled.text(self.pages[self.current_page], x, 28)
        # 前一页面
        if x < 0 and self.current_page + 1 < len(self.pages):
            self.oled.text(self.pages[(self.current_page + 1) % len(self.pages)], x + 128, 28)
        # 后一页面
        elif x > 0 and self.current_page - 1 >= 0:
            self.oled.text(self.pages[(self.current_page - 1) % len(self.pages)], x - 128, 28)
        self.oled.show()

    def draw_image_with_text(self,pages):
        self.oled.fill(0)
        tag = server
        if pages == 0:
            tag = server
        elif pages == 1:
            tag = function
        elif pages == 2:
            tag = GPT_app
        elif pages == 3:
            tag = data
        # 显示当前页面的文字和 GPT_app 图片
        display_image(self.oled, tag, self.pages[self.current_page])

def into_page(page):
    if page == 0:
        print("服务终端")
        main_server()
    elif page == 1:
        print("fuction call")
    elif page == 2:
        print("GPT直连")
    else:
        print("data")


# 按键控制逻辑
def game_control(controller,slider):

    while True:
        action = controller.get_action()
        if action:
            if action == 11:
                print("1键单击 - 向左滑动")
                page = slider.slide_left()
            elif action == 21:
                print("2键单击 - 向右滑动")
                page = slider.slide_right()
            elif action == 23:
                print("进入当前页面" + str(page))
                #进入函数
                into_page(page)
            elif action == 13:
                print("退出")
                break
        utime.sleep(0.1)

    # 示例用法
def main_func(controller):

    pages = ["终端对话", "函数控制", "GPT直连", "数据展示"]
    slider = SmoothSlider(pages)
    slider.draw()
    slider.draw_image_with_text(0)
     #启动按键控制
    game_control(controller,slider)

# if __name__ == '__main__':
#     main_func(controller)

