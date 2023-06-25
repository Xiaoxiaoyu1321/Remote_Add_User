#AdminClientCreater
print("欢迎来到 AdminClientCreater ，此向导可以帮助您完成创建管理员专用客户端 \n")
print("先从第一步开始")
print("请输入你要管理的服务器地址，可以是域名或IP")
host = input("请输入您的管理地址:")
print("")
print("接下来，请输入您服务器对应的管理端口，此项设置可以在服务端或ISP处获取")
port = input("请输入您的管理端口：")
print("")
print("接下来我们还需要知道您服务端配置的管理员的账户和密码，以阻止未授权的访问")
Admin = input("请输入您服务端管理员账号：")
AdminPwd = input("请输入您服务端管理员密码：")
abc = input("很好，现在您已完成所有设置，输入y开始创建程序")
if abc == "y" or abc == "Y":
    with open('d.xyfile','r') as f:
        d = f.read()
        f.close()
    b = ""
    b = b + "import socket" + "\n"
    b = b + "host = '" + host + "'"+ "\n"
    b = b + "port = " + port+ "\n"
    b = b + "Admin = '" + Admin + "'"+ "\n"
    b = b + "AdminPwd = '" + AdminPwd + "'"+ "\n"
    b = b + d
    with open("output.py","a",encoding="utf-8") as f:
        f.write(b)
        f.close()

input("文件已写入output.py，按任意键退出")
