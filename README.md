# 叠加态 AI 游戏机（ESP32 + MicroPython）

- 一个基于 ESP32 与 MicroPython 的小型 AI 游戏机项目，使用 SSD1306 128×64 OLED 作为显示屏，配合双按键交互，支持页面切换、平滑滑动、图像展示与 Wi-Fi 连接到后端服务进行对话。
- 项目包含启动流程、页面系统、按键控制、网络通信与图形展示等模块，适合学习与扩展嵌入式 + AI 的交互式终端。

## 功能概览
- 启动动画与欢迎页，自动尝试连接指定 Wi-Fi
- 双按键交互：单击/双击/长按识别，页面切换与特殊动作
- 页面系统：终端对话、函数控制、GPT 直连、数据展示
- 图像渲染：快速绘制大图、滚动效果、图标与文本组合
- 网络通信：通过 TCP 与服务器交互，展示返回结果

## 硬件与连线
- 开发板：ESP32
- 显示屏：SSD1306 OLED 128×64，I2C 接口
  - SDA 接 GPIO 21
  - SCL 接 GPIO 22
- 按键：上拉输入
  - Button1 接 GPIO 0
  - Button2 接 GPIO 25
- 板载 LED：GPIO 2（启动阶段闪烁作为状态指示）

## 主要模块
- 启动与流程控制：[boot.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/boot.py)
  - 初始化 I2C 与 OLED，加载字体，连接 Wi-Fi，显示欢迎页与 Logo
  - 提示“点击任意按键开始”，进入页面系统
- 页面系统与交互：[page.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/page.py)
  - 通过按钮切换页面，长按触发特殊内容或进入功能页
  - 示例特殊内容：滚动 AI 页、显示 jingkang 图片、切回 Logo
- 平滑滑动与功能入口：[function.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/function.py)
  - SmoothSlider 实现文本页的平滑滑动
  - 进入“服务终端”等功能，调用网络端交互
- 按键识别：[control.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/control.py)
  - 去抖与点击模式识别：单击/双击/长按
  - 动作码：11/12/13 对应按钮1，21/22/23 对应按钮2
- 图像资源与渲染：
  - 快速渲染与页面图：[image.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/image.py)、[song_image.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/song_image.py)
  - GUI 示例页（战斗力、国力对比）：[GUI.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/GUI.py)
  - SSD1306 驱动（基于 framebuf）：[ssd1306.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/ssd1306.py)
- 网络与通信：
  - Wi-Fi 连接：[wifi.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/wifi.py)
  - TCP 客户端与消息选择：[socket.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/socket.py)、[server.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/server.py)

## 部署与运行
1. 烧录 MicroPython 到 ESP32（参考 MicroPython 官方文档）
2. 将本项目文件复制到设备（推荐 mpremote）

```bash
# 列出设备
mpremote connect ttyUSB0

# 复制整个目录到设备根目录
mpremote cp -r /Users/jeremygan/Desktop/TangledupAI/AI_game :

# 或者逐个复制文件
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/boot.py :
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/page.py :
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/function.py :
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/control.py :
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/wifi.py :
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/socket.py :
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/server.py :
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/ssd1306.py :
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/image.py :
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/song_image.py :
mpremote cp /Users/jeremygan/Desktop/TangledupAI/AI_game/GUI.py :
```

3. 字体文件
- 代码中使用 `oled.font_load("GB2312-12.fon")`。确保将该字体文件拷贝到设备根目录或合适路径。
- 若未使用扩展字体，MicroPython framebuf 的内置 `text()` 仅支持基本 ASCII。

4. 启动方式
- MicroPython 默认执行 `boot.py` 后再执行 `main.py`。本项目将主要逻辑放在 `boot.py` 的 `main()` 中。
- 选择其一：
  - 在设备上手动运行：`mpremote run boot.py`
  - 或将启动调用迁移/复制到 `main.py`：

```python
# main.py
from boot import main
main("你的WiFi名", "你的WiFi密码")
```

## 使用说明
- Wi-Fi 设置：修改 [boot.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/boot.py#L121-L123) 中的 SSID/密码，或在 `main()` 调用时传入
- 按键动作：
  - Button1 单击：11（向左切换/滑动）
  - Button2 单击：21（向右切换/滑动）
  - Button1 长按：13、Button2 长按：23（触发特殊动作/进入功能）
- 页面与特殊动作：
  - AI 页滚动展示后返回 Logo
  - 宋/金主题图片切换示例
  - 进入“服务终端”后，可在屏幕上选择预设消息并通过 TCP 发送到服务器

## 服务器通信
- 默认服务器：`106.15.108.125:1234`，可在 [socket.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/socket.py) 与 [server.py](file:///Users/jeremygan/Desktop/TangledupAI/AI_game/server.py) 中修改
- 发送内容：在终端页选择预设消息后，使用 `usocket` 建立 TCP 连接并发送，接收结果显示到屏幕
- 异常处理：包含连接超时/拒绝等错误提示，确保在失败时关闭套接字

## 目录结构
- 启动与流程：boot.py
- 页面系统：page.py
- 平滑滑动与入口：function.py
- 按键识别：control.py
- 显示与图像：ssd1306.py、image.py、song_image.py、GUI.py
- Wi-Fi 与通信：wifi.py、socket.py、server.py

## 常见问题
- 字体不生效或报错
  - 确认设备上存在 `GB2312-12.fon`，且驱动支持 `font_load` 方法。若不支持，请移除 `font_load` 调用或使用内置 `text()`。
- Wi-Fi 连接失败
  - 检查 SSID/密码是否正确，确保 2.4GHz 网络与信号稳定
- 服务器未响应
  - 确认后端服务运行、IP/端口正确、网络可达

## 扩展建议
- 替换页面为你的自定义功能：数据采集、小游戏、串口调试等
- 接入更多外设：蜂鸣器、加速度计、旋转编码器
- 将 TCP 协议封装为应用层指令集，支持更丰富的交互

