# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../..")) + "/"
using(_project_root + "channel/ChannelDefaultHandler.air")
from ChannelDefaultHandler import ChannelDefaultHandler
using(_project_root)
from abc import ABC,abstractmethod
from helper import exists_any

class Channel(ABC):
    
    MasterManager = None
    
    poco = None
    AppID = None
    Game = None
    
    Reporter = None
    
    ChannelDefaultHandler = None
    
    '''==================== 初始化 ==================='''
    
    def __init__(self, TestMasterManager):
        self.MasterManager = TestMasterManager
        
    def config(self):
        self.poco = self.MasterManager.poco
        self.AppID = self.MasterManager.AppID
        self.Game = self.MasterManager.Game
        self.Reporter = self.MasterManager.Reporter
        
        self.ChannelDefaultHandler = ChannelDefaultHandler(self.poco)
        
    @abstractmethod
    def getProcessDict(self):
        return None
    
    '''================= 获取识别信息 ================='''
    
    eCheckPoint = {"None": 0,
             
                   "OrdinarySplash_Exist": 1,
                   "OrdinarySplash_Close": 2,
                   "NativeSplash_Exist": 3,
                   "NativeSplash_Close": 4,
                    
                   "OrdinaryBanner_Exist": 5,
                   "NativeBanner_Exist": 6,
                   
                   "OrdinaryInterstitial_Exist": 7,
                   "OrdinaryInterstitial_Close": 8,
                   "NativeInterstitial_Exist": 9,
                   "NativeInterstitial_Close": 10,
                   
                   "Video_Exist": 11,
                   "Video_End": 12,
                   "Video_Close": 13}
    
    ''' 返回相应监测点的Poco
        若该监测点不可使用Poco, 则返回None'''
    @abstractmethod
    def getPoco(self, PocoType = "None"):
        pass
    
    ''' 返回相应监测点的Image List
        建议全部都填, 但是在有Poco的情况下不会用到图片'''
    @abstractmethod
    def getImage(self, ImageType = "None"):
        pass
    
    '''================= 广告识别相关 ================='''
    
    ''' 开屏是否存在 '''
    def checkSplash(self, isReport = False):
        
        # 原生开屏(图片)
        for j in range(1,3):
            for img in self.Game.nativeSplash:
                sleep(2)
                self.Game.stop_app()
                sleep(2)
                self.Game.start_app()
                sleep(2)
                pos = exists_any(img)
                if (pos != False):
                    self.Reporter.report("检测到原生开屏(图片)", isReport_caller = isReport)
                    return True
        # 检测 普通开屏(poco) + 原生开屏(poco)
        for i in range(1,3):
            sleep(2)
            self.Game.stop_app()
            sleep(2)
            self.Game.start_app()
            sleep(2)
            #pos = exists_any(self.getPoco("OrdinarySplash_Exist")) # 普通开屏(Poco)
            #if (pos != False):
               # self.Reporter.report("检测到普通开屏(Poco)", isReport_caller = isReport)
               # sleep(10)
               # return True
            pos = exists_any(self.ChannelDefaultHandler.getPoco_default("OrdinarySplash_Exist")) # 普通开屏(Default_Poco)
            if (pos != False):
                self.Reporter.report("检测到普通开屏(Default_Poco)", isReport_caller = isReport)
                return True
            pos = exists_any(self.getPoco("NativeSplash_Exist")) # 原生开屏(Poco)
            if (pos != False):
                self.Reporter.report("检测到原生开屏(Poco)", isReport_caller = isReport)
                return True
        # 检测 普通开屏(图片)
