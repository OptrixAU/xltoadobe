class ScriptPlatformScriptGen:
    
    def __init__(self):        
        pass    

    def GenerateScriptStart(self):        
        Script = "var filePath = app.activeDocument.fullName.path;\r\n"
        #Script += "var newDoc = app.activeDocument.duplicate();\r\n"
        #Script += "app.activeDocument = newDoc;\r\n"        

        return Script
        
    def GenerateCardEnd(self, sheet, row):
        Script = 'app.jpegExportPreferences.exportResolution = 300;app.jpegExportPreferences.jpegQuality = JPEGOptionsQuality.HIGH;\n'
        Script += 'var savePath = File(filePath + "/' + sheet.cell_value(row,0).replace(".","") + '.jpg");app.activeDocument.exportFile(ExportFormat.JPG, savePath,false);\n'
        return Script
    
    def GenerateScriptEnd(self):
        return "app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);\r\n"
