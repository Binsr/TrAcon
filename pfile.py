import pfReader
import mark


class Pfile:

    def __init__(self,pathToDir,filename):
        self.pathToDir= pathToDir
        self.filename= filename

        self.parentName= None
        self.parentEncoding= None
        self.encoding= None
        self.transArg= None #za izmenu da ne bude argument nego da bude

        self.setInfo(pathToDir + '/' + filename)

        self.file= open(pathToDir + '/' + filename,'r')
        self.reader= pfReader.pfReder(self.file)


    def setInfo(self,path):
        markH= mark.Mark()
        info = markH.getInfo(path)
        if len(info) != 4:
            return

        info[1] = markH.decodeEn(info[1])
        info[2] = markH.decodeEn(info[2]) # ZA PREPRAVITI
        self.parentName= info[0]
        self.parentEncoding= info[1]
        self.encoding= info[2]
        self.transArg= info[3]

    def readNext(self):
        return self.reader.readNext()

    def getParentName(self):
        return self.parentName

    def getTransArg(self):
        return self.transArg