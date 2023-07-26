"""
    Socket(套接字):进程之间通信的工具
    两个进程间通信，必须要有客户端和服务端
"""
import socket

# 创建Socket对象
socket_client = socket.socket()

# 连接到服务端
socket_client.connect(("localhost", 8888))

while True:
    msg = input("请输入要发送的消息。。。")
    if msg == 'exit':
        break
    # 发送消息
    socket_client.send(msg.encode("UTF-8"))

    # 接收服务端返回的消息
    recv_data = socket_client.recv(1024)
    print(f"服务端发回来的消息是：{recv_data.decode('UTF-8')}")

# 关闭客户端
socket_client.close()
