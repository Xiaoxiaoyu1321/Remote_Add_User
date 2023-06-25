#导入模块
import socket
import time
import select

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

SP = "|||"

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
    
        
        
#得到程序管理员账户
def GetAdminAccount():
    global AdminAccount
    global AdminAccountPwd
    with open("Admin.txt","r") as f:
        AdminAccount = f.read()
        f.close()
    with open("AdminPwd.txt","r") as f:
        AdminAccountPwd = f.read()
        f.close()
    print('本地管理员账户名:',AdminAccount)
    print('本地管理员密码:',AdminAccountPwd)
    
        

GetAdminAccount()

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
            
            #尝试分割文本
            try:
                Infor = getMessage.split(SP)
                if len(Infor) != 0:
                    if Infor[0] == "CreateNewAccount":
                        Admin = Infor[1] #程序管理员账户
                        AdminPwd = Infor[2] #程序管理员账户密码
                        Account = Infor[3] #欲创建的账户名
                        AccountPwd = Info[4] #欲创建的账户密码
                        if Admin == AdminAccount and AdminPwd = AdminAccountPwd:
                            cmd = "net user " + Account + " " AccountPwd + " //add"
                            print(cmd)
                            #os.system()
            except Exception as bnm:
                print("无法尝试分割文本,错误信息:" , bnm)
                
        else:
            print("用户可能因超时，已被踢出")
            
    except Exception as q:
        print("错误信息:" , q)
        
    
    
    