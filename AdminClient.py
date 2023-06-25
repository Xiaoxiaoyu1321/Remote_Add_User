import socket
host = input('请输入您要管理的服务器:')
port = int(input('请输入您要管理的服务器的端口(默认14254):'))
Admin = input("请输入服务器管理用户名:")
AdminPwd = input("请输入服务器管理密码:")
Client = socket.socket()
SP = "|||"



Account = input("请输入您要开户的账户名:")
AccountPwd = input("请输入您要开户的密码:")
msg = "CreateNewAccount" + SP + Admin + SP + AdminPwd + SP + Account + SP + AccountPwd
    
    
Client.connect((host,port))
Client.send(msg.encode('gbk'))
Client.close()
    