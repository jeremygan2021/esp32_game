from machine import Pin
import ssd1306
from ssd1306 import SSD1306_I2C

import framebuf

# 初始化I2C
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# 清除显示屏
oled.fill(0)

def mountain():
    # 画山的轮廓
    oled.line(0, 50, 15, 30, 1)
    oled.line(15, 30, 30, 50, 1)
    oled.line(30, 50, 50, 20, 1)
    oled.line(50, 20, 70, 50, 1)
    oled.line(70, 50, 90, 35, 1)
    oled.line(90, 35, 110, 50, 1)
    oled.line(110, 50, 128, 40, 1)

    # 画山的内部细节
    oled.line(20, 40, 30, 30, 1)
    oled.line(30, 30, 40, 40, 1)
    oled.line(60, 35, 70, 25, 1)
    oled.line(70, 25, 80, 35, 1)
    oled.line(100, 40, 110, 30, 1)
    oled.line(110, 30, 120, 40, 1)

    # 画湖泊/河流
    oled.line(0, 60, 20, 55, 1)
    oled.line(20, 55, 40, 58, 1)
    oled.line(40, 58, 60, 55, 1)
    oled.line(60, 55, 80, 60, 1)
    oled.line(80, 60, 100, 55, 1)
    oled.line(100, 55, 128, 60, 1)

    # 画树木
    # 树1
    oled.line(10, 50, 10, 40, 1)
    oled.line(12, 50, 12, 40, 1)
    oled.line(8, 40, 14, 40, 1)
    oled.line(7, 38, 15, 38, 1)
    oled.line(6, 36, 16, 36, 1)

    # 树2
    oled.line(90, 50, 90, 40, 1)
    oled.line(92, 50, 92, 40, 1)
    oled.line(88, 40, 94, 40, 1)
    oled.line(87, 38, 95, 38, 1)
    oled.line(86, 36, 96, 36, 1)

    # 画太阳
    # oled.rect(110, 15, 8, 1)

    # 画太阳光芒
    oled.line(110, 7, 110, 0, 1)
    oled.line(110, 23, 110, 30, 1)
    oled.line(102, 15, 95, 15, 1)
    oled.line(118, 15, 125, 15, 1)
    oled.line(105, 10, 100, 5, 1)
    oled.line(115, 10, 120, 5, 1)
    oled.line(105, 20, 100, 25, 1)
    oled.line(115, 20, 120, 25, 1)

    # 显示绘制的内容
    oled.show()
    
def gennor():
    # 画将军的头盔
    oled.line(50, 10, 78, 10, 1)  # 头盔顶部
    oled.line(50, 10, 40, 20, 1)  # 左侧头盔
    oled.line(78, 10, 88, 20, 1)  # 右侧头盔
    oled.line(40, 20, 88, 20, 1)  # 头盔底部
    oled.line(45, 15, 83, 15, 1)  # 头盔装饰

    # 画将军的脸
    oled.line(50, 20, 50, 35, 1)  # 左侧脸
    oled.line(78, 20, 78, 35, 1)  # 右侧脸
    oled.line(50, 35, 78, 35, 1)  # 下巴

    # 画眼睛
    oled.pixel(55, 25, 1)  # 左眼
    oled.pixel(73, 25, 1)  # 右眼
    oled.pixel(56, 26, 1)  # 左眼细节
    oled.pixel(74, 26, 1)  # 右眼细节

    # 画鼻子
    oled.line(64, 25, 64, 30, 1)  # 鼻子

    # 画嘴巴
    oled.line(58, 33, 70, 33, 1)  # 嘴巴

    # 画胡子
    oled.line(58, 34, 60, 35, 1)
    oled.line(70, 34, 68, 35, 1)

    # 画将军的铠甲
    oled.line(45, 35, 45, 55, 1)  # 左侧铠甲
    oled.line(83, 35, 83, 55, 1)  # 右侧铠甲
    oled.line(45, 55, 83, 55, 1)  # 铠甲底部
    oled.line(45, 35, 83, 35, 1)  # 铠甲顶部

    # 画铠甲细节
    oled.line(50, 35, 50, 55, 1)  # 左内侧铠甲
    oled.line(78, 35, 78, 55, 1)  # 右内侧铠甲
    oled.line(61, 35, 61, 55, 1)  # 中间左侧铠甲
    oled.line(67, 35, 67, 55, 1)  # 中间右侧铠甲
    oled.line(50, 45, 78, 45, 1)  # 铠甲中间横线

    # 画肩甲
    oled.line(40, 20, 45, 35, 1)  # 左肩甲
    oled.line(88, 20, 83, 35, 1)  # 右肩甲

    # 画将军的身体
    oled.line(45, 55, 45, 64, 1)  # 左侧身体
    oled.line(83, 55, 83, 64, 1)  # 右侧身体
    oled.line(45, 64, 83, 64, 1)  # 腿部

    # 画腿部细节
    oled.line(55, 55, 55, 64, 1)  # 左腿
    oled.line(73, 55, 73, 64, 1)  # 右腿

    # 画手臂和武器
    oled.line(45, 40, 30, 55, 1)  # 左臂
    oled.line(30, 55, 32, 64, 1)  # 左手
    oled.line(83, 40, 98, 55, 1)  # 右臂
    oled.line(98, 55, 96, 64, 1)  # 右手
    oled.line(96, 64, 96, 55, 1)  # 武器柄
    oled.line(96, 55, 100, 50, 1)  # 武器锋刃
    
    def draw_text_bl(oled):
        # 画出“汴梁”两个字
        oled.text('副', 15, 20)
        oled.text('将', 100, 20)

    # 显示绘制的内容
    draw_text_bl(oled)
    oled.show()

def wall_of_bianlian():
    def draw_wall(oled):
        # 画城墙的底部
        for y in range(48, 64):
            for x in range(0, 128):
                oled.pixel(x, y, 1)
        
        # 画城墙的砖块
        for y in range(48, 64, 4):
            for x in range(0, 128, 16):
                for i in range(0, 16, 4):
                    oled.pixel(x+i, y, 0)
                    oled.pixel(x+i, y+1, 0)
                    
        # 画城墙的顶部
        for x in range(0, 128, 16):
            oled.rect(x, 40, 16, 8, 1)
            oled.fill_rect(x + 4, 44, 8, 4, 1)

    def draw_text_bl(oled):
        # 画出“汴梁”两个字
        oled.text('汴', 40, 20)
        oled.text('梁', 70, 20)

        
    def draw_text(oled):
        # 画出“靖康之耻”四个字
        oled.text('靖', 4, 0)
        oled.text('康', 36, 0)
        oled.text('之', 68, 0)
        oled.text('耻', 100, 0)


    # 清空显示屏
    oled.fill(0)

    # 画城墙
    draw_wall(oled)
    draw_text(oled)

    # 画文字
    draw_text_bl(oled)

    # 更新显示屏
    oled.show()


if __name__ == '__main__':
    wall_of_bianlian()