# -*- encoding=utf8 -*-
__author__ = "wanghuajun"
from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../../..")) + "/"
using(_project_root)
from game.screenmanager.ScreenManager import ScreenManager
from helper import exists_any
from TestManager.TestMasterManager import MasterManager

class MTT2Screen(ScreenManager,MasterManager):

    def config(self):
        super(MTT2Screen, self).config()

    '''================== 主界面切换 ================='''
    
    # 判断是否在主界面
    def isInMainScreen(self):
        return exists_any([Template(r"tpl1568968528465.png", threshold=0.95, rgb=True, record_pos=(-0.401, 0.59), resolution=(1080, 1920)), Template(r"tpl1571121556578.png", threshold=0.95, rgb=True, record_pos=(-0.397, 0.695), resolution=(1080, 2160))])


    # 去前院
    def goToForeyard(self, isReport_Interstitial = False):
       #检测是否在主界面
        for i in range(0, 2):
            sleep(5)
            if (not self.isInMainScreen()):
                self.backToMain()
            else:
                break
#         # 在主界面
        #for i in range(0, 5):
        pos = exists_any([Template(r"tpl1566294170393.png", threshold=0.6, record_pos=(-0.389, 0.932), resolution=(1080, 2248)), Template(r"tpl1568947501612.png", record_pos=(-0.392, 0.782), resolution=(1080, 1920)), Template(r"tpl1568947186133.png", record_pos=(-0.387, 0.781), resolution=(1080, 1920)), Template(r"tpl1568947201734.png", record_pos=(-0.39, 0.781), resolution=(1080, 1920)),Template(r"tpl1584154493349.png", record_pos=(-0.395, 0.969), resolution=(1080, 2340)),Template(r"tpl1584154814121.png", record_pos=(-0.389, 0.967), resolution=(1080, 2340)),Template(r"tpl1584154882545.png", record_pos=(-0.387, 0.967), resolution=(1080, 2340))])
        if (pos != False):
            print("555555555555555555555555")
            touch(pos)
            sleep(1)
            pos_check = exists_any([Template(r"tpl1568948155552.png", threshold=0.8, rgb=True, record_pos=(-0.023, -0.134), resolution=(1080, 1920)),Template(r"tpl1584773226222.png", record_pos=(0.002, -0.214), resolution=(1080, 2280))])

            if (pos_check != False):
                print("in  foreyard")
                return True
            else:
                if (self.MasterManager.curCase.name== "CheckInterstitial"):
                    self.Channel.skipInterstitial(isReport = True)
                else:
                    keyevent("BACK")

#             if (pos != False):
#                 break
#             if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
#                 continue
#             keyevent("BACK")
#         pos_check = exists_any([Template(r"tpl1568948155552.png", threshold=0.8, rgb=True, record_pos=(-0.023, -0.134), resolution=(1080, 1920))])
#         if (pos_check != False):
#             return True
#         for i in range (0,10):
#             touch(pos)
#             sleep(5)
#             pos_check = exists_any([Template(r"tpl1568948155552.png", threshold=0.8, rgb=True, record_pos=(-0.023, -0.134), resolution=(1080, 1920))])
#             if (pos_check != False):
#                 return True
#             # Todo: 处理弹出
#             if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
#                 continue
#             keyevent("BACK")
#             pos2 = exists(Template(r"tpl1570697720179.png", record_pos=(0.004, 0.057), resolution=(1080, 1920)))
#             if (pos2 != False):
#                 keyevent("BACK")
#                 continue
#             pos_check = exists_any([Template(r"tpl1568948155552.png", threshold=0.8, rgb=True, record_pos=(-0.023, -0.134), resolution=(1080, 1920))])
#             if (pos_check != False):
#                 return True
#             pos2 = exists(Template(r"tpl1570764361137.png", record_pos=(0.424, -0.603), resolution=(720, 1520)))
#             if (pos2 != False):
#                 keyevent("BACK")
#                 continue
#             sleep(1)




    # 去厨房
    def goToKitchen(self, isReport_Interstitial = False):

        # 检测是否在主界面
