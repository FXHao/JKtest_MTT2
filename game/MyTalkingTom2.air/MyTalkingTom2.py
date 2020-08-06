# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *



from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
using(_project_root)
from game.Game import Game
from game.screenmanager.api import *
import traceback
from helper import exists_any, position_to_absolute
from channel.Channel import *

class MyTalkingTom2(Game):

    nativeBanner = None
    nativeSplash = None
    nativeInterstitial = None
    nativeInterstitialClose = None
    GuideTest = None
    AdTest = None
    ScreenManager = None

    '''================== 初始化 =================='''

    def config(self):
        super(MyTalkingTom2, self).config()
        self.ScreenManager = new_ScreenManager("MTT2Screen", self.MasterManager)
        self.GuideTest = MyTalkingTom2_Guide(MasterManager = self.MasterManager)
        self.AdTest = MyTalkingTom2_Ad(MasterManager = self.MasterManager)
        self.ScreenManager.config()
        self.init_imglist()

    # [Helper] 初始化图片
    def init_imglist(self):
        self.nativeBanner = [Template(r"tpl1565861133795.png", record_pos=(-0.367, -0.835), resolution=(1080, 2280)), Template(r"tpl1568975410884.png", record_pos=(0.206, -0.723), resolution=(1080, 1920)), Template(r"tpl1570776265451.png", record_pos=(-0.021, -0.833), resolution=(720, 1520))]

        self.nativeSplash = [Template(r"tpl1565771856076.png", record_pos=(0.174, -0.339), resolution=(720, 1280))]
        self.nativeInterstitial = [Template(r"tpl1565860833031.png", threshold=0.8, record_pos=(-0.319, 0.257), resolution=(1080, 2280)), Template(r"tpl1566541160832.png", record_pos=(0.202, 0.058), resolution=(1080, 2248)), Template(r"tpl1570763650210.png", record_pos=(0.082, -0.308), resolution=(720, 1520)), Template(r"tpl1567826456493.png", record_pos=(0.006, -0.611), resolution=(1080, 1920)), Template(r"tpl1570759026587.png", record_pos=(0.337, 0.1), resolution=(1080, 2248))]
        self.nativeInterstitialClose = [Template(r"tpl1565860843397.png", record_pos=(0.372, -0.212), resolution=(1080, 2280)), Template(r"tpl1566541176236.png", record_pos=(0.331, -0.431), resolution=(1080, 2248)), Template(r"tpl1567826466958.png", record_pos=(0.428, -0.813), resolution=(1080, 1920)), Template(r"tpl1570763661920.png", record_pos=(0.429, -0.324), resolution=(720, 1520)),Template(r"tpl1570759015750.png", record_pos=(0.289, -0.253), resolution=(1080, 2248))] #

    ''' 获取流程字典 '''
    def getProcessDict(self):

        return {"StartApp": self.start_app,
                "StopApp": self.stop_app,
                "ClearApp": self.clear_app,
                "WakePhone": self.wake_phone,
                "Restart": self.Channel.restart,

                "SkipInterstitial": self.Channel.skipInterstitial,


                "Guide":self.GuideTest.guide,
                "Setting":self.GuideTest.setting,
                "MiniGame":self.GuideTest.minigame,
                "Shop":self.GuideTest.shop,

                "CheckSplash": self.AdTest.checkSplash,
                "CheckBanner": self.AdTest.checkBanner,
                "CheckInterstitial": self.AdTest.checkInterstitial,
                "CheckVideo": self.AdTest.checkVideo,
                "CheckExitBox": self.AdTest.checkExitBox,

                "BannerForeyard":self.AdTest.checkBanner_Foreyard,
                "BannerKitchen":self.AdTest.checkBanner_Kitchen,
                "BannerBathroom":self.AdTest.checkBanner_Bathroom,
                "BannerBedroom":self.AdTest.checkBanner_Bedroom,
                "BannerBackyard":self.AdTest.checkBanner_Backyard,

                "CheckVideoBalloon":self.AdTest.checkVideo_Balloon,
                "CheckVideoMiniGame":self.AdTest.checkVideo_MiniGame,
                "CheckVideoBonus":self.AdTest.checkVideo_Bonus,
                "CheckVideoNoFood":self.AdTest.checkVideo_NoFood,
                "CheckVideoRefrigeratorFood":self.AdTest.checkVideo_RefrigeratorFood,
                "CheckVideoKitchenFood":self.AdTest.checkVideo_KitchenFood,
                "CheckVideoDebuff":self.AdTest.checkVideo_Debuff,
                "CheckVideoSoap":self.AdTest.checkVideo_Soap,
                "CheckVideoCrayon":self.AdTest.checkVideo_Crayon,
                "CheckVideoEnergyDrink":self.AdTest.checkVideo_EnergyDrink}

    '''================== 通用流程 =================='''

    #跳过权限申请
    def skipPermission(self, times = 1):

        poco = self.poco
        sleep(1)

        for i in range(0, times):
            function = exists_any
            pos = function([poco(text = "始终允许"), poco(text = "允许"), poco(text = "确定"), poco(text = "确  定"),poco(text = "总是允许")])
            if (pos != False):
                touch(pos)
                sleep(1)
                continue
            return

    # 跳过每日签到
    def skipDailyCheckIn(self):
        sleep(5)
        pos = exists_any([Template(r"tpl1573466388761.png", record_pos=(-0.283, -0.019), resolution=(720, 1520))])
        if (pos != False):
            touch(pos)
            for i in range(5):
                pos2 = exists_any([Template(r"tpl1573466873123.png", record_pos=(0.001, -0.515), resolution=(720, 1520))])
                if (pos != False):
                    touch(position_to_absolute([0.5,0.5]))
                    sleep(3)
            sleep(5)
        pos = exists_any([Template(r"tpl1565946466706.png", record_pos=(0.0, 0.486), resolution=(1080, 2280))])
        if (pos != False):
            touch(pos)
            sleep(5)

    # 跳过暑假福利
    def skipHolidayWelfare(self):
        sleep(5)
        if exists(Template(r"tpl1565078669765.png", record_pos=(0.134, -0.542), resolution=(1080, 2340))):
            wait(Template(r"tpl1565078699109.png", record_pos=(0.001, 0.612), resolution=(1080, 2340)))
            touch(Template(r"tpl1565078699109.png", record_pos=(0.001, 0.612), resolution=(1080, 2340)))
            sleep(15)

    # 跳过麦克风权限申请
    def skipMicrophonePermission(self):

        poco = self.poco

        sleep(10)
        if poco(text = "始终允许").exists():
            poco(text = "始终允许").click()
        if poco(text = "允许").exists():
            poco(text = "允许").click()
        if poco(text = "确定").exists():
            poco(text = "确定").click()
        sleep(5)

