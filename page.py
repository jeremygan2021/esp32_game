from machine import SoftI2C, Pin
from ssd1306 import SSD1306_I2C
import time
from image import display_image, display_image_fast, tangled_page,song_page, AIpage, tangledup_ai_logo
from song_image import jingkang
from control import GameController
from function import main_func
from config import I2C_SDA_PIN, I2C_SCL_PIN, OLED_ADDR, BUTTON1_PIN, BUTTON2_PIN

controller = GameController(button1_pin=BUTTON1_PIN, button2_pin=BUTTON2_PIN)


i2c = SoftI2C(sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN))
oled = SSD1306_I2C(128, 64, i2c, addr=OLED_ADDR)
oled.font_load("GB2312-12.fon")
oled.fill(0)

display_image_fast(oled,AIpage)



def page_control(oled,controller):
    pages = [tangled_page, song_page, AIpage]
    current_page_index = 2  # Start with AIpage (index 2)
    
    def scroll_ai_page():
        for i in range(64):
            oled.scroll(0, -1)
            oled.show()
            time.sleep(0.01)
        display_image_fast(oled, AIpage)

    while True:
        action = controller.get_action()
        if action:
            if action == 11:  # 1键单击
                print("1键单击 - 向左切换页面")
                current_page_index = (current_page_index - 1) % len(pages)
                display_image_fast(oled, pages[current_page_index])
            elif action == 21:  # 2键单击
                print("2键单击 - 向右切换页面")
                current_page_index = (current_page_index + 1) % len(pages)
                display_image_fast(oled, pages[current_page_index])
            elif action == 13 or action == 23:  # 1键或2键长按
                print("长按 - 特殊动作")
                if pages[current_page_index] == song_page:
                    display_image_fast(oled, jingkang)
                elif pages[current_page_index] == tangled_page:
                    display_image_fast(oled, tangledup_ai_logo)
                    time.sleep(1.5)
                    main_func(controller) #载入
                    
                elif pages[current_page_index] == AIpage:
                    scroll_ai_page()
                    display_image_fast(oled, tangledup_ai_logo)
                else:
                    continue  # 如果不是特定页面，不执行任何操作

                time.sleep(2)  # 显示特殊内容 2秒
                display_image_fast(oled, pages[current_page_index])  # 返回当前页面
        
        time.sleep(0.1)
        
if __name__ == '__main__':
    page_control(oled,controller)

