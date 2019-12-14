import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import buss.model1
import tool.model1

buss.model1.project_info()
tool.model1.tool_info()