#         for i in range(0, 2):
#             sleep(5)
#             if (not self.isInMainScreen()):
#                 self.backToMain()
#             else:
#                 break

        # 在主界面
        #for i in range(0, 5):
        pos = exists_any([Template(r"tpl1566294566222.png", threshold=0.6, record_pos=(-0.194, 0.93), resolution=(1080, 2248)), Template(r"tpl1568947445957.png", record_pos=(-0.196, 0.784), resolution=(1080, 1920)), Template(r"tpl1568947399542.png", record_pos=(-0.192, 0.784), resolution=(1080, 1920)), Template(r"tpl1568947417715.png", record_pos=(-0.194, 0.784), resolution=(1080, 1920)),Template(r"tpl1584339969044.png", record_pos=(-0.198, 0.931), resolution=(1080, 2280))])
        if (pos != False):
            touch(pos)
            sleep(1)
            pos_check = exists_any([Template(r"tpl1568948586885.png", threshold=0.8, rgb=True, record_pos=(-0.035, -0.254), resolution=(1080, 1920)),Template(r"tpl1584773394054.png", record_pos=(-0.291, -0.169), resolution=(1080, 2280))])

            if (pos_check != False):
                print("in  kitchen")
                return True
            #if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
            else:
                if (self.MasterManager.curCase.name=="CheckInterstitial"):
                    self.Channel.skipInterstitial(isReport = True)
                else:
                    keyevent("BACK")
               # keyevent("BACK")

#             if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
#                 continue
#             keyevent("BACK")
#         pos_check = exists_any([Template(r"tpl1568948586885.png", threshold=0.8, rgb=True, record_pos=(-0.035, -0.254), resolution=(1080, 1920))])
#         if (pos_check != False):
#             return True
#         for i in range (0,10):
#             touch(pos)
#             sleep(5)
#             pos_check = exists_any([Template(r"tpl1568948586885.png", threshold=0.8, rgb=True, record_pos=(-0.035, -0.254), resolution=(1080, 1920))])
#             if (pos_check != False):
#                 return True
#             # Todo: 处理弹出
#             if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
#                 continue
#             keyevent("BACK")
#             pos2 = exists(Template(r"tpl1570697720179.png", record_pos=(0.004, 0.057), resolution=(1080, 1920)))
#             if (pos2 != False):
#                 keyevent("BACK")
#             sleep(1)

    # 去厕所
    def goToBathroom(self, isReport_Interstitial = False):

        # 检测是否在主界面
#         for i in range(0, 2):
#             sleep(5)
#             if (not self.isInMainScreen()):
#                 self.backToMain()
#             else:
#                 break

        # 在主界面
        #for i in range(0, 5):
        pos = exists_any([Template(r"tpl1566556908526.png", threshold=0.6, record_pos=(-0.004, 0.947), resolution=(1080, 2280)), Template(r"tpl1568947361772.png", record_pos=(-0.003, 0.782), resolution=(1080, 1920)), Template(r"tpl1568947311495.png", record_pos=(0.003, 0.782), resolution=(1080, 1920)), Template(r"tpl1568947320842.png", record_pos=(-0.002, 0.779), resolution=(1080, 1920)),Template(r"tpl1584180269143.png", record_pos=(-0.014, 0.945), resolution=(1080, 2280))])
        if (pos != False):
            touch(pos)
            sleep(1)
            pos_check = exists_any([Template(r"tpl1568980252288.png", threshold=0.9, rgb=True, record_pos=(0.022, -0.216), resolution=(1080, 1920)), Template(r"tpl1570529594280.png", threshold=0.9, rgb=True, record_pos=(0.094, -0.221), resolution=(720, 1440)), Template(r"tpl1571207324463.png", threshold=0.8, rgb=True, record_pos=(0.031, -0.163), resolution=(1080, 2160))])
            #touch(Template(r"tpl1584773469002.png", record_pos=(0.378, -0.519), resolution=(1080, 2280)))
            if (pos_check != False):
                print("in  bathroom")
                return True
            #if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
            else:
                if (self.MasterManager.curCase.name=="CheckInterstitial"):
                    self.Channel.skipInterstitial(isReport = True)
                else:
                    keyevent("BACK")



#         for i in range (0,10):
#             touch(pos)
#             sleep(5)
#             pos_check = exists_any([Template(r"tpl1568980252288.png", threshold=0.9, rgb=True, record_pos=(0.022, -0.216), resolution=(1080, 1920)), Template(r"tpl1570529594280.png", threshold=0.9, rgb=True, record_pos=(0.094, -0.221), resolution=(720, 1440)), Template(r"tpl1571207324463.png", threshold=0.8, rgb=True, record_pos=(0.031, -0.163), resolution=(1080, 2160))])
#             if (pos_check != False):
#                 return True
    #         # Todo: 处理弹出
    #         if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
    #             return Turn
    #         keyevent("BACK")
    #         pos2 = exists(Template(r"tpl1570697720179.png", record_pos=(0.004, 0.057), resolution=(1080, 1920)))
    #         if (pos2 != False):
    #             keyevent("BACK")
            #rint("in bathroom")
        #sleep(1)

    # 去卧室
    def goToBedroom(self, isReport_Interstitial = False):
        # 检测是否在主界面
