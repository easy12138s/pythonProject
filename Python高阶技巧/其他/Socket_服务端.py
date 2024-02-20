"""
    Socket(套接字):进程之间通信的工具
    两个进程间通信，必须要有客户端和服务端
    主动的是客户端，被动的是服务端
"""
import socket
# 创建Socket对象
socket_server = socket.socket()

# 绑定IP地址和端口
socket_server.bind(("localhost", 8888))

# 监听端口,listen方法接收一个整数参数，表示接受的连接数量
socket_server.listen(1)
# 等待客户端链接:accept返回的是一个二元元组，通过两个变量分别接收
# result: tuple = socket_server.accept()
# conn = result[0]        # 客户端与服务端的连接对象
# address = result[1]     # 客户端地址信息
conn, address = socket_server.accept()      # 简洁写法
# accept是阻塞的方法，如果没有客户端连接就会卡在这一行，不往下执行
print(f"客户端信息：{address}")

while True:
    # 接收客户端信息，使用客户端与服务端的连接对象conn而不是socket_server
    data = conn.recv(1024).decode("UTF-8")
    # recv参数为缓冲区大小，返回值是bytes字节数组，不是字符串，通过decode方法进行解码为字符串对象
    print(f"客户端发来的消息是：{data}")

    # 发送给客户端消息
    msg = input("请输入回复给客户端的消息：").encode("UTF-8")    # 通过encode将字符串编码为字节数组对象
    if msg == 'exit':
        print("断开连接，已下线!")
        break
    conn.send(msg)

# 关闭连接
conn.close()
socket_server.close()

