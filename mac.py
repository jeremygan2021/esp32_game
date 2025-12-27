import machine
import time

# 配置ADC
adc = machine.ADC(machine.Pin(32))  # MAX4466连接到GPIO32
adc.atten(machine.ADC.ATTN_11DB)  # 设置衰减以读取0-3.3V
adc.width(machine.ADC.WIDTH_12BIT)  # 设置ADC分辨率为12位

# 录音参数
SAMPLE_RATE = 8000  # 采样率
RECORD_TIME = 5  # 录音时长（秒）
CHUNK_SIZE = 1024  # 每次写入文件的样本数

def record_audio(filename):
    print("开始录音...")
    start_time = time.ticks_ms()
    samples = bytearray()
    
    while time.ticks_diff(time.ticks_ms(), start_time) < RECORD_TIME * 1000:
        sample = adc.read()
        samples.extend(sample.to_bytes(2, 'little'))
        
        if len(samples) >= CHUNK_SIZE * 2:
            with open(filename, 'ab') as f:
                f.write(samples)
            samples = bytearray()
        
        time.sleep_us(int(1000000 / SAMPLE_RATE))  # 控制采样率
    
    # 写入剩余的样本
    if samples:
        with open(filename, 'ab') as f:
            f.write(samples)
    
    print("录音完成")

# 主程序
def main():
    filename = '/raw_audio.pcm'
    record_audio(filename)
    print("原始音频数据已保存为 " + filename)

if __name__ == "__main__":
    main()