#         for i in range(0, 2):
#             sleep(5)
#             if (not self.isInMainScreen()):
#                 self.backToMain()
#             else:
#                 break
        # 在主界面

        pos = exists_any([Template(r"tpl1566294794596.png", threshold=0.6, record_pos=(0.193, 0.937), resolution=(1080, 2248)), Template(r"tpl1568947680078.png", record_pos=(0.194, 0.781), resolution=(1080, 1920)), Template(r"tpl1568947633309.png", record_pos=(0.191, 0.783), resolution=(1080, 1920)), Template(r"tpl1568947642670.png", record_pos=(0.193, 0.781), resolution=(1080, 1920))])
        if (pos != False):
            touch(pos)
            sleep(1)
            pos_check = exists_any([Template(r"tpl1568948748049.png", threshold=0.8, rgb=True, record_pos=(-0.015, -0.203), resolution=(1080, 1920)), Template(r"tpl1571207952710.png", threshold=0.8, rgb=True, record_pos=(-0.032, -0.122), resolution=(1080, 2160)),Template(r"tpl1584773668619.png", record_pos=(-0.26, 0.012), resolution=(1080, 2280)),Template(r"tpl1584773678302.png", record_pos=(0.236, -0.012), resolution=(1080, 2280))])


            if (pos_check != False):
                print("in  Bedroom")
                return True
            #if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
            else:
                if (self.MasterManager.curCase.name=="CheckInterstitial"):
                    self.Channel.skipInterstitial(isReport = True)
                else:
                    keyevent("BACK")
              #  keyevent("BACK")
#         for i in range(0, 5):
#             pos = exists_any([Template(r"tpl1566294794596.png", threshold=0.6, record_pos=(0.193, 0.937), resolution=(1080, 2248)), Template(r"tpl1568947680078.png", record_pos=(0.194, 0.781), resolution=(1080, 1920)), Template(r"tpl1568947633309.png", record_pos=(0.191, 0.783), resolution=(1080, 1920)), Template(r"tpl1568947642670.png", record_pos=(0.193, 0.781), resolution=(1080, 1920))])
#             if (pos != False):
#                 break
#             if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
#                 continue
#             keyevent("BACK")
#         pos_check = exists_any([Template(r"tpl1568948748049.png", threshold=0.8, rgb=True, record_pos=(-0.015, -0.203), resolution=(1080, 1920)), Template(r"tpl1571207952710.png", threshold=0.8, rgb=True, record_pos=(-0.032, -0.122), resolution=(1080, 2160))])
#         if (pos_check != False):
#             return True
#         for i in range (0,10):
#             touch(pos)
#             sleep(5)
#             pos_check = exists_any([Template(r"tpl1568948748049.png", threshold=0.8, rgb=True, record_pos=(-0.015, -0.203), resolution=(1080, 1920)), Template(r"tpl1571207952710.png", threshold=0.8, rgb=True, record_pos=(-0.032, -0.122), resolution=(1080, 2160))])
#             if (pos_check != False):
#                 return True
#             # Todo: 处理弹出
#             if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
#                 continue
#             keyevent("BACK")
#             pos2 = exists(Template(r"tpl1570697720179.png", record_pos=(0.004, 0.057), resolution=(1080, 1920)))
#             if (pos2 != False):
#                 keyevent("BACK")
#             sleep(1)

    # 去后院
    def goToBackyard(self, isReport_Interstitial = False):

        # 检测是否在主界面
#         for i in range(0, 2):
#             sleep(5)
#             if (not self.isInMainScreen()):
#                 self.backToMain()
#             else:
#                 break
        # 在主界面
        pos = exists_any([Template(r"tpl1568947694147.png", record_pos=(0.389, 0.782), resolution=(1080, 1920)), Template(r"tpl1568947705998.png", record_pos=(0.389, 0.78), resolution=(1080, 1920)), Template(r"tpl1566294888915.png", threshold=0.6, record_pos=(0.384, 0.931), resolution=(1080, 2248))])
        if (pos != False):
            touch(pos)

        pos_check = exists_any([Template(r"tpl1568948804334.png", threshold=0.8, rgb=True, record_pos=(-0.011, -0.362), resolution=(1080, 1920))])
        if (pos_check != False):
            print("in  backyard")
        #if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
        else:
            if (self.MasterManager.curCase.name=="CheckInterstitial"):
                self.Channel.skipInterstitial(isReport = True)
            else:
                keyevent("BACK")