class MyTalkingTom2_Guide:

    '''================== 初始化 ===================='''

    MasterManager = None

    # MasterManager 中的指针
    poco = None
    AppID = None
    Game = None
    Channel = None
    Reporter = None

    # Game 中的指针
    ScreenManager = None

    def __init__(self, MasterManager):
        self.MasterManager = MasterManager
        self.poco = self.MasterManager.poco
        self.AppID = self.MasterManager.AppID
        self.Game = self.MasterManager.Game
        self.Channel = self.MasterManager.Channel
        self.Reporter = self.MasterManager.Reporter
        self.ScreenManager = self.Game.ScreenManager

    '''==================== 入口 ====================='''

    ''' 新手指引入口 '''
    def guide(self):
        self.Game.stop_app()
        sleep(1)
        self.Game.clear_app()
        sleep(2)
        self.Game.start_app()
        self.Game.skipPermission(5)
        self.Channel.login()
        self.enter()
        self.startNewGame()
        self.guidancePickup()
        self.guidanceLift()
        self.guidanceFeed()
        self.guidanceBathroom()
        self.guidanceSleep()
        self.guidanceAirplane()
        self.guidanceDress()
        self.Game.skipPermission(2)
        self.guidancemagic()
        self.endGuide()

    ''' 查看设置入口 '''
    def setting(self):
        self.ScreenManager.goToForeyard_Setting()
        self.checkLaws()
        # self.checkGiftCode()
        self.checkSetting()
        self.ScreenManager.backToMain()

    ''' 查看小游戏入口 '''
    def minigame(self):
        self.ScreenManager.goToForeyard_MiniGame()
        self.testMiniGame()
        self.ScreenManager.backToMain()

    ''' 查看商店入口 '''
    def shop(self):
        self.ScreenManager.goToForeyard_Shop()
        self.checkGoods()
        self.ScreenManager.backToMain()

    '''================= For guide() ================='''

    # 选择生日性别
    def enter(self):
        sleep(5)
        touch(Template(r"tpl1564977560468.png", record_pos=(0.364, 0.126), resolution=(1080, 2248)), duration = 0.2, times = 2)
        touch(Template(r"tpl1564977511533.png", record_pos=(0.003, 0.676), resolution=(1080, 2248)))

        if exists(Template(r"tpl1564978338559.png", record_pos=(-0.292, 0.113), resolution=(1080, 2248))):
            touch(Template(r"tpl1564978338559.png", record_pos=(-0.292, 0.113), resolution=(1080, 2248)))

    # 覆盖安装后，在选择存档界面选择新建游戏
    def startNewGame(self):
        sleep(5)
        if exists(Template(r"tpl1565321798920.png", record_pos=(0.005, -0.69), resolution=(1080, 2340))):
            touch(Template(r"tpl1565321816345.png", record_pos=(0.001, -0.181), resolution=(1080, 2340)))
            sleep(2)
            touch(Template(r"tpl1565321946759.png", record_pos=(-0.152, 0.244), resolution=(1080, 2340)))

    # 从盒子里拿出来

    def guidancePickup(self):
        for i in range(0, 3):
            sleep(20)
            for i in range(1,3):
                sleep(2)
                pos = exists(Template(r"tpl1564986333843.png", record_pos=(0.021, 0.091), resolution=(1080, 2248)))

                break
            if (pos == False):
                keyevent("BACK")
                continue
            swipe(pos, vector=[-0.0692, -0.389])
            break
        sleep(5)

    # 提起汤姆猫
    def guidanceLift(self):
        swipe(Template(r"tpl1565332358635.png", record_pos=(0.018, 0.173), resolution=(1080, 2340)), vector=[-0.0012, -0.2678])
        sleep(5)

    # 点击去厨房 + 喂汤姆猫胡萝卜
    def guidanceFeed(self):
        touch(Template(r"tpl1568965520172.png", record_pos=(-0.196, 0.783), resolution=(1080, 1920)))
        swipe(Template(r"tpl1565058021601.png", record_pos=(-0.004, 0.395), resolution=(1080, 2248)),vector=[-0.0087, -0.0846])
        sleep(5)

    # 点击去厕所 + 拖动汤姆猫去马桶上
    def guidanceBathroom(self):
        touch(Template(r"tpl1568965901549.png", record_pos=(0.001, 0.782), resolution=(1080, 1920)))
        sleep(0.5)
        touch(Template(r"tpl1565338179254.png", record_pos=(0.376, -0.056), resolution=(1080, 2340)))
        sleep(15)
        self.Game.skipPermission()

    # 拖动汤姆猫去床上 + 关灯睡觉
    def guidanceSleep(self):
        touch(Template(r"tpl1568965674523.png", record_pos=(0.193, 0.781), resolution=(1080, 1920)))
        sleep(2)
        touch(Template(r"tpl1565338811412.png", record_pos=(0.333, -0.094), resolution=(1080, 2340)))
        sleep(2)

        #关灯
        touch(Template(r"tpl1565337673698.png", record_pos=(0.43, -0.181), resolution=(1080, 2340)))
        sleep(20)

    # 点击去飞机抽奖 + 拖动汤姆猫上飞机 + 选择一个飞机奖励+ 打开飞机奖励 + 点击第n次飞机奖励
    def guidanceAirplane(self):
        touch(Template(r"tpl1565060088730.png", record_pos=(0.388, 0.956), resolution=(1080, 2248)))
        for i in range(3):
            pos = exists(Template(r"tpl1568966054806.png", record_pos=(0.332, 0.055), resolution=(1080, 1920)))
            if (pos != False):
                touch(pos)
            else:
                break
        sleep(10)

        touch(Template(r"tpl1565061192053.png", record_pos=(0.345, 0.592), resolution=(1080, 2248)))
        sleep(10)

        # 打开飞机奖励
        touch(Template(r"tpl1565061230949.png", record_pos=(-0.001, -0.069), resolution=(1080, 2248)))
        sleep(10)
        for i in range(0, 10):
            pos = exists(Template(r"tpl1565062131152.png", record_pos=(0.07, 0.252), resolution=(1080, 2248)))
            if (pos != False):
                touch(pos)
                sleep(4)
            else:
                pos = exists(Template(r"tpl1565063759841.png", record_pos=(-0.006, 0.692), resolution=(1080, 2248)))
                if (pos != False):
                    touch(pos)
                    break
                else:
                    continue
        sleep(3)

    # 点击衣柜 + 点击选择按钮 + 点击关闭按钮
    def guidanceDress(self):
        touch(exists_any([Template(r"tpl1565073066846.png", record_pos=(-0.365, -0.2), resolution=(1080, 2248)), Template(r"tpl1569657325818.png", record_pos=(-0.348, -0.234), resolution=(1080, 1920))]))
        sleep(3)
        touch(Template(r"tpl1565073236016.png", record_pos=(0.002, 0.947), resolution=(1080, 2248)))
        sleep(3)
        keyevent("back")

    # 汤姆猫魔术
    def guidancemagic(self):
        #pos = exists_any(Template(r"tpl1584093410662.png", record_pos=(-0.008, 0.631), resolution=(1080, 2340)),Template(r"tpl1584093459264.png", record_pos=(0.006, -0.605), resolution=(1080, 2340)),Template(r"tpl1584093487841.png", record_pos=(0.407, -0.941), resolution=(1080, 2340)))
        #if (pos !):
        #    keyevent("back")
        pass

    # 结束新手时跳过奖励
    def endGuide(self):
        self.Game.skipDailyCheckIn()
        touch(Template(r"tpl1568966744799.png", record_pos=(-0.392, 0.786), resolution=(1080, 1920)))
        self.Game.skipDailyCheckIn()
        self.Reporter.report("新手测试成功")

    '''================ For setting() ================'''

    # 点击法律按钮
    def checkLaws(self):
        touch(Template(r"tpl1565076852338.png", record_pos=(-0.003, 0.358), resolution=(1080, 2248)))
        sleep(2)
        touch(Template(r"tpl1565076944735.png", target_pos=6, record_pos=(0.001, -0.551), resolution=(1080, 2248)))
        sleep(1)
        if (exists(Template(r"tpl1565145547760.png", record_pos=(-0.119, -0.673), resolution=(1080, 2340)))):
            self.Reporter.report("最终用户许可协议显示成功")
        else:
            self.Reporter.report("最终用户许可协议显示失败")
        keyevent("BACK")
        sleep(1)
        touch(Template(r"tpl1565077124832.png", target_pos=6, record_pos=(0.003, -0.352), resolution=(1080, 2248)))
        sleep(1)
        if (exists(Template(r"tpl1565145567639.png", record_pos=(-0.331, -0.933), resolution=(1080, 2340)))):
            self.Reporter.report("隐私政策显示成功")
        else:
            self.Reporter.report("隐私政策显示失败")
        keyevent("BACK")
        sleep(1)
        keyevent("BACK")
        sleep(2)
        self.Channel.skipInterstitial()

    # 点击兑换码按钮
    def checkGiftCode(self):
        touch(Template(r"tpl1565077736205.png", record_pos=(-0.001, 0.517), resolution=(1080, 2248)))
        sleep(3)
        if (exists(Template(r"tpl1565077761533.png", record_pos=(-0.004, -0.203), resolution=(1080, 2248)))):
            self.Reporter.report("兑换码显示成功")
        else:
            self.Reporter.report("兑换码显示失败")
        sleep(1)
        keyevent("MENU")
        sleep(5)
        keyevent("MENU")
        sleep(3)
        for i in range(0, 5):
            pos = exists(Template(r"tpl1565077857819.png", threshold=0.8, record_pos=(0.0, -0.146), resolution=(1080, 2248)))
            if (pos == False):
                keyevent("BACK")
                sleep(1)
            else:
                break
        sleep(1)
        self.Channel.skipInterstitial()
        assert_exists(Template(r"tpl1565077857819.png", record_pos=(0.0, -0.146), resolution=(1080, 2248)), "点击关闭按钮")

    # 点击设置按钮
    def checkSetting(self):
        touch(Template(r"tpl1565077908369.png", record_pos=(0.003, 0.674), resolution=(1080, 2248)))
        sleep(1)
        if (exists(Template(r"tpl1568972317596.png", record_pos=(0.003, -0.636), resolution=(1080, 1920)))):
            self.Reporter.report("设置显示成功")
        else:
            self.Reporter.report("设置显示失败")
        sleep(1)
        keyevent("BACk")

    '''================ For minigame() ==============='''

    # 测试小游戏
    def testMiniGame(self):
        is_swipe = False
        game_list = [Template(r"tpl1565074007867.png", record_pos=(-0.328, -0.621), resolution=(1080, 2340)),Template(r"tpl1565074493851.png", record_pos=(-0.003, -0.629), resolution=(1080, 2340)),Template(r"tpl1565075073797.png", record_pos=(0.315, -0.623), resolution=(1080, 2340)),Template(r"tpl1565075630683.png", record_pos=(-0.33, -0.217), resolution=(1080, 2340)),Template(r"tpl1565075863933.png", record_pos=(-0.005, -0.215), resolution=(1080, 2340)),Template(r"tpl1565076209914.png", record_pos=(0.322, -0.215), resolution=(1080, 2340)),Template(r"tpl1565076411496.png", record_pos=(-0.326, 0.195), resolution=(1080, 2340)),Template(r"tpl1565076669045.png", threshold=0.8, record_pos=(-0.005, 0.197), resolution=(1080, 2340)),Template(r"tpl1565076885312.png", record_pos=(0.319, 0.195), resolution=(1080, 2340))]
        gameExists_list = [Template(r"tpl1565074252004.png", record_pos=(0.003, 0.544), resolution=(1080, 2340)),Template(r"tpl1565074713559.png", record_pos=(-0.343, 0.885), resolution=(1080, 2340)),Template(r"tpl1565075127378.png", record_pos=(-0.021, 0.632), resolution=(1080, 2340)),Template(r"tpl1565347021231.png", record_pos=(-0.003, -0.131), resolution=(1080, 1920)),Template(r"tpl1565075981162.png", record_pos=(-0.309, 0.664), resolution=(1080, 2340)),Template(r"tpl1565347167700.png", record_pos=(-0.006, -0.395), resolution=(1080, 1920)),Template(r"tpl1565076446494.png", record_pos=(-0.331, 0.869), resolution=(1080, 2340)),Template(r"tpl1565076695417.png", record_pos=(-0.001, -0.514), resolution=(1080, 2340)),Template(r"tpl1565347372132.png", record_pos=(-0.363, 0.664), resolution=(1080, 1920))]
        for i in range(len(game_list)):

            if (is_swipe == False):
                pos = exists(game_list[i])
                if (pos == False):
                    is_swipe = True

            if (is_swipe == True):

                for j in range(0, 3):
                    swipe(position_to_absolute([0.5, 0.4]), position_to_absolute([0.5, 0.8]))

                for j in range(0, 3):
                    pos = exists(game_list[i])
                    if (pos == False):
                        swipe(position_to_absolute([0.5, 0.8]), position_to_absolute([0.5, 0.4]))
                        continue
                    else:
                        break

                if (pos == False):
                    self.Reporter.report("Game icon not found.")
                    continue

            # 图标存在
            touch(pos)
            self.Game.AdTest.checkVideo_TooSleepy(isReport = False)
            sleep(2)
            if (exists(gameExists_list[i])):
                self.Reporter.report("小游戏" + i.__str__() + "检测成功")
            else:
                self.Reporter.report("小游戏" + i.__str__() + "检测失败")

            # 退回
            keyevent("BACK")
            sleep(1)
            pos = exists(Template(r"tpl1565074085510.png", record_pos=(-0.144, 0.094), resolution=(1080, 2340)))
            if (pos != False):
                touch(pos)
            for j in range(0, 5):
                sleep(2)
                pos = exists_any([Template(r"tpl1568968102483.png", record_pos=(-0.001, -0.816), resolution=(1080, 1920)), Template(r"tpl1569729625234.png", record_pos=(0.0, -0.813), resolution=(1080, 1920)), Template(r"tpl1570517128204.png", record_pos=(-0.002, -0.943), resolution=(1080, 2340))])
                if (pos != False):
                    break
                #self.Channel.skipInterstitial()
                keyevent("BACK")
                sleep(1)

    '''================= For shop() =================='''

    #检查商品
    def checkGoods(self):
        good_list = [Template(r"tpl1565079622651.png", record_pos=(-0.33, -0.445), resolution=(1080, 2340)), Template(r"tpl1565079696311.png", record_pos=(0.001, -0.444), resolution=(1080, 2340)), Template(r"tpl1565079786045.png", record_pos=(0.324, -0.44), resolution=(1080, 2340)), Template(r"tpl1565347465512.png", record_pos=(-0.326, 0.267), resolution=(1080, 1920)), Template(r"tpl1565347502684.png", record_pos=(-0.001, 0.267), resolution=(1080, 1920)), Template(r"tpl1565347539817.png", record_pos=(0.324, 0.274), resolution=(1080, 1920)), Template(r"tpl1565347560029.png", record_pos=(-0.213, 0.739), resolution=(1080, 1920)), Template(r"tpl1565347581547.png", record_pos=(0.224, 0.741), resolution=(1080, 1920))]
        for i in range(0, len(good_list)):
            pos = exists(good_list[i])
            if (pos != False):
                self.Reporter.report("第" + (i + 1).__str__() + "个商品显示成功")
            else:
                self.Reporter.report("第" + (i + 1).__str__() + "个商品显示失败")
            sleep(1)

