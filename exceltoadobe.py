import xlrd
import sys
import os
import importlib
from pathlib import Path
import traceback
import argparse

parser = argparse.ArgumentParser(description='Prepares Print-At-Home Card Games for Printing',fromfile_prefix_chars="@")
parser.add_argument('name', default="workbook.xlsx", help='The name of the excel file')
parser.add_argument('platform', default="photoshop", help='The name of the product you want to automate')
args = parser.parse_args()

wb = xlrd.open_workbook(args.name + ".xlsx") 
sheet = wb.sheet_by_index(0) 
#sheet.cell_value(0, 0) 
  
nrows = sheet.nrows
ncols = sheet.ncols

colmodes = []
colactors = []

#Collect column info
for x in range(0,ncols):    
    colmodes.append((sheet.cell_value(0,x),sheet.cell_value(1,x)))

#Find out which unique modules we will need to import
modules = []
for mod in colmodes:
    if mod[0] not in modules:
        modules.append(mod[0])

loadedmodules = {}

includefolder = os.getcwd() + os.path.sep + args.platform
print("Adding Path: " + includefolder)
sys.path.append(includefolder)
module = importlib.import_module("scriptplatform")
class_ = getattr(module, "ScriptPlatformScriptGen")
platform = class_()

#Load each required module
for mod in modules:
    try:
        module = importlib.import_module(mod.lower())
        loadedmodules[mod] = module
    except:
        print("Unable to find module '" + mod + "' - Processing Stopped")
        traceback.print_exc()
        sys.exit(-1)

#Create new instances for each column
for col in colmodes:
    try:
        class_ = getattr(loadedmodules[col[0]], col[0]+"ScriptGen")
        instance = class_(col[1])
        colactors.append(instance)
    except:
        print("Unable to initialise column type: " + col[1] + " / " + col[0])
        traceback.print_exc()
        sys.exit(-1)

Script = platform.GenerateScriptStart()

#Run the instances for each row...
for row in range(2,nrows):
    colno = -1
    for cl in colactors:
        colno = colno + 1
        Script = Script + colactors[colno].GenerateScript(sheet.cell_value(row,colno))
        
    Script += platform.GenerateCardEnd(sheet, row)

    colno = -1
    for cl in colactors:
        colno = colno + 1
        try:
            Script = Script + colactors[colno].CleanupScript(sheet.cell_value(row,colno))
        except:
            pass

Script += platform.GenerateScriptEnd()

f = open(args.name + ".jsx", "w")
f.write(Script)
f.close()
