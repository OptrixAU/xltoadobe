class FillColourScriptGen:
    
    def __init__(self, args):
        self.layername = args;
        pass    

    def GenerateScript(self, arg2):
        bits = arg2.split(',')
        numbers = (float(bits[0]),float(bits[1]),float(bits[2]),float(bits[3]),float(bits[4]))

        cyan = f'{numbers[0]:9.5f}'
        magenta = f'{numbers[1]:9.5f}'
        yellow = f'{numbers[2]:9.5f}'
        black = f'{numbers[3]:9.5f}'
        opacity = f'{numbers[4]:9.5f}'
        
        Script = "var lyr = app.activeDocument.layers.getByName('" + self.layername + "');\n"
        Script += "var col = new CMYKColor(); \ncol.black=" + black + ";\ncol.cyan=" + cyan + ";\ncol.magenta=" + magenta + ";\ncol.yellow=" + yellow + ";\n"
        Script += "lyr.pageItems[0].filled=true;\n"
        Script += "lyr.pageItems[0].fillColor=col;\n"
        return Script
