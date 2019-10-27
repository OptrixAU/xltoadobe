class FillColourScriptGen:
    
    def __init__(self, args):
        self.layername = args;
        pass    

    def GenerateScript(self, arg2):        
        Script = "var lyr = app.activeDocument.layers.item('" + self.layername + "');\n"
        Script += "lyr.allPageItems[0].fillColor=app.activeDocument.colors.item('" + arg2 + "');\n"
        return Script
