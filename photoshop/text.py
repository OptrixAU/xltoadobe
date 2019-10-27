class TextScriptGen:
    
    def __init__(self, args):
        self.layername = args
        pass    

    def GenerateScript(self, arg2):
        if not isinstance(arg2, str):
            arg2 = str(int(arg2))
        st = "//Text Replacement\n"
        st += "layers = app.activeDocument.layers;\n"
        st += "for (var i =0; i<layers.length; i++) {\n"
        st += "   if (layers[i].name == '" + self.layername + "') {\n"
        st += "      layers[i].textItem.contents = '" + arg2.replace("\n","\\r") + "';\n"
        st += "} }\n"
        return st