class MyTalkingTom2_Ad:

    '''================== 初始化 ===================='''

    MasterManager = None

    # MasterManager 中的指针
    poco = None
    AppID = None
    Game = None
    Channel = None
    Reporter = None

    # Game 中的指针
    ScreenManager = None

    def __init__(self, MasterManager):
        self.MasterManager = MasterManager
        self.poco = self.MasterManager.poco
        self.AppID = self.MasterManager.AppID
        self.Game = self.MasterManager.Game
        self.Channel = self.MasterManager.Channel
        self.Reporter = self.MasterManager.Reporter
        self.ScreenManager = self.Game.ScreenManager

    '''==================== 入口 ====================='''

    ''' 检测开屏 '''
    def checkSplash(self):
        self.Channel.checkSplash(isReport = True)
        #self.Channel.login()

    ''' 检测Banner '''
    def checkBanner(self):

        for fun in [self.checkBanner_Foreyard,
                    self.checkBanner_Kitchen,
                    self.checkBanner_Bathroom,
                    self.checkBanner_Bedroom,
                    self.checkBanner_Backyard]:
            try:
                fun()
            except:
                self.MasterManager.curCase.Message += "Case Failed"
                traceback.print_exc()
#                 #self.Channel.restart()

    ''' 检测插屏 '''
    def checkInterstitial(self):

        # 去主界面
        self.Reporter.report("正在检查插屏")