#         for i in range(0, 5):
#             pos = exists_any([Template(r"tpl1568947694147.png", record_pos=(0.389, 0.782), resolution=(1080, 1920)), Template(r"tpl1568947705998.png", record_pos=(0.389, 0.78), resolution=(1080, 1920)), Template(r"tpl1566294888915.png", threshold=0.6, record_pos=(0.384, 0.931), resolution=(1080, 2248))])
#             if (pos != False):
#                 break
#             if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
#                 continue
#             keyevent("BACK")
#         for i in range (0,10):
#             pos_check = exists_any([Template(r"tpl1568948804334.png", threshold=0.8, rgb=True, record_pos=(-0.011, -0.362), resolution=(1080, 1920))])
#             if (pos_check != False):
#                 return True
#             touch(pos)
#             sleep(5)
#             pos_check = exists_any([Template(r"tpl1568948804334.png", threshold=0.8, rgb=True, record_pos=(-0.011, -0.362), resolution=(1080, 1920))])
#             if (pos_check != False):
#                 return True
#             # Todo: 处理弹出
#             if (self.Channel.skipInterstitial(isReport = isReport_Interstitial)):
#                 continue
#             keyevent("BACK")
#             pos2 = exists(Template(r"tpl1570697720179.png", record_pos=(0.004, 0.057), resolution=(1080, 1920)))
#             if (pos2 != False):
#                 keyevent("BACK")
#                 continue
#             sleep(1)

    # 回到主界面
    def backToMain(self, isReport_Interstitial = False):

        # 用回退键尝试5次
        for i in range(0, 5):
            if (not self.isInMainScreen()):
                if (isReport_Interstitial):
                    result = self.Channel.skipInterstitial(isReport = isReport_Interstitial)
                    if (result == True):
                        continue
                keyevent("BACK")
                sleep(1)
            else:
                return

        # 尝试插屏
        for i in range(0, 5):
            if (not self.isInMainScreen()):
                result = self.Channel.skipInterstitial(isReport = isReport_Interstitial)
                if (result == True):
                    continue
                keyevent("BACK")
                sleep(1)
            else:
                return


        # 重启
        if (not self.isInMainScreen()):
            self.Channel.restart()

    '''===================== 前院 ==================='''

    def goToForeyard_Setting(self, isReport_Interstitial = False):
        self.goToForeyard(isReport_Interstitial = isReport_Interstitial)
        #pos = exists_any([Template(r"tpl1565076621190.png", record_pos=(-0.356, -0.669), resolution=(1080, 2248)), Template(r"tpl1566617348874.png", record_pos=(-0.359, -0.677), resolution=(1080, 2280)), Template(r"tpl1566626742647.png", record_pos=(-0.355, -0.68), resolution=(1080, 2280)), Template(r"tpl1566627158264.png", record_pos=(-0.362, -0.68), resolution=(1080, 2280)), Template(r"tpl1566532549491.png", record_pos=(-0.352, -0.665), resolution=(1080, 2248)), Template(r"tpl1565838292440.png", threshold=0.6, rgb=True, record_pos=(-0.356, -0.638), resolution=(1080, 2248)), Template(r"tpl1566627350512.png", record_pos=(-0.357, -0.668), resolution=(1080, 2248)),Template(r"tpl1584170152443.png", record_pos=(-0.35, -0.736), resolution=(1080, 2280)),Template(r"tpl1584170166867.png", record_pos=(-0.377, -0.701), resolution=(1080, 2280))])
        pos = exists_any([Template(r"tpl1584170413590.png", record_pos=(-0.431, -0.693), resolution=(1080, 2280)),Template(r"tpl1584772720041.png", record_pos=(-0.416, -0.692), resolution=(1080, 2280)),Template(r"tpl1584772757902.png", record_pos=(-0.44, -0.688), resolution=(1080, 2280))])