#         img_list = []
#         if(self.getImage("OrdinarySplash_Exist") != None):
#             img_list.extend(self.getImage("OrdinarySplash_Exist"))
#         if(self.ChannelDefaultHandler.getImage_default("OrdinarySplash_Exist") != None):
#             img_list.extend(self.ChannelDefaultHandler.getImage_default("OrdinarySplash_Exist"))
#         for img in img_list:
#             sleep(2)
#             self.Game.stop_app()
#             sleep(2)
#             self.Game.start_app()
#             sleep(1)
#             pos = exists_any(img)
#             if (pos != False):
#                 self.Reporter.report("检测到普通开屏(图片)", isReport_caller = isReport)
#                 return True
        
        # 无开屏
        self.Reporter.report("未检测到开屏", isReport_caller = isReport)
        return False
        
    ''' Banner 是否存在
        若存在, 则输出存在并返回True
        若不存在则返回False '''
    def isBannerExists(self, isReport = False, snapshotonly = False):
        
        if (snapshotonly):
            sleep(3)
            self.Reporter.report("Banner界面截图", isReport_caller = isReport)
            return True
        
        checkpoint_list = [[self.Game.nativeBanner, "检测到原生Banner(图片)"],
                           [self.getPoco("OrdinaryBanner_Exist"), "检测到普通Banner(Poco)"], 
                           [self.getPoco("NativeBanner_Exist"), "检测到原生Banner(Poco)"], 
                           [self.ChannelDefaultHandler.getPoco_default("OrdinaryBanner_Exist"), "检测到普通Banner(Default_Poco)"],
                           [self.getImage("OrdinaryBanner_Exist"), "检测到普通Banner(图片)"],
                           [self.ChannelDefaultHandler.getImage_default("OrdinaryBanner_Exist"), "检测到普通Banner(Default_图片)"]]
        
        for c, msg in checkpoint_list:
            pos = exists_any(c)
            if (pos != False):
                self.Reporter.report(msg, isReport_caller = isReport)
                return True
        
        # 无Banner
        self.Reporter.report("未显示Banner", isReport_caller = isReport)
        return False
    
    '''  跳过插屏广告
        若无插屏广告返回False
        若有插屏广告, 关闭插屏广告并放回True 
        
        目前使用:
        原生图片, 普通poco, 普通图片 '''
    
    def skipInterstitial(self, isReport = False):
#         , isQuickSkip = False
#         sleep(2)

#         if (isQuickSkip):
#             if (not self.ChannelDefaultHandler.isinInterstitial()):
#                 return False
#             self.Reporter.report("检测到插屏(不在游戏界面)", isReport_caller = isReport)
#             #keyevent("BACK")
#             if (not self.ChannelDefaultHandler.isinInterstitial()):
#                 return True

#         checkpoint_list = [[self.Game.nativeInterstitial,
#                             self.Game.nativeInterstitialClose,
#                             "检测到原生插屏(图像)"],
#                            [self.ChannelDefaultHandler.getImage_default("OrdinaryInterstitial_Exist"),
#                             self.ChannelDefaultHandler.getImage_default("OrdinaryInterstitial_Close"),
#                             "检测到普通插屏(Default_图像)"],
#                             [self.getPoco("OrdinaryInterstitial_Exist"),
#                             self.getPoco("OrdinaryInterstitial_Close"),
#                             "检测到普通插屏(Poco)"],
#                             [self.ChannelDefaultHandler.getPoco_default("OrdinaryInterstitial_Exist"),
#                             self.ChannelDefaultHandler.getPoco_default("OrdinaryInterstitial_Close"),
#                             "检测到普通插屏(Default_Poco)"],
#                             [self.getImage("OrdinaryInterstitial_Exist"),
#                             self.getImage("OrdinaryInterstitial_Close"),
#                             "检测到普通插屏(图像)"]]

#         for exist, close, msg in checkpoint_list:
#             pos = exists_any(exist, isReturnObj = False)
#             #print("00000000000000000:",pos)
#             if (pos != False):
#                 print(msg)
#                 self.Reporter.report(msg, isReport_caller = isReport)
#                 keyevent("BACK")
#                 print("11111111111111111")
#                 return True
#             else:
#                 continue
#             # 找到广告