#         self.ScreenManager.goToKitchen(isReport_Interstitial = True)
#         sleep(100)
#         self.ScreenManager.goToForeyard(isReport_Interstitial = True)
#         sleep(100)
#         self.ScreenManager.goToKitchen(isReport_Interstitial = True)
#         sleep(100)
#         self.ScreenManager.goToBathroom(isReport_Interstitial = True)
#         sleep(100)
#         self.ScreenManager.goToBedroom(isReport_Interstitial = True)
#         sleep(100)
#         self.ScreenManager.goToBackyard(isReport_Interstitial = True)
        '''
        self.ScreenManager.goToForeyard(isReport_Interstitial = True)
        self.ScreenManager.goToKitchen(isReport_Interstitial = True)
        self.ScreenManager.goToBathroom(isReport_Interstitial = True)
        self.ScreenManager.goToBedroom(isReport_Interstitial = True)
        self.ScreenManager.goToBackyard(isReport_Interstitial = True)
        '''
        self.ScreenManager.goToForeyard()
        sleep(90)

        self.ScreenManager.goToKitchen()
        #self.Channel.skipInterstitial(isReport = True)
        sleep(90)

        self.ScreenManager.goToBathroom()
        #self.Channel.skipInterstitial(isReport = True)
        sleep(90)

        self.ScreenManager.goToBedroom()
        #self.Channel.skipInterstitial(isReport = True)
        sleep(90)

        self.ScreenManager.goToBackyard()


    ''' 检测视频 '''
    def checkVideo(self):
        for fun in [self.checkVideo_MiniGame,
                    self.checkVideo_Trampoline,
                    self.checkVideo_Bonus,
                    self.checkVideo_NoFood,
                    self.checkVideo_RefrigeratorFood,
                    self.checkVideo_KitchenFood,
                    self.checkVideo_Debuff,
                    self.checkVideo_Soap,
                    self.checkVideo_Crayon,
                    self.checkVideo_EnergyDrink]:

            try:
                fun()
            except:
                traceback.print_exc()
                self.Channel.restart()

    ''' 检测退出框 '''
    def checkExitBox(self):
        self.ScreenManager.goToForeyard()
        keyevent("BACK")
        self.Channel.skipExitBox(isReport = True)

    '''============= For checkBanner() ============='''

    # 测试_前院部分
    def checkBanner_Foreyard(self):

        # 前院主界面
        self.ScreenManager.goToForeyard()
        self.Channel.isBannerExists(isReport = True)

        # 场景更换装饰页面
        touch(Template(r"tpl1565770786983.png", record_pos=(-0.403, 0.733), resolution=(1080, 2248)))
        self.Channel.isBannerExists(isReport = True)

        # 设置页面

        self.ScreenManager.backToMain()
        pos = exists_any([Template(r"tpl1584170413590.png", record_pos=(-0.431, -0.693), resolution=(1080, 2280)),Template(r"tpl1584772720041.png", record_pos=(-0.416, -0.692), resolution=(1080, 2280)),Template(r"tpl1584772757902.png", record_pos=(-0.44, -0.688), resolution=(1080, 2280))])