#         if (pos == False):
#             self.Reporter.raise_error()
        touch(pos)
        sleep(0.5)
        pos = exists_any([Template(r"tpl1568971859496.png", record_pos=(-0.117, -0.206), resolution=(1080, 1920))])
        if (pos == False):
            self.Reporter.raise_error()

    def goToForeyard_MiniGame(self, isReport_Interstitial = False):
        self.goToForeyard(isReport_Interstitial = isReport_Interstitial)
        pos = exists_any([Template(r"tpl1565073787262.png", record_pos=(-0.365, 0.138), resolution=(1080, 2340)), Template(r"tpl1571198138950.png", record_pos=(-0.38, 0.191), resolution=(1080, 2160)),Template(r"tpl1584761650507.png", record_pos=(-0.381, 0.219), resolution=(1080, 2280))])

        if (pos == False):
            self.Reporter.raise_error()
        touch(pos)
        pos = exists_any([Template(r"tpl1568968102483.png", record_pos=(-0.001, -0.816), resolution=(1080, 1920)), Template(r"tpl1569729625234.png", record_pos=(0.0, -0.813), resolution=(1080, 1920)), Template(r"tpl1570517128204.png", record_pos=(-0.002, -0.943), resolution=(1080, 2340))])
        if (pos == False):
            self.Reporter.raise_error()

    def goToForeyard_Shop(self, isReport_Interstitial = False):
        self.goToForeyard(isReport_Interstitial = isReport_Interstitial)
        pos = exists_any([Template(r"tpl1565079474632.png", record_pos=(-0.163, -0.761), resolution=(1080, 2340)), Template(r"tpl1568970276367.png", threshold=0.8, record_pos=(-0.144, -0.644), resolution=(1080, 1920))])
        if (pos == False):
            self.Reporter.raise_error()
        touch(pos)
        sleep(1)
        pos = exists_any([Template(r"tpl1568970217292.png", record_pos=(0.002, -0.811), resolution=(1080, 1920)), Template(r"tpl1565347465512.png", record_pos=(-0.326, 0.267), resolution=(1080, 1920))])
        if (pos == False):
            self.Reporter.raise_error()

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
                self.Channel.skipInterstitial()
                keyevent("BACK")
                sleep(1)




    '''===================== 厨房 ==================='''

    def goToKitchen_Refrigerator(self, isReport_Interstitial = False):
        self.goToKitchen(isReport_Interstitial = isReport_Interstitial)
        pos = exists_any([Template(r"tpl1569037556459.png", record_pos=(0.303, -0.394), resolution=(1080, 1920))])
        if (pos == False):
            self.Reporter.raise_error()
        touch(pos)
        sleep(1)

    '''===================== 浴室 ==================='''

    def goToBathroom_AidKit(self, isReport_Interstitial = False):
        self.goToBathroom(isReport_Interstitial = isReport_Interstitial)
        pos = exists_any([Template(r"tpl1569038291685.png", record_pos=(-0.275, -0.372), resolution=(1080, 1920)), Template(r"tpl1569740048940.png", record_pos=(-0.279, -0.381), resolution=(1080, 1920))])
        if (pos == False):
            self.Reporter.raise_error()
        touch(pos)
        sleep(1)

    def goToBathroom_BathTub(self, isReport_Interstitial = False):
        self.goToBathroom(isReport_Interstitial = isReport_Interstitial)
        pos = exists_any([Template(r"tpl1569038921145.png", rgb=True, record_pos=(-0.373, 0.13), resolution=(1080, 1920)), Template(r"tpl1569056933147.png", record_pos=(-0.356, 0.055), resolution=(1080, 1920)), Template(r"tpl1570611413025.png", record_pos=(-0.34, 0.15), resolution=(720, 1440))])
        if (pos == False):
            self.Reporter.raise_error()
        touch(pos)
        sleep(1)

    '''===================== 卧室 ==================='''

    def goToBedroom_Crayon(self, isReport_Interstitial = False):
        self.goToBedroom(isReport_Interstitial = isReport_Interstitial)
        pos = exists_any([Template(r"tpl1565771637885.png", record_pos=(0.343, -0.363), resolution=(1080, 2248)), Template(r"tpl1569047245126.png", record_pos=(0.345, -0.431), resolution=(1080, 1920)), Template(r"tpl1569047262270.png", record_pos=(0.348, -0.432), resolution=(1080, 1920))])
        if (pos == False):
            self.Reporter.raise_error()
        touch(pos)
        sleep(1)

    def check_Interstitial(self):
        self.goToForeyard()
        sleep(80)

        self.goToKitchen()
        #self.Channel.skipInterstitial(isReport = True)
        sleep(80)

        self.goToBathroom()
        #self.Channel.skipInterstitial(isReport = True)
        sleep(80)

        self.goToBedroom()
        #self.Channel.skipInterstitial(isReport = True)
        sleep(80)

        self.goToBackyard()
        #self.Channel.skipInterstitial(isReport = True)




























