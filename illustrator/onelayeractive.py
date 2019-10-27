class OneLayerActiveScriptGen:
    
    def __init__(self, args):
        self.valid = args.split('|')
        pass    

    def GenerateScript(self, arg2):        
        Script = "for (i=0;i<app.activeDocument.layers.length;i++)\n"
        Script += "{\n"
        for vl in self.valid:
            Script += "  if (app.activeDocument.layers[i].name == '" + vl + "') {\n"
            Script += " if (app.activeDocument.layers[i].name == '" + arg2 + "')\n"
            Script += "    app.activeDocument.layers[i].visible = true;\n"
            Script += "  else\n"
            Script += "    app.activeDocument.layers[i].visible = false;\n"
            Script += " };\n"
        Script += "}\n"
        return Script
