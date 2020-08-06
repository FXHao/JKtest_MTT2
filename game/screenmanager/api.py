# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
using(_project_root)

def new_ScreenManager(class_name, *args):
    
    if (class_name == "MTT2Screen"):
        using(_project_root + "game/screenmanager/MTT2Screen.air")
        from MTT2Screen import MTT2Screen
        result = MTT2Screen(*args)
        return result

    if (class_name == "MTTScreen"):
        using(_project_root + "game/screenmanager/MTTScreen.air")
        from MTTScreen import MTTScreen
        result = MTTScreen(*args)
        return result