#         if (pos == False):
#             self.Reporter.raise_error()
        touch(pos)
        #self.ScreenManager.goToForeyard_Setting()
        self.Channel.isBannerExists(isReport = True)


        # 法律法规页面
        touch(Template(r"tpl1565770916957.png", record_pos=(0.0, 0.362), resolution=(1080, 2248)))
        self.Channel.isBannerExists(isReport = True)
        #self.ScreenManager.goToForeyard()
        self.ScreenManager.backToMain()

#         # 部分小游戏游戏界面顶部 & 小游戏结束页面(后台已关闭）
#         touch(Template(r"tpl1566964626043.png", record_pos=(-0.377, 0.185), resolution=(1080, 2248)))
#         sleep(1)
#         touch(Template(r"tpl1566964610441.png", record_pos=(0.0, -0.219), resolution=(1080, 2248)))
#         sleep(2)
#         self.checkVideo_TooSleepy(isReport = False)
#         self.Channel.isBannerExists(isReport = True)
#         touch(Template(r"tpl1566964641420.png", record_pos=(0.011, 0.601), resolution=(1080, 2248)))
#         sleep(1)
#         keyevent("BACK")
#         sleep(1)
#         touch(Template(r"tpl1566964668826.png", record_pos=(-0.144, 0.161), resolution=(1080, 2248)))
#         sleep(5)
#         self.Channel.skipInterstitial()
#         sleep(5)
#         self.Channel.isBannerExists(isReport = True)
#         self.ScreenManager.goToForeyard()

    # 测试_厨房部分
    def checkBanner_Kitchen(self):

        # 厨房界面
        self.ScreenManager.goToKitchen()
        self.Channel.isBannerExists(isReport = True)

        # 沙冰机界面
        touch(Template(r"tpl1565771132760.png", record_pos=(-0.294, -0.185), resolution=(1080, 2248)))
        self.Channel.isBannerExists(isReport = True)
        self.ScreenManager.backToMain()
        #self.ScreenManager.goToKitchen()

    # 测试_浴室部分
    def checkBanner_Bathroom(self):

        # 厕所
        self.ScreenManager.goToBathroom()
        self.Channel.isBannerExists(isReport = True)

        # 浴缸界面
        pos = exists_any([Template(r"tpl1569652654216.png", record_pos=(-0.346, 0.091), resolution=(1080, 1920)), Template(r"tpl1565855004149.png", record_pos=(-0.344, 0.185), resolution=(1080, 2248))])
        touch(pos)
        self.Channel.isBannerExists(isReport = True)
        #self.ScreenManager.goToBathroom()
        self.ScreenManager.backToMain()
        # 马桶界面
        touch(Template(r"tpl1565771390269.png", record_pos=(0.382, -0.001), resolution=(1080, 2248)))
        self.Channel.isBannerExists(isReport = True)
        sleep(5)
        self.ScreenManager.goToBathroom()
        #self.ScreenManager.backToMain()

        # 医疗箱界面
        touch(Template(r"tpl1569740048940.png", record_pos=(-0.279, -0.381), resolution=(1080, 1920)))
        self.Channel.isBannerExists(isReport = True)
        #self.ScreenManager.goToBathroom()
        self.ScreenManager.backToMain()
    # 测试_卧室部分
    def checkBanner_Bedroom(self):

        # 卧室界面
        self.ScreenManager.goToBedroom()
        self.Channel.isBannerExists(isReport = True)

        # 睡觉界面
        touch(Template(r"tpl1565771502501.png", record_pos=(0.356, 0.153), resolution=(1080, 2248)))
        self.Channel.isBannerExists(isReport = True)
        self.ScreenManager.backToMain()

        # 衣柜界面
        touch(Template(r"tpl1565771571686.png", record_pos=(-0.393, -0.197), resolution=(1080, 2248)))
        self.Channel.isBannerExists(isReport = True)


        touch(Template(r"tpl1584344660559.png", record_pos=(0.432, 0.198), resolution=(1080, 2280)))
        self.Channel.isBannerExists(isReport = True)

        touch(Template(r"tpl1584344749177.png", record_pos=(-0.016, 0.942), resolution=(1080, 2280)))
        self.Channel.isBannerExists(isReport = True)

        sleep(2)
        touch(Template(r"tpl1584344915603.png", record_pos=(-0.006, 0.792), resolution=(1080, 2280)))
        self.Channel.isBannerExists(isReport = True)
        sleep(10)


        self.ScreenManager.backToMain()

        # 画画界面
        touch(Template(r"tpl1565771637885.png", record_pos=(0.343, -0.363), resolution=(1080, 2248)))
        self.Channel.isBannerExists(isReport = True)
        touch(Template(r"tpl1565855282710.png", record_pos=(0.013, 0.955), resolution=(1080, 2248)))
        touch(Template(r"tpl1566369165886.png", record_pos=(0.391, -0.715), resolution=(1080, 2248)))
        self.ScreenManager.backToMain()



    # 测试_后院部分
    def checkBanner_Backyard(self):

        # 后院界面
        self.ScreenManager.goToBackyard()
