# 这是一个用海龟画图模块和pygame的混音模块制作的简易播放器。
# 作者：李兴球，日期：2018/8/26
def init_mixer():
# 初始化混音器，注意在函数内部导入的模块的作用范围
    have_pygame = False
    try:
        import pygame
        pygame.mixer.init()
        have_pygame = True
    except:
        pygame = None
    return have_pygame,pygame
#class Button(Turtle):
# 按钮类，每个按钮有两张图片，自带音乐
    #def __init__(self,costume_list,x,y,music,width,height):
        #Turtle.__init__(self,visible=False)
        #self.onclick(self.play) # 单击按钮调用play方法
def play(self,x,y):
# 先停止音乐再播放音乐
    pygame.mixer.music.stop() # 停止正在播放的音乐
    pygame.mixer.music.load(self.music)
    #screen.title(gametitle + "，正在播放：" + self.music)
    pygame.mixer.music.play(-1,0) # -1表示循环播放，0表示从头开始播放
def onmousemove(self,event):
# 判断鼠标指针是否在按钮坐标范围内
    pass
def make_button():
# 加载资源，生成播放按钮
    c1_list = ("Losing_Sleep0.gif","Losing_Sleep1.gif")
    music1 = "Alan Walker - Losing Sleep.mp3"
    b1 = Button(c1_list,-250,0,music1,200,150)
    c2_list = ("和兰花在一起0.gif","和兰花在一起1.gif")
    music2 = "Yanni - With An Orchid.mp3"
    b2 = Button(c2_list,00,0,music2,200,150)
    c3_list = ("Faded0.gif","Faded1.gif")
    music3 = "Alan Walker - Faded (纯音乐).wav"
    b3 = Button(c3_list,250,0,music3,200,150)
    c4_list = ("兰贵人0.gif","兰贵人1.gif")
    music4 = "胡伟立-兰贵人.mp3"
    b4 = Button(c4_list,-250,-200,music4,200,150)
    c5_list = ("Spectre0.gif","Spectre1.gif")
    music5 = "Alan Walker - Spectre.mp3"
    b5 = Button(c5_list,0,-200,music5,200,150)
    c6_list = ("新古典主义0.gif","新古典主义1.gif")
    music6 = "新古典主义-组曲.mp3"
    b6 = Button(c6_list,250,-200,music6,200,150)
if __name__ == "__main__":
    gametitle = "花框音乐盒"
    mixer_success,pygame = init_mixer()
if mixer_success:
    print("成功初始化混音器。")
else:
    print("初始化混音器出现问题。")
make_button()