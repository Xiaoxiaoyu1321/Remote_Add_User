#导入模块
import socket
import time
import select
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


host = "0.0.0.0" #服务器地址
port = 14254 #端口
print("服务器：",host)
print("端口:",port)
StartNewServer = False #设定主线程启动新服务器为禁用

#启动服务器监听
def StartServerListen(): 
    serversocket.bind((host,port)) #绑定端口
    serversocket.listen(1) #设置监听数量
    print("已开启监听，最多1个用户连接")
    
        


StartServerListen()
#主循环
while True:
    if StartNewServer == True:
        StartNewServer() #重新启动服务器
        StartNewServer = False #设定主线程启动新服务器为禁用
    
    print("等待用户连接")
    
    clientsocket,addr = serversocket.accept() #同意所有用户连接
    print("新用户连接" ,str(addr))
    
    try:
        ready = select.select([serversocket],[],[],10) #设置超时时间
        if ready[0]:
            getMessage = ""  #设置接收到的信息为空，以便防堵塞工作"
            getMessage = clientsocket.recv(9999).decode('gbk') #收到信息并转码
            print("收到信息",getMessage)
         else:
            print("用户可能因超时，已被踢出")
            
    except Exception as q:
        print("错误信息:" , q)
        
    
    
    