#         sleep(5)
#         pos = exists(Template(r"tpl1566370616013.png", record_pos=(0.422, -0.718), resolution=(1080, 2248)))
#         if pos:
#             touch(pos)

#         self.ScreenManager.goToBackyard()
        self.Channel.isBannerExists(isReport = True)

#         # 拍照界面
#         pos = exists_any([Template(r"tpl1568976202963.png", rgb=True, target_pos=6, record_pos=(-0.377, 0.459), resolution=(1080, 1920)), Template(r"tpl1568976071429.png", rgb=True, target_pos=6, record_pos=(-0.38, 0.458), resolution=(1080, 1920))])
#         if (pos != False):
#             touch(pos)
#         else:
#             self.Reporter.raise_error()

#         self.Channel.isBannerExists(isReport = True)

#         # 打分界面
#         touch(Template(r"tpl1565771849444.png", record_pos=(0.392, 0.674), resolution=(1080, 2248)))
#         sleep(0.5)
#         self.Channel.isBannerExists(isReport = True)
#         keyevent("BACK")
#         sleep(0.5)
#         touch(Template(r"tpl1565771879583.png", record_pos=(-0.15, 0.195), resolution=(1080, 2248)))
#         sleep(0.5)

#         # 拍照相册界面
#         touch(Template(r"tpl1565771926401.png", record_pos=(0.382, 0.927), resolution=(1080, 2248)))
#         sleep(0.5)
#         self.Channel.isBannerExists(isReport = True)
#         keyevent("BACK")
#         self.ScreenManager.goToBackyard()

        # 收藏界面
        touch(Template(r"tpl1565772047033.png", record_pos=(0.374, 0.678), resolution=(1080, 2248)))
        self.Channel.isBannerExists(isReport = True)
        sleep(1.5)
        #self.ScreenManager.goToBackyard()
        self.ScreenManager.backToMain()

        # 宠物窝界面
        touch(Template(r"tpl1565772105888.png", record_pos=(-0.399, 0.228), resolution=(1080, 2248)))
        self.Channel.isBannerExists(isReport = True)
        #self.ScreenManager.goToBackyard()
        self.ScreenManager.backToMain()
        # 飞行界面
        touch(Template(r"tpl1565772146564.png", record_pos=(0.334, 0.157), resolution=(1080, 2248)))
        sleep(5)
        self.Channel.isBannerExists(isReport = True)
        #self.ScreenManager.goToBackyard()
        self.ScreenManager.backToMain()

    '''========== For checkInterstitial() =========='''

    # 切换底部按钮，返回检查插屏广告结果(暂时没用到或者改用了其他方法
