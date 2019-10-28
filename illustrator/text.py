class TextScriptGen:
    
    def __init__(self, args):
        self.layername = args
        pass    

    def GenerateScript(self, arg2):
        if not isinstance(arg2, str):
            arg2 = str(int(arg2))
        Script = "var found = false;\n"
        Script += "for (i=0;i<app.activeDocument.layers.length;i++)\n"
        Script += "{\n"	
        Script += "  if (app.activeDocument.layers[i].name == '" + self.layername + "')\n"
        Script += "  {\n"
        Script += "    app.activeDocument.layers[i].textFrames[0].contents = '" + arg2.replace("\n","\\r") + "';\n"
        Script += "    found = true;\n"
        Script += "  }\n"
        Script += "}\n"
        
        Script += "if (found == true) { for (i=0;i<app.activeDocument.textFrames.length;i++)\n"
        Script += "{\n"	
        Script += "  if (app.activeDocument.textFrames[i].contents == '" + self.layername + "')\n"
        Script += "  {\n"
        Script += "    app.activeDocument.textFrames[i].contents = '" + arg2.replace("\n","\\r") + "';\n"
        Script += "  }\n"
        Script += "}; };\n"
        return Script

    def CleanupScript(self, arg2):
        if not isinstance(arg2, str):
            arg2 = str(int(arg2))
        Script = "for (i=0;i<app.activeDocument.textFrames.length;i++)\n"
        Script += "{\n"	
        Script += "  if (app.activeDocument.textFrames[i].contents == '" + arg2.replace("\n","\\r") + "')\n"
        Script += "  {\n"
        Script += "    app.activeDocument.textFrames[i].contents = '" + self.layername + "';\n"
        Script += "  }\n"
        Script += "}\n"
        return Script
