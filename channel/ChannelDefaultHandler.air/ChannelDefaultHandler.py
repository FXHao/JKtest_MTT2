# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *

class ChannelDefaultHandler:
    
    i = 1
    poco = None
    
    def __init__(self, poco):
        self.poco = poco
    
    ''' 返回全渠道默认的相应监测点的Poco
        若该监测点不可使用Poco, 则返回None'''
    def getPoco_default(self, PocoType = "None"):
        
        poco = self.poco
        
        if (PocoType == "OrdinarySplash_Exist"):        # 普通开屏_存在
            return [poco(textMatches="(.*)跳过(.*)"), poco(text="身边小朋友都在玩"), poco(text="跳过")]
        
        if (PocoType == "NativeSplash_Exist"):          # 原生开屏_存在
            return None
        
        if (PocoType == "OrdinaryBanner_Exist"):        # 普通Banner_存在
            return [poco(text="广告"), 
                     poco(nameMatches = "(.*)id/activead").offspring(),
                     poco("android:id/content").parent().parent().child("android.widget.FrameLayout").offspring()]
        
        if (PocoType == "NativeBanner_Exist"):          # 原生Banner_存在
            return None
        
        if (PocoType == "OrdinaryInterstitial_Exist"):  # 普通插屏_关闭
            return None
        
        if (PocoType == "OrdinaryInterstitial_Close"):  # 普通插屏_关闭
            return None
        
        if (PocoType == "NativeInterstitial_Close"):    # 原生插屏_关闭
            return None
        
        if (PocoType == "Video_Close"):                 # Video_结束
            return [poco(nameMatches = ("(.*)tt_video_ad_close")), poco(text="关闭广告"), poco(text="返回")]
    
        if (PocoType == "ExitBox_Back"):
            return [poco(nameMatches = ("(.*)id/btn_continue")),
                    poco(nameMatches = ("(.*)MainHeadBack")),
                    poco(text="再玩一会"),
                    poco(text="取消"),
                    poco(text="继续游戏")
                    ]
        return None
    
    ''' 返回全渠道默认的相应监测点的Image List '''
    def getImage_default(self, ImageType = "None"):

        if (ImageType == "OrdinarySplash_Exist"):        # 普通开屏_存在
            return [Template(r"tpl1571056326972.png", record_pos=(-0.003, 0.914), resolution=(720, 1520)), Template(r"tpl1571224359530.png", record_pos=(0.402, -0.835), resolution=(1080, 2160)), Template(r"tpl1571281055622.png", record_pos=(0.408, -0.863), resolution=(1080, 2160))]
        
        if (ImageType == "OrdinaryBanner_Exist"):        # 普通Banner_存在
            return None
        
        if (ImageType == "OrdinaryInterstitial_Exist"):  # 普通插屏_关闭
            return [Template(r"tpl1569829010496.png", record_pos=(0.408, -0.756), resolution=(1080, 1920)), Template(r"tpl1570776463630.png", record_pos=(0.404, -0.847), resolution=(720, 1520)), Template(r"tpl1570778190918.png", record_pos=(0.39, -0.365), resolution=(720, 1520)), Template(r"tpl1570798247945.png", record_pos=(0.375, -0.221), resolution=(720, 1520)), Template(r"tpl1571129208161.png", record_pos=(0.379, -0.668), resolution=(1080, 2160)), Template(r"tpl1571230071353.png", record_pos=(-0.435, -0.862), resolution=(1080, 2160)), Template(r"tpl1570697354719.png", record_pos=(0.45, -0.448), resolution=(1080, 1920))]
        
        if (ImageType == "OrdinaryInterstitial_Close"):  # 普通插屏_关闭
            return [Template(r"tpl1569829010496.png", record_pos=(0.408, -0.756), resolution=(1080, 1920)), Template(r"tpl1570776463630.png", record_pos=(0.404, -0.847), resolution=(720, 1520)), Template(r"tpl1570778190918.png", record_pos=(0.39, -0.365), resolution=(720, 1520)), Template(r"tpl1570798247945.png", record_pos=(0.375, -0.221), resolution=(720, 1520)), Template(r"tpl1571129208161.png", record_pos=(0.379, -0.668), resolution=(1080, 2160)), Template(r"tpl1571230071353.png", record_pos=(-0.435, -0.862), resolution=(1080, 2160)), Template(r"tpl1570697354719.png", record_pos=(0.45, -0.448), resolution=(1080, 1920))]
        if (ImageType == "Video_Close"):                 # Video_关闭
            return [Template(r"tpl1569828720855.png", record_pos=(0.395, -0.235), resolution=(1920, 1080)), Template(r"tpl1570613304570.png", record_pos=(0.414, -0.912), resolution=(720, 1440)), Template(r"tpl1570679019576.png", record_pos=(0.407, -0.208), resolution=(1440, 720)),Template(r"tpl1571122079095.png", record_pos=(0.455, -0.877), resolution=(1080, 2160)),Template(r"tpl1584601219061.png", record_pos=(-0.412, -0.894), resolution=(1080, 2280))]

        
        if (ImageType == "ExitBox_Back"):
            return [Template(r"tpl1573123436527.png", record_pos=(-0.147, 0.215), resolution=(1080, 2160))]
        
        # Defalut
        return None
    
    def isinInterstitial(self):
        
        poco = self.poco
        
        if (poco(nameMatches = "(.*)id/topLevel").exists()):
            #print("未检测到普通插屏")
            return False
        #print("检测到普通插屏")
        return True






