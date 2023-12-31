# Remote_Add_User   
# 一个可以远程在Windows 系统上添加账户的软件   

**数据无价，软件请仅授权给您信任的人使用**    
若因使用本软件而导致的任何损失，本软件作者概不负责   
  

# 配置方法

## 服务器配置方法   
1. 在您的服务器上安装Python 
2. 前往 *Release* 页下载 Server.zip 
3. 以管理员身份运行cmd.exe，定位到程序目录，输入"python Server.py" 

## 管理员客户端配置方法
1. 在您的控制机器上安装Python 
2. 前往 *Release* 页下载 Client.py 
3. 以任意用户身份运行cmd.exe，定位到程序目录，输入 "python Client.py "

## 特别注意！！！
**在安装Python时，请务必将Python 添加到系统环境变量中**   
Python 需要 Python 3.x 或更新版本  



# 基本使用

## 如何修改服务器的管理员密码？

当您首次运行客户端时，您可能会看到客户端提示您您使用的是默认密码。使用默认密码可能会导致您的服务器被未授权的访问。  
如何修改服务器的管理员密码  
当您解压完Server.zip 时，您会注意到您的目录下有两个txt文件，Admin.txt 是您的服务端管理用户名，AdminPwd 是您服务端管理密码  
您只需要便捷的修改其中的内容然后保存即可   

## 如果您需要创建exe 可执行文件
如果您需要脱离Python 环境使用客户端，您可以通过Pyinstaller 及其他同类软件创建exe ，下面是一个示例

```
pip install pyinstaller
pyinstaller -F AdminClient.py
```

您也可以通过相同的其他方法创建exe可执行文件。但是请注意，您创建出来的exe文件很有可能会被他人反编译或以其他方式获取您的服务器地址以及账户密码，所以请妥善保管好您的文件，仅分享给您信任的人。

## 如果您无法通过除服务器外的其他设备连接到服务器   
请确保您已在您的 ISP 中允许您设置的端口的传入连接    
   
若您已在ISP 中允许您设置的端口的传入连接，请尝试以下方法：    

1. 请前往 Windows 防火墙 设置，允许 Python.exe 的传入连接   
2. 修改 Server.py 中绑定的服务器及端口设置    
3. 使用局域网连接服务端    

## 如果您需要更安全的连接   
受限于本人的能力，我没有（懒）给这个软件传输加密，通过明文传输在局域网还行，但是在外网存在不安全问题，您可以根据您的需要修改源代码添加加密功能  

## 支持的平台

服务端仅支持 Windows 远程开户，不支持Linux 等其他操作系统。  
而客户端则可以在任何支持完整版Python 的平台上运行    

# 附属软件

## 关于 AdminClientCreater
**此附带工具仅推荐高级用户使用**   
使用此工具可以创建专门的管理员客户端，而无需每次重新输入服务器地址及管理账号密码。请妥善保管好您生成的文件。   

使用仅需要运行 start.bat