class ScriptPlatformScriptGen:
    
    def __init__(self):        
        pass    

    def GenerateScriptStart(self):        
        Script = "var filePath = activeDocument.fullName.path;\r\n"
        #Script += "var newDoc = app.activeDocument.duplicate();\r\n"
        #Script += "app.activeDocument = newDoc;\r\n"        

        return Script
        
    def GenerateCardEnd(self, sheet, row):
        Script = "var pngExportOpts = new ExportOptionsPNG24();\r\n"
        Script += "\r\n"
        Script += 'var savePath = File(filePath + "/' + str(sheet.cell_value(row,0)).replace(".","") + '.png");' + "\r\n"
        Script += "pngExportOpts.antiAliasing = true;\r\n"
        Script += "pngExportOpts.artBoardClipping = true;\r\n"
        Script += "pngExportOpts.horizontalScale = 100.0;\r\n"
        Script += "pngExportOpts.transparency = true;\r\n"
        Script += "pngExportOpts.verticalScale = 100.0;\r\n"
        Script += "app.activeDocument.exportFile( savePath, ExportType.PNG24, pngExportOpts );\r\n"
                    
        return Script
    
    def GenerateScriptEnd(self):
        return "app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);\r\n"
