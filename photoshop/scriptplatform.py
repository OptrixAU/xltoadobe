class ScriptPlatformScriptGen:
    
    def __init__(self):        
        pass    

    def GenerateScriptStart(self):
        Script = "var layers = null;\r\n"
        Script += "var filePath = activeDocument.fullName.path;\r\n"
        Script += "var newDoc = app.activeDocument.duplicate();\r\n"
        Script += "app.activeDocument = newDoc;\r\n"
        #Script += "app.activeDocument.bringToFront();\r\n"

        Script += 'var idCnvM = charIDToTypeID( "CnvM" );' + "\n"
        Script += 'var desc89 = new ActionDescriptor();' + "\n"
        Script += 'var idT = charIDToTypeID( "T   " );' + "\n"
        Script += 'var idRGBM = charIDToTypeID( "RGBM" );' + "\n"
        Script += 'desc89.putClass( idT, idRGBM );' + "\n"
        Script += 'var idMrge = charIDToTypeID( "Mrge" );' + "\n"
        Script += 'desc89.putBoolean( idMrge, false );' + "\n"
        Script += 'var idRstr = charIDToTypeID( "Rstr" );' + "\n"
        Script += 'desc89.putBoolean( idRstr, false );' + "\n"
        Script += 'executeAction( idCnvM, desc89, DialogModes.NO );' + "\n"
        return Script
        
    def GenerateCardEnd(self, sheet, row):
        Script = '// Save Image' + "\r\n"
        Script += 'pngOptions = new PNGSaveOptions();' + "\r\n"
        Script += 'pngOptions.compression = 0;' + "\r\n"
        Script += 'pngOptions.interlaced = false;' + "\r\n"
        Script += '' + "\r\n"    
        Script += 'savePath = File(filePath + "/' + sheet.cell_value(row,0).replace(".","") + '.png");' + "\r\n"
        Script += '' + "\r\n"    
        Script += 'app.activeDocument.saveAs(savePath, pngOptions, true, Extension.LOWERCASE);' + "\r\n"
        Script += '' + "\r\n"
        return Script
    
    def GenerateScriptEnd(self):
        return "app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);\r\n"
