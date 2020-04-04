import pfhandle
import pfReader
import os
import pfReader
import pfhandle
import translator

class UpdateHandle:

    def __init__(self): #ako hoces kasnije rekurzivno ili nesto onda je bolje da se etuje preko update funkcije
        self.path= None
        self.parentFilePath= None

    def updateDir(self, path, parentFilePath):
        self.path= path
        self.parentFilePath= parentFilePath

        posOfName=  parentFilePath.rfind('/')+1
        parentFileName= parentFilePath[posOfName:]

        for filename in os.listdir(path):
            if not filename.endswith(".properties") or filename == parentFileName:
                continue
            if self.getParentName(filename) != parentFileName:
                continue
            self.updateFile(path + '/' + filename)

    def getParentName(self,filename):
        file= open(self.path + '/' + filename,'r')
        mark= file.readline()
        parentName= mark[18:33]
        file.close()
        return parentName #Neka bude regex


    def updateFile(self,filePath):

        handleP= pfhandle.PFhandle(None,None,'eng-fran') #Ovo mora da bude promenjivog tipa

        cFile= open(filePath,'r')
        pFile= open(self.parentFilePath,'r')
        rFile= open(self.path + '/tmp.properties','w')

        readerP= pfReader.pfReder(pFile)
        readerC= pfReader.pfReder(cFile)

        while True:
            cLine= readerC.readNext()
            if cLine is False:
                break

            if cLine['type'] == 'comment':
                rFile.write(cLine['value'])
            if cLine['type'] == 'property':
                if not cLine['value']['string'].isspace():
                    rFile.write(cLine['value']['property'] + cLine['value']['string'])
                    rFile.write('\n\n')
                else: #MALO LESPE OVO PREPRAVI
                    while True:
                        pLine= readerP.readNext()
                        if pLine['type'] == 'property':
                            if pLine['value']['property'] == cLine['value']['property']:
                                rFile.write(pLine['value']['property'] + " ")
                                rFile.write(handleP.translateLine(pLine['value']['string'],'no','no')) #ISTO PROMENJIVOG TIPA
                                rFile.write("\n\n")
                                break
        rFile.close()
        pFile.close()
        rFile.close() #Dodaj da se prethodni fajl brise a tmp preimenuje u njegovo ime

        return


    #KLASA READ FILE KOJA ZNA KAKO DA CITA PROP I TAKO TO I DA IMA FUNCKIJU GET