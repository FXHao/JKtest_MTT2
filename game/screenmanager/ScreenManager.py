# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
from abc import ABC,abstractmethod

class ScreenManager(ABC):
    
    MasterManager = None
    
    poco = None
    AppID = None
    Game = None
    Channel = None
    Reporter = None
    
    def __init__(self, MasterManager):
        self.MasterManager = MasterManager
    
    def config(self):
        self.poco = self.MasterManager.poco
        self.AppID = self.MasterManager.AppID
        self.Game = self.MasterManager.Game
        self.Channel = self.MasterManager.Channel
        self.Reporter = self.MasterManager.Reporter
    

    
    
    
    
    
    






