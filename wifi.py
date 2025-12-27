import network
import time
from machine import SoftI2C, Pin
from ssd1306 import SSD1306_I2C

i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)
oled.font_load("GB2312-12.fon")
oled.fill(0)

def connect_wifi(ssid, password):
    # 创建WLAN接口对象
    wlan = network.WLAN(network.STA_IF)
    
    # 激活WLAN接口
    wlan.active(True)
    
    # 如果未连接，则进行连接
    if not wlan.isconnected():
        print('正在连接到网络...')
        wlan.connect(ssid, password)
        
        # 等待连接或超时
        max_wait = 10
        while max_wait > 0:
            if wlan.isconnected():
                break
            oled.fill(0)
            oled.text("等待连接...", 15, 30)
            oled.show()
            max_wait -= 1
            print('等待连接...')
            time.sleep(1)
        
        # 处理连接结果
        if wlan.isconnected():
            print('网络连接成功')
            print('网络配置:', wlan.ifconfig())
            return True
        else:
            oled.fill(0)
            print('连接失败')
            return False
    else:
        print('已经连接到网络')
        wifi_ip = wlan.ifconfig()
        print('网络配置:', wifi_ip)
        return True
        
    

