class OneLayerActiveScriptGen:
    
    def __init__(self, args):
        self.valid = args.split('|')
        pass    

    def GenerateScript(self, arg2):
        Script = ""
        for vl in self.valid:
            Script += "app.activeDocument.layers.item('" + vl + "').visible = false;\n"

        Script += "app.activeDocument.layers.item('" + arg2 + "').visible = true;\n"        
        return Script
