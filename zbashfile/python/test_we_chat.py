import itchat

itchat.auto_login(enableCmdQR=True)

itchat.send('Hello, filehelper', toUserName='filehelper')
#itchat.auto_login(hotReload=True)