#             print("2222222222222222222222222")
#             self.Reporter.report("未找到该插屏退出按钮", isReport_caller = isReport, isRaiseError = True)
#             return False
#             if (exists_any(pos[1]) != False):
#                 print("+++++++++++++++++",exists_any(pos[1]))
#             else:
#                 print("++++++++++++++++++++++False")
#             if (exists_any(pos[1]) != False):
#                 pos = exists_any(close)
#                 #print("3333333333333333333333333",msg)
#                 if (pos != False):
#                     #print("44444444444444444444444444",msg)
#                     self.Reporter.report(msg,isReport_caller = isReport)
#                     touch(pos)
#                 else:
#                     self.Reporter.report("未找到该插屏退出按钮", isReport_caller = isReport, isRaiseError = True)
        
        #采用不在游戏界面逻辑判断
        if (self.ChannelDefaultHandler.isinInterstitial() != False):
            self.Reporter.report("检测到普通插屏")
            keyevent("BACK")
            return True
        if (self.ChannelDefaultHandler.isinInterstitial() == False):
            pos = exists_any(self.Game.nativeInterstitial)
            if (pos != False):
                self.Reporter.report("检测到原生插屏")
                keyevent("BACK")
                return True
            snapshot(msg="未显示插屏广告")
            self.Reporter.report("未显示插屏广告")
            return False

        # 无插屏
        # if (isReport):
        #     self.Reporter.report("未显示插屏广告")
        # return False
    
    ''' 跳过视频
        若无视频播放, 返回False
        若有视频播放, 等待视频结束并返回True '''
    def skipVideo(self, isReport = False):
        sleep(1)
        self.Reporter.report("检测到视频，开始观看。。。", isReport_caller = isReport)
        sleep(30)

        checkpoint_list = [[self.ChannelDefaultHandler.getPoco_default("Video_Close"), "检测到视频结束"],
                           [self.getImage("Video_Close"), "检测到视频结束"],
                           [self.ChannelDefaultHandler.getImage_default("Video_Close"), "检测到视频结束"]]
        #大部分视频30秒  超过30秒没检测到再检测一次
        for close, msg in checkpoint_list:
            pos = exists_any(close)
            if (pos != False):
                self.Reporter.report(msg, isReport_caller = isReport)
                touch(pos)
                return True
        #再次检测
        #sleep(10)
        for close, msg in checkpoint_list:
            pos = exists_any(close)
            if (pos != False):
                self.Reporter.report(msg, isReport_caller = isReport)
                touch(pos)
                return True

        # No video exists
        self.Reporter.report("未检测到视频", isReport_caller = isReport)
        return False
    
    ''' 跳过退出框 '''
    def skipExitBox(self, isReport = False):
        
        checkpoint_list = [[self.ChannelDefaultHandler.getPoco_default("ExitBox_Back"), "检测到退出框(poco)"], 
                           [self.ChannelDefaultHandler.getImage_default("ExitBox_Back"), "检测到退出框(图象)"]]
        
        for back, msg in checkpoint_list:
            pos = exists_any(back)
            if (pos != False):
                self.Reporter.report(msg, isReport_caller = isReport)
                touch(pos)
                return True
        
        self.Reporter.report("未检测到退出框", isReport_caller = isReport)
        return False
    
    '''=============== 对应渠道流程相关 ================'''
    
    ''' 登录 '''
    @abstractmethod
    def login(self):
        pass
    
    ''' 重开游戏(未完) '''
    def restart(self):
        stop_app(self.AppID)
        start_app(self.AppID)
        self.login()
    
    ''' 获取渠道特殊流程函数 '''
    def get_fun(self, fun_name = "None"):
        return None
    
    '''================= 开发 Helper =================='''

    def print_CheckResult(self):
        print("Splash: " + self.isSplashExists().__str__())
        print("Banner: " + self.isSplashExists().__str__())
        print("Interstitial: " + self.isSplashExists().__str__())
        print("Interstitial Close: " + self.isSplashExists().__str__())
        print("Video: " + self.isVideoExists().__str__())

    def isCheckPointReady(self, checkpoint = "All"):
        
        isSplashReady = True
        isBannerReady = True
        isInterstitialReady = True
        isVideoReady = True
        
        if (self.getPoco(self.eCheckPoint["OrdinarySplash_Exist"]) == None and 
            self.getImage(self.eCheckPoint["OrdinarySplash_Exist"]) == None):
            isSplashReady = False
        
        if (self.getPoco(self.eCheckPoint["OrdinaryBanner_Exist"]) == None and 
            self.getImage(self.eCheckPoint["OrdinaryBanner_Exist"]) == None):
            isBannerReady == False
    
        if (self.getPoco(self.eCheckPoint["OrdinaryInterstitial_Exist"]) == None and
            self.getImage(self.eCheckPoint["OrdinaryInterstitial_Exist"]) == None):
            isInterstitialReady == False
        
        if ((self.getPoco(self.eCheckPoint["Video_Exist"]) == None or 
            self.getPoco(self.eCheckPoint["Video_End"]) == None) and
            self.getImage(self.eCheckPoint["Video_Close"]) == None):
            isVideoReady == False
        
        if (checkpoint == "All"):
            return isSplashReady and isBannerReady and isInterstitialReady and isVideoReady
        
        if (checkpoint == "Splash"):
            return isSplashReady
        
        if (checkpoint == "Banner"):
            return isBannerReady
        
        if (checkpoint == "Interstitial"):
            return isInterstitialReady
        
        if (checkpoint == "Video"):
            return isVideoReady



























