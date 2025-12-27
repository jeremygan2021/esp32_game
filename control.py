from machine import Pin, Timer
import time

class GameController:
    DOUBLE_CLICK_TIME = 500  # Maximum time between clicks for a double-click (ms)
    LONG_PRESS_TIME = 1000   # Minimum time for a long press (ms)

    def __init__(self, button1_pin=0, button2_pin=25):
        self.button1 = Pin(button1_pin, Pin.IN, Pin.PULL_UP)
        self.button2 = Pin(button2_pin, Pin.IN, Pin.PULL_UP)
        self.button1_state = self.ButtonState()
        self.button2_state = self.ButtonState()
        self.timer = Timer(-1)
        self.last_action = None

        self.button1.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self._button_callback)
        self.button2.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self._button_callback)

    class ButtonState:
        def __init__(self):
            self.last_press_time = 0
            self.press_count = 0
            self.is_pressed = False
            self.press_duration = 0

    def _check_long_press(self, button_state, button_name):
        if button_state.is_pressed and time.ticks_diff(time.ticks_ms(), button_state.last_press_time) >= self.LONG_PRESS_TIME:
            self.last_action = button_name + "Long Press"
            button_state.is_pressed = False

    def _button_callback(self, pin):
        button_state = self.button1_state if pin == self.button1 else self.button2_state
        button_name = "Button 1" if pin == self.button1 else "Button 2"
        
        current_time = time.ticks_ms()
        if not pin.value():  # Button pressed (remember, it's active low)
            if not button_state.is_pressed:
                button_state.is_pressed = True
                if time.ticks_diff(current_time, button_state.last_press_time) <= self.DOUBLE_CLICK_TIME:
                    button_state.press_count += 1
                else:
                    button_state.press_count = 1
                button_state.last_press_time = current_time
                
                # Start timer to check for long press
                self.timer.init(period=self.LONG_PRESS_TIME, mode=Timer.ONE_SHOT, 
                                callback=lambda t: self._check_long_press(button_state, button_name))
        else:  # Button released
            if button_state.is_pressed:
                button_state.is_pressed = False
                press_duration = time.ticks_diff(current_time, button_state.last_press_time)
                
                # Cancel the long press timer
                self.timer.deinit()
                
                if press_duration < self.LONG_PRESS_TIME:
                    if button_state.press_count == 2:
                        self.last_action = button_name + "Double Click"
                        button_state.press_count = 0
                    elif button_state.press_count == 1:
                        self.last_action = button_name + "Single Click"

    def get_action(self):
        action = self.last_action
        self.last_action = None
        if action == "Button 1Single Click":
            return 11
        elif action == "Button 1Double Click":
            return 12
        elif action == "Button 1Long Press":
            return 13
        elif action == "Button 2Single Click":
            return 21
        elif action == "Button 2Double Click":
            return 22
        elif action == "Button 2Long Press":
            return 23







# # # Usage example:
# controller = GameController()
# 
# while True:
#     action = controller.get_action()
#     if action:
#         print(action)
#     time.sleep(0.1)