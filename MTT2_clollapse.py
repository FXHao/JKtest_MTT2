# # -*- encoding=utf8 -*-
# __author__ = "fanxiaohao"
#
# from airtest.core.api import *
#
# import logging
#
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)
#
# auto_setup(__file__)
#
#
# class CheckCollapse(object):
#     '''检测MTT2崩溃率'''
#
#     def __init__(self):
#         self.app_packagename = 'com.tencent.tmgp.mytalkingtom2'
#         self.app = device()
#         self.start_num = 0
#         self.collapse_num = 0
#
#     def output(self):
#         '''输出'''
#         print('***************启动APP次数：【{}】*******************'.format(self.start_num))
#         print('***************崩溃次数:【{}】***********************'.format(self.collapse_num))
#         print('***************崩溃率为：【{}%】**********************'.format((self.collapse_num * 100 / self.start_num)))
#
#     def login(self):
#         '''登录操作'''
#         wait(Template(r"tpl1594182982780.png", record_pos=(0.006, 0.875), resolution=(1200, 2640)))
#         sleep(1)
#         touch((322, 2401))
#         sleep(1)
#         wait(Template(r"tpl1594183068639.png", record_pos=(0.007, 0.224), resolution=(1200, 2640)))
#         sleep(1)
#         touch((589, 2342))
#         sleep(1)
#         wait(Template(r"tpl1594183146750.png", record_pos=(0.0, -0.133), resolution=(1200, 2640)), timeout=5)
#         sleep(1)
#         touch((1094, 254))
#         sleep(1)
#
#     def check_app(self):
#         '''检测APP进程是否存在'''
#         try:
#             # 判断APP进程是否存在
#             str = 'ps|grep ' + self.app_packagename
#             self.app.shell(str)
#         except:
#             # 不存在报错
#             self.collapse_num += 1
#             # 获取日志
#             with open('./logcat_path_{}.txt'.format(self.start_num), 'wb') as f:
#                 for x in self.app.logcat(grep_str=self.app_packagename):
#                     f.write(x)
#
#     def main(self):
#         '''操作步骤'''
#         while (True):
#             start_app(self.app_packagename)
#             self.start_num += 1
#             try:
#                 # 第一次登录
#                 self.login()
#                 # 第二次登录
#                 self.login()
#             except:
#                 self.check_app()
#             finally:
#                 stop_app(self.app_packagename)
#                 sleep(30)
#
# MTT2 = CheckCollapse()
# MTT2.main()
#
# -*- encoding=utf8 -*-
__author__ = "fanxiaohao"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# airtest.core.api中包含了一个名为ST的变量，即为全局设置

# from airtest.core.settings import Settings as ST

# import os
# # 下一个操作需要等待多少秒（默认0.1s）
# ST.OPDELAY = 1
# # 修改阈值，（默认0.6，越高识别越精确）
# ST.THRESHOLD = 0.75

auto_setup(__file__)

class CheckCollapse(object):
    '''检测MTT2崩溃率'''

    def __init__(self):
        self.app_packagename = 'com.tencent.tmgp.mytalkingtom2'
        self.app = device()
        self.start_num = 0
        self.collapse_num = 0

    def output(self):
        '''输出'''
        print('***************启动APP次数：【{}】*******************'.format(self.start_num))
        print('***************崩溃次数:【{}】***********************'.format(self.collapse_num))
        print('***************崩溃率为：【{}%】**********************'.format((self.collapse_num * 100 / self.start_num)))

    def login(self):
        '''登录操作'''
        wait(Template(r"tpl1594182982780.png", record_pos=(0.006, 0.875), resolution=(1200, 2640)))
        sleep(2)
        touch((154,836))
        sleep(2)
        wait(Template(r"tpl1594183068639.png", record_pos=(0.007, 0.224), resolution=(1200, 2640)))
        sleep(2)
        touch((287,817))
        sleep(2)
        wait(Template(r"tpl1594183146750.png", record_pos=(0.0, -0.133), resolution=(1200, 2640)), timeout=5)
        sleep(2)
        touch((481,51))
        sleep(2)

    def check_app(self):
        '''检测APP进程是否存在'''
        try:
            # 判断APP进程是否存在
            str = 'ps|grep ' + self.app_packagename
            self.app.shell(str)
        except:
            # 不存在就报错
            self.collapse_num += 1
            # 获取日志
            with open('./logcat_path_{}.txt'.format(self.start_num), 'wb') as f:
                for x in self.app.logcat(grep_str=self.app_packagename):
                    f.write(x)

    def main(self):
        '''操作步骤'''
        while (True):
            #             wake()
            start_app(self.app_packagename)
            self.start_num += 1
            try:
                # 第一次登录
                self.login()
                # 第二次登录
                self.login()
            except:
                self.check_app()
            finally:
                stop_app(self.app_packagename)
                self.app.shell('adb logcat -c')
                sleep(30)

MTT2 = CheckCollapse()
MTT2.main()
