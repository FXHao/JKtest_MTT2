# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
from airtest.core.android.android import Android
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../..")) + "/"
auto_setup(__file__)
using(_project_root)
from TestManager.TestMasterManager import MasterManager


'''
m_MasterManager = MasterManager()
m_MasterManager.config(config_file = "config.ini")
m_MasterManager.print_test_list()
m_MasterManager.run_test()

m_MasterManager.TestSummarize_print()
m_MasterManager.LogToFile()
'''
# devs = device()
# print(devs.list_app(third_only=True))
#clear_app()
#start_app("com.outfit7.mytalkingtom2.nearme.gamecenter")

m_MasterManager = MasterManager()
m_MasterManager.config(config_file = "config.ini")
m_MasterManager.print_test_list()
m_MasterManager.run_test()
#m_MasterManager.TestSummarize_print()
#m_MasterManager.LogToFile()

