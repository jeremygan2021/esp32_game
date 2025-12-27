import usocket as socket
import utime
from wifi import connect_wifi

SERVER_IP = '106.15.108.125'
SERVER_PORT = 1234
MESSAGE = '测试'  # 使用普通字符串

def socket_conn(SERVER_IP,SERVER_PORT,MESSAGE):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)  # 设置10秒超时
    
    try:
        print("Attempting to connect to {}:{}".format(SERVER_IP, SERVER_PORT))
        s.connect((SERVER_IP, SERVER_PORT))
        print("WIFI 连接成功。")

        s.send(MESSAGE.encode('utf-8'))

        data = s.recv(1024)
        received_data = data.decode('utf-8')
        print('Received:', received_data)  # 将接收到的字节解码为字符串
        return received_data
        
    except OSError as e:
        if e.args[0] == 110:  # ETIMEDOUT
            print("WIFI 连接超时。Connection timed out. The server might not be responding.")
        elif e.args[0] == 111:  # ECONNREFUSED
            print("WIFI 连接被拒绝。Connection was refused. The server might not be running or the port might be closed.")
        elif e.args[0] == -2:  # Name or service not known
            print("Address-related error. Please check the IP address and port.")
        else:
            print("An unexpected error occurred: {}".format(str(e)))
        print("Error type: {}".format(type(e).__name__))
        print("Error details: {}".format(str(e)))
    
    finally:
        s.close()
        
    
# if __name__ == '__main__':
#     connect_wifi("yqf", "888999yqf")
#     socket_conn(SERVER_IP,SERVER_PORT,MESSAGE)
#     connect_wifi("Tangled Up AI", "djt12345678")
#     main()