#     def findInterstitial(self):
#         bottomButton = [Template(r"tpl1565605746616.png", record_pos=(-0.393, 0.776), resolution=(720, 1280)),Template(r"tpl1565605760440.png", record_pos=(-0.197, 0.775), resolution=(720, 1280)),Template(r"tpl1565605768152.png", record_pos=(-0.007, 0.775), resolution=(720, 1280)),Template(r"tpl1565605776482.png", record_pos=(0.193, 0.772), resolution=(720, 1280)),Template(r"tpl1565605988357.png", record_pos=(0.382, 0.772), resolution=(720, 1280))]
#         bottomButton.extend(bottomButton)
#         for button in bottomButton:
#             if exists(button):
#                 touch(button, duration=0.3)
#                 sleep(5)
#                 #普通插屏
#                 if (self.Channel.skipInterstitial(isReport = True)):
#                     return True
#         return False

    '''========== For checkVideoAd() ==============='''

    # 视频_气球礼盒
    def checkVideo_Balloon(self):
        self.ScreenManager.goToForeyard()

        # 点击礼盒
        sleep(5)
        pos = exists_any([Template(r"tpl1583981586150.png", record_pos=(0.303, -0.104), resolution=(1080, 2280)),Template(r"tpl1583994856831.png", record_pos=(0.386, 0.385), resolution=(1080, 2280))])
        if (pos == False):
            self.Reporter.report("未出现气球礼盒")
            return
        touch(pos)
        sleep(2)

            # 点击看视频按钮
        pos = exists(Template(r"tpl1565606189301.png", record_pos=(-0.001, 0.494), resolution=(720, 1280)))
        if (pos == False):
            #print("+++++++")
            self.Reporter.report("气球礼盒中无观看视频按钮")
            return
        touch(pos)
        self.Channel.skipVideo(isReport = True)
        sleep(10)
        self.ScreenManager.backToMain()

    # 视频_玩小游戏: 小游戏复活 & 双倍飞行币
    def checkVideo_MiniGame(self):
        resurgenceAvailable = True
        self.ScreenManager.goToForeyard_MiniGame()
        pos = exists(Template(r"tpl1565075863933.png", record_pos=(-0.005, -0.215), resolution=(1080, 2340)))
        if (pos == False):
            self.Reporter.report("未出现游戏图标")
            return
        touch(pos)
        self.checkVideo_TooSleepy(isReport = True)
        sleep(1)
        
        while (True):
            arrow = exists(Template(r"tpl1565853539912.png", record_pos=(0.001, 0.558), resolution=(720, 1280)))
            if (arrow != False):
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                pos = exists(Template(r"tpl1565850621664.png", record_pos=(0.01, 0.313), resolution=(1080, 2248)))
                if (pos != False):
                    touch(pos)
                    self.Channel.skipVideo(isReport = True)
                    #sleep(5)
                    break
                arrow = exists(Template(r"tpl1565853539912.png", record_pos=(0.001, 0.558), resolution=(720, 1280)))
                if (arrow == False):
                    break
                else:
                    continue
            else:
                print("+++++++++++++++++++++++++++未进入游戏界面")
                

        arrow = exists(Template(r"tpl1565853539912.png", record_pos=(0.001, 0.558), resolution=(720, 1280)))
        print("22222222222222222222222222")
        if (arrow == False):
            self.Reporter.report("未出现复活视频按钮")
        
        #sleep(5)
        while (True):
            arrow = exists(Template(r"tpl1565853539912.png", record_pos=(0.001, 0.558), resolution=(720, 1280)))
            print("333333333333333333333333333")
            if (arrow != False):
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
                sleep(0.01)
                touch(arrow)
            else:
                break
        sleep(2)
        pos = exists_any([Template(r"tpl1571047615999.png", record_pos=(0.006, 0.026), resolution=(1080, 2280))])
        if (pos == False):
            #self.Channel.skipInterstitial()
            keyevent("BACK")
            sleep(2)
        pos = exists_any([Template(r"tpl1565660995294.png", record_pos=(-0.014, 0.346), resolution=(720, 1280))])
        if (pos == False):
            self.Reporter.report("未出现双倍飞行币按钮")
        else:
            touch(pos)
            self.Channel.skipVideo(isReport = True)
        sleep(2)
        self.ScreenManager.backToMain()

    # 视频_每日特惠
    def checkVideo_Bonus(self):
        self.ScreenManager.goToForeyard_Shop()
        pos = exists_any([Template(r"tpl1566556982532.png", record_pos=(0.001, -0.26), resolution=(1080, 2280)), Template(r"tpl1571047030653.png", record_pos=(-0.002, -0.227), resolution=(1080, 2280)), Template(r"tpl1571122198087.png", record_pos=(0.007, -0.205), resolution=(1080, 2160))])
        if (pos != False):
            touch(pos)
            self.Channel.skipVideo(isReport = True)
        else:
            self.Reporter.report("未出现每日特惠视频按钮")
        self.ScreenManager.backToMain()

    # 视频_无食物: 当厨房没有食物，通过观看广告来获取食物
    def checkVideo_NoFood(self):
        self.ScreenManager.goToKitchen()
        sleep(3)
        pos = exists(Template(r"tpl1565860651498.png", record_pos=(-0.008, 0.572), resolution=(1080, 2280)))
        if (pos == False):
            self.Reporter.report("未出现领取大餐提示")
            return
        touch(pos)
        self.Channel.skipVideo(isReport = True)

    # 视频_冰箱食物
    def checkVideo_RefrigeratorFood(self):
        self.ScreenManager.goToKitchen_Refrigerator()
        pos = exists_any([Template(r"tpl1565854357282.png", record_pos=(-0.196, 0.434), resolution=(1080, 2248)), Template(r"tpl1571122017199.png", record_pos=(-0.325, -0.079), resolution=(1080, 2160)), Template(r"tpl1571047098711.png", record_pos=(0.002, -0.128), resolution=(1080, 2280))])
        if (pos == False):
            self.Reporter.report("未出现免费冰箱食物")
        else:
            touch(pos)
            self.Channel.skipVideo(isReport = True)
            sleep(1)
        self.ScreenManager.backToMain()

    # 视频_餐厅食物
    def checkVideo_KitchenFood(self):
        self.ScreenManager.goToKitchen()
        pos = exists(Template(r"tpl1565926426602.png", record_pos=(-0.358, 0.362), resolution=(1080, 2280)))
        if (pos == False):
            self.Reporter.report("未出现餐厅食物盒子")
            return
        touch(pos)
        self.Channel.skipVideo(isReport = True)
        sleep(1)

    # 视频_病态
    def checkVideo_Debuff(self):
        self.ScreenManager.goToBathroom_AidKit()
        pos = exists(Template(r"tpl1565666429952.png", record_pos=(0.001, 0.631), resolution=(720, 1280)))
        if (pos == False):
            self.Reporter.report("未出现病态瓶")
            self.ScreenManager.backToMain()
            return
        touch(pos)
        sleep(1)
        pos = exists(Template(r"tpl1565666490906.png", record_pos=(0.003, 0.321), resolution=(720, 1280)))
        if (pos == False):
            self.Reporter.report("未出现免费按钮")
            self.ScreenManager.backToMain()
            return
        touch(pos)
        self.Channel.skipVideo(isReport = True)
        self.ScreenManager.backToMain()

    # 视频_肥皂
    def checkVideo_Soap(self):
        self.ScreenManager.goToBathroom_BathTub()
        pos = exists_any([Template(r"tpl1565663833247.png", record_pos=(-0.014, 0.625), resolution=(720, 1280)), Template(r"tpl1571047145230.png", record_pos=(-0.017, 0.636), resolution=(1080, 2280))])
        if (pos == False):
            self.Reporter.report("未出现免费肥皂")
            self.ScreenManager.backToMain()
            return
        touch(pos)
        self.Channel.skipVideo(isReport = True)
        self.ScreenManager.backToMain()

    # 视频_蜡笔
    def checkVideo_Crayon(self):
        self.ScreenManager.goToBedroom_Crayon()
        sleep(3)
        pos = exists_any([Template(r"tpl1565746865961.png", record_pos=(0.003, 0.79), resolution=(720, 1280)), Template(r"tpl1571121704803.png", record_pos=(0.007, 0.911), resolution=(1080, 2160))])
        if (pos == False):
            self.Reporter.report("未出现选择画")
            self.ScreenManager.backToMain()
            return
        touch(pos)
        pos2 = exists(Template(r"tpl1565667873928.png", record_pos=(0.425, 0.746), resolution=(720, 1280)))
        if (pos2 == False):
            self.Reporter.report("未出现选择蜡笔按钮")
            self.ScreenManager.backToMain()
            return
        for i in range(0, 9):
            pos = exists_any([Template(r"tpl1565667860495.png", record_pos=(0.001, 0.738), resolution=(720, 1280)), Template(r"tpl1571129174290.png", record_pos=(0.005, 0.862), resolution=(1080, 2160))])
            if (pos == False):
                touch(pos2)
                sleep(1)
                continue
            else:
                touch(pos)
                self.Channel.skipVideo(isReport = True)
                self.ScreenManager.backToMain()
                return
        self.Reporter.report("未出现免费蜡笔")
        self.ScreenManager.backToMain()

    # 视频_能量药水
    def checkVideo_EnergyDrink(self):
        self.ScreenManager.goToBedroom()
        pos = exists_any([Template(r"tpl1565664786022.png", threshold=0.85, record_pos=(0.269, 0.588), resolution=(720, 1280)), Template(r"tpl1571129235505.png", record_pos=(0.274, 0.719), resolution=(1080, 2160))])
        if (pos == False):
            self.Reporter.report("未出现能量药水")
            return
        touch(pos)
        self.Channel.skipVideo(isReport = True)

    # [未成功]蹦床损坏后看广告立即修好
    def checkVideo_Trampoline(self):
        self.ScreenManager.goToForeyard()
        touch(Template(r"tpl1584669517695.png", record_pos=(0.343, 0.151), resolution=(1080, 2280)))

        for i in range(0,4):
            if  (exists(Template(r"tpl1584671041783.png", record_pos=(0.053, -0.731), resolution=(1080, 2280)))!=False):
                sleep(1)
            
                if (exists(Template(r"tpl1584669896799.png", record_pos=(-0.006, 0.4), resolution=(1080, 2280)))!=False):
                    touch(Template(r"tpl1584669896799.png", record_pos=(-0.006, 0.4), resolution=(1080, 2280)))
                    self.Channel.skipVideo(isReport = True)
                    self.ScreenManager.backToMain()  
                    return True
                else:
                    self.Reporter.report("未出现蹦床视频")
                    self.ScreenManager.backToMain()  
                    return False
            else:
                touch(Template(r"tpl1584669699096.png", record_pos=(0.231, -0.729), resolution=(1080, 2280)))
                sleep(1)
                            

    # 视频_太困了
    def checkVideo_TooSleepy(self, isReport = False):

        pos = exists(Template(r"tpl1584169427441.png", record_pos=(-0.023, -0.05), resolution=(1080, 2280)))

        if (pos == False): # 未检测到太困提示
            return False

        pos = exists_any([Template(r"tpl1570762579755.png", record_pos=(0.002, 0.609), resolution=(1080, 2248)), Template(r"tpl1571301800744.png", record_pos=(0.008, 0.646), resolution=(1080, 2160))])
        if (pos != False):
            touch(pos)
            return True
        pos = exists_any([Template(r"tpl1570765574987.png", record_pos=(-0.003, 0.644), resolution=(720, 1520)),Template(r"tpl1584177736295.png", record_pos=(-0.01, 0.395), resolution=(1080, 2280))])

        if (pos != False):
            touch(pos)
            return self.Channel.skipVideo(isReport = True)









