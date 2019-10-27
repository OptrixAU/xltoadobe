class OneLayerActiveScriptGen:
    
    def __init__(self, args):
        layernames = args.split(':')
        self.lgroups = "app.activeDocument.layerSets.getByName('" + layernames[0] + "')"
        if len(layernames) > 1:
            for x in range(1,len(layernames)):
                self.lgroups = self.lgroups + ".layerSets.getByName('" + layernames[x] + "')"                
        pass    

    def GenerateScript(self, arg2):
        script = "var sets = " + self.lgroups + ";\n"
        script += "for(x=0;x<sets.layers.length;x++){sets.layers[x].visible = false;}\n"
        if arg2 != "":
            script += "sets.layers.getByName('" + arg2+ "').visible = true;\n"
        return script
