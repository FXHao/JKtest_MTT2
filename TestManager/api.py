# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
# project_root = os.path.dirname(os.path.abspath(__file__) + "/../../")
using(os.path.abspath(os.path.join(os.path.abspath(__file__), "..")))
from TestReporter import TestReporter

Reporter = None

def config_reporter(input_Reporter):
    Reporter = input_Reporter

def report(msg, isRaiseError = False):
    Reporter.report(msg, isRaiseError = False)
