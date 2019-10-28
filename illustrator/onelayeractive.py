class OneLayerActiveScriptGen:
    
    def __init__(self, args):
        self.valid = args.split('|')
        pass    

    def GenerateScript(self, arg2):        
        if len(self.valid) == 1:
            #OK, this uses sub-layers
            Script = "for (i=0;i<app.activeDocument.layers.length;i++)\n"
            Script += "{\n"
            for vl in self.valid:
                Script += "  lyr = app.activeDocument.layers[i];\n"
                Script += "   if (lyr.name == '" + self.valid[0] + "') {"
                Script += "     for (q=0;q<lyr.layers.length;q++) {\n"
                Script += "        if (lyr.layers[q].name == '" + arg2 + "')\n"
                Script += "           lyr.layers[q].visible = true;\n"
                Script += "        else\n"
                Script += "           lyr.layers[q].visible = false;\n"
                Script += " }; };\n"
            Script += "}\n"
        else:
            #This has a list of the layers we are going to use.
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
