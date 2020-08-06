# -*- coding: utf-8 -*-
# -*- encoding=utf8 -*-
# __author__ = "acer"
#
# from airtest.core.api import *
#
# auto_setup(__file__)
#
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 设置日志显示等级
# import logging
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

# class Gamecheck(object):
#     '''
#     测试
#     '''
#     def __init__(self):
#         self.packagename = 'com.outfit7.mytalkingtomfree.HUAWEI:id/'
#         self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#         self.banner = None
#         self.interstitial = None
#         self.video = None
#         self.mag_path = ''
#
#     def isBannerexists(self):
#         '''
#         检测banner是否存在
#         :return:
#         '''
#         # 原生
#         icon_id = 'com.outfit7.mytalkingangelafree.nearme.gamecenter:id/icon'
#         detail = 'com.outfit7.mytalkingangelafree.nearme.gamecenter:id/detail'
#         close_di = 'com.outfit7.mytalkingangelafree.nearme.gamecenter:id/close'
#
#
#     def isInterstitialexists(self):
#         '''
#         检测插屏是否存在
#         :return:
#         '''
#         # 普通
#         image_id = 'android.widget.ImageView'
#
#         # 视频
#         video_id = 'android.view.View'

# -*- encoding=utf8 -*-
__author__ = "fanxiaohao"

from airtest.core.api import *

import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


auto_setup(__file__)

num = 0

def check_inte():
    # 视频
    if poco('android:id/content').wait(3).exists():
        snapshot(filename=r'D:\\Users\\Desktop\\MTA\\mag\{}.jpg'.format(num))
        if poco('android.widget.TextView', touchable=true, enabled=true).wait(5).exists():
            poco('android.widget.TextView', touchable=true, enabled=true).click()
        else:
            poco(text = '跳过').click()
        poco('com.outfit7.mytalkingangelafree.nearme.gamecenter:id/tt_insert_express_dislike_icon_img').click()
    # 普通插屏
    elif poco('android.widget.ImageView').wait(3).exists():
        snapshot(filename=r'D:\\Users\\Desktop\\MTA\\mag\{}.jpg'.format(num))
        poco('android.widget.ImageView', touchable='true', enabled='true').click()

    else:
        snapshot(filename=r'D:\\Users\\Desktop\\MTA\\mag\{}.jpg'.format(num))

def playgame():
    touch((88,2209))
    sleep(3)
    check_inte()
    sleep(20)
    touch((500,2202))
    check_inte()
    sleep(20)

while(True):
    playgame()


