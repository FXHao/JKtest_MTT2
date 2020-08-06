# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../..")) + "/"
using(_project_root)

class TestReporter:
    
    MasterManager = None
    
    def __init__(self, MasterManager):
        self.MasterManager = MasterManager

    def report(self, msg, isRaiseError = False, isReport_caller = True):
        
        if (isReport_caller == False):
            return
        
        self.MasterManager.curCase.Message += msg + "\n"
        snapshot(msg = msg)
        assert_equal(True, (not isRaiseError), msg = msg)

    def raise_error(self, msg = "Should not be here"):
        self.report(msg = msg, isRaiseError = True)



