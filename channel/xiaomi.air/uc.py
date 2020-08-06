# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
using(_project_root)
from channel.Channel import Channel
from helper import exists_any

class uc(Channel):
    
    def getProcessDict(self):
        return {}
    
    '''=============== 对应渠道流程相关 ================'''
    
    # 登录
    def login(self):
        poco = self.poco
        sleep(20)
        self.Game.skipPermission(5)
        for i in range(0, 10):
            pos = exists_any([Template(r"tpl1564977560468.png", rgb=True, record_pos=(0.364, 0.126), resolution=(1080, 2248)), Template(r"tpl1568968491570.png", rgb=True, record_pos=(-0.399, 0.585), resolution=(1080, 1920))])
            if (pos != False):
                break
            else:
                if(self.Game.skipPermission(5)):
                    sleep(15)
                    continue
                if (exists_any([poco(textMatches="(.*)登录(.*)")])):
                    keyevent("BACK")
                    pos = exists_any([poco(textMatches="(.*)退出(.*)")])
                    touch(pos)
                    sleep(10)
                keyevent("BACK")
                if(self.poco(nameMatches = "(.*)mytalkingtom2(.*)").exists() == False):
                    self.Game.start_app()
                sleep(10)
    
    '''================= Poco Getter ================='''
    
    def getPoco(self, PocoType = "None"):
        
        poco = self.poco
        
        if (PocoType == "None"):
            return None
        
        if (PocoType == "OrdinarySplash_Exist"):        # 普通开屏_存在
            return None
        
        if (PocoType == "OrdinarySplash_Close"):        # 普通开屏_关闭
            return None
        
        if (PocoType == "NativeSplash_Exist"):          # 原生开屏_存在
            return None
        
        if (PocoType == "NativeSplash_Close"):          # 原生开屏_关闭
            return None
        
        if (PocoType == "OrdinaryBanner_Exist"):        # 普通Banner_存在
            return poco("com.outfit7.mytalkingtom2.mi:id/activead").child("android.widget.FrameLayout")
        
        if (PocoType == "NativeBanner_Exist"):          # 原生Banner_存在
            return None
        
        if (PocoType == "OrdinaryInterstitial_Exist"):  # 普通插屏_存在
            return poco("android.widget.RelativeLayout").child("android.widget.RelativeLayout")
        
        if (PocoType == "OrdinaryInterstitial_Close"):  # 普通插屏_关闭
            return poco("android.widget.RelativeLayout").child("android.widget.RelativeLayout").child("android.widget.ImageView")[0]
        
        if (PocoType == "NativeInterstitial_Exist"):    # 原生插屏_存在
            return poco("com.outfit7.mytalkingtom2.mi:id/news_view_pager")
        
        if (PocoType == "NativeInterstitial_Close"):    # 原生插屏_关闭
            return poco("com.outfit7.mytalkingtom2.mi:id/image_close")
        
        if (PocoType == "Video_Exist"):                 # Video_存在
            return poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.RelativeLayout")
        
        if (PocoType == "Video_End"):                   # Video_结束
            return poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.RelativeLayout").child("android.widget.ImageView")
        
        if (PocoType == "Video_Close"):                 # Video_关闭
            return poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.RelativeLayout").child("android.widget.ImageView")[0]
        
        # Defalut
        return None
    
    def getImage(self, ImageType = "None"):
        
        poco = self.poco
        
        if (ImageType == "OrdinarySplash_Exist"):        # 普通开屏_存在
            return None
        
        if (ImageType == "OrdinarySplash_Close"):        # 普通开屏_关闭
            return None
        
        if (ImageType == "OrdinaryBanner_Exist"):        # 普通Banner_存在
            return [Template(r"tpl1566528808677.png", record_pos=(0.236, -0.856), resolution=(1080, 2248)), Template(r"tpl1565840573164.png", record_pos=(0.397, 0.185), resolution=(720, 1280))]
        
        if (ImageType == "OrdinaryInterstitial_Exist"):  # 普通插屏_存在
            return [Template(r"tpl1566528808677.png", record_pos=(0.236, -0.856), resolution=(1080, 2248)), Template(r"tpl1565840573164.png", record_pos=(0.397, 0.185), resolution=(720, 1280))]
        
        if (ImageType == "OrdinaryInterstitial_Close"):  # 普通插屏_关闭
            return None

        if (ImageType == "Video_Close"):                 # Video_关闭
            return None
        
        # Defalut
        return None
    
