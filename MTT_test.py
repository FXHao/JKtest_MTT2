# -*- encoding=utf8 -*-
__author__ = "acer"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 设置日志显示等级
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

class Gamecheck(object):
    '''
    测试
    '''
    def __init__(self):
        self.packagename = 'com.outfit7.mytalkingtomfree.HUAWEI:id/'
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        self.banner = None
        self.interstitial = None
        self.video = None
        self.mag_path = ''

    def banner_exists(self):
        '''
        检查普通banner
        :return: 存在banner返回True
        '''
        bannername = self.packagename + 'hiad_banner_image_1'
        # 元素存在返回true，不存在返回False
        self.banner = self.poco(bannername).wait(6).exists()
        return self.banner

    def interstitial_exists(self):
        '''
        检测原生插屏
        :return: 存在返回1
        '''
        interstitialname = self.packagename + 'interstitial_layout'
        self.interstitial = self.poco(interstitialname).wait(2).exists()
        return self.interstitial

    def video_exists(self):
        '''
        检测视频广告
        :return: 存在返回True
        '''
        vieoname = self.packagename + 'reward_content_area'
        self.video = self.poco(vieoname).wait(2).exists()
        return self.video

    # 各个界面检测
    def index(self):
        '''
        检查4个主界面
        :return:
        '''




if __name__ == '__main__':
    MTT = Gamecheck()
    print(MTT.checkbanner())