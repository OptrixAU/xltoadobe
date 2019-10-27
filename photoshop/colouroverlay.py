class ColourOverlayScriptGen:
    
    def __init__(self, args):
        self.layer = args
        pass    

    def GenerateScript(self, arg2):
        bits = arg2.split(',')
        numbers = (float(bits[0]),float(bits[1]),float(bits[2]),float(bits[3]),float(bits[4]))

        cyan = f'{numbers[0]:9.5f}'
        magenta = f'{numbers[1]:9.5f}'
        yellow = f'{numbers[2]:9.5f}'
        black = f'{numbers[3]:9.5f}'
        opacity = f'{numbers[4]:9.5f}'
                
        script = "//Change colour overlay for the chosen layer...\r\n"
        script += "app.activeDocument.activeLayer = app.activeDocument.layers.getByName('" + self.layer + "');\r\n"
        script += 'var idsetd = charIDToTypeID( "setd" );' + "\r\n"
        script += 'var desc17 = new ActionDescriptor();' + "\r\n"
        script += 'var idnull = charIDToTypeID( "null" );' + "\r\n"
        script += 'var ref5 = new ActionReference();' + "\r\n"
        script += 'var idPrpr = charIDToTypeID( "Prpr" );' + "\r\n"
        script += 'var idLefx = charIDToTypeID( "Lefx" );' + "\r\n"
        script += 'ref5.putProperty( idPrpr, idLefx );' + "\r\n"
        script += 'var idLyr = charIDToTypeID( "Lyr " );' + "\r\n"
        script += 'var idOrdn = charIDToTypeID( "Ordn" );' + "\r\n"
        script += 'var idTrgt = charIDToTypeID( "Trgt" );' + "\r\n"
        script += 'ref5.putEnumerated( idLyr, idOrdn, idTrgt );' + "\r\n"
        script += 'desc17.putReference( idnull, ref5 );' + "\r\n"
        script += 'var idT = charIDToTypeID( "T   " );' + "\r\n"
        script += 'var desc18 = new ActionDescriptor();' + "\r\n"
        script += 'var idScl = charIDToTypeID( "Scl " );'
        script += 'var idPrc = charIDToTypeID( "#Prc" );'
        script += 'desc18.putUnitDouble( idScl, idPrc, 416.666667 );'
        script += 'var idSoFi = charIDToTypeID( "SoFi" );' + "\r\n"
        script += 'var desc19 = new ActionDescriptor();' + "\r\n"
        script += 'var idenab = charIDToTypeID( "enab" );' + "\r\n"
        script += 'desc19.putBoolean( idenab, true );' + "\r\n"
        script += 'var idpresent = stringIDToTypeID( "present" );' + "\r\n"
        script += 'desc19.putBoolean( idpresent, true );' + "\r\n"
        script += 'var idshowInDialog = stringIDToTypeID( "showInDialog" );' + "\r\n"
        script += 'desc19.putBoolean( idshowInDialog, true );' + "\r\n"
        script += 'var idMd = charIDToTypeID( "Md  " );' + "\r\n"
        script += 'var idBlnM = charIDToTypeID( "BlnM" );' + "\r\n"
        script += 'var idNrml = charIDToTypeID( "Nrml" );' + "\r\n"
        script += 'desc19.putEnumerated( idMd, idBlnM, idNrml );' + "\r\n"
        script += 'var idClr = charIDToTypeID( "Clr " );' + "\r\n"
        script += 'var desc20 = new ActionDescriptor();' + "\r\n"
        script += 'var idCyn = charIDToTypeID( "Cyn " );' + "\r\n"
        script += 'desc20.putDouble( idCyn, ' + cyan + ' );' + "\r\n"
        script += 'var idMgnt = charIDToTypeID( "Mgnt" );' + "\r\n"
        script += 'desc20.putDouble( idMgnt, ' + magenta + ' );' + "\r\n"
        script += 'var idYlw = charIDToTypeID( "Ylw " );' + "\r\n"
        script += 'desc20.putDouble( idYlw, ' + yellow + ' );' + "\r\n"
        script += 'var idBlck = charIDToTypeID( "Blck" );' + "\r\n"
        script += 'desc20.putDouble( idBlck, ' + black + ' );' + "\r\n"
        script += 'var idCMYC = charIDToTypeID( "CMYC" );' + "\r\n"
        script += 'desc19.putObject( idClr, idCMYC, desc20 );' + "\r\n"
        script += 'var idOpct = charIDToTypeID( "Opct" );'
        script += 'var idPrc = charIDToTypeID( "#Prc" );'
        script += 'desc19.putUnitDouble( idOpct, idPrc, ' + opacity + ' );'
        script += 'var idSoFi = charIDToTypeID( "SoFi" );'
        script += 'desc18.putObject( idSoFi, idSoFi, desc19 );'
        script += 'var idLefx = charIDToTypeID( "Lefx" );'
        script += 'desc17.putObject( idT, idLefx, desc18 );'
        script += 'executeAction( idsetd, desc17, DialogModes.NO )' + "\r\n"
        return script
