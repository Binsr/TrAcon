import pfReader
import mark

class Pfile:

    def __init__(self,pathToDir,filename):
        self.fullPath= pathToDir + '/' + filename

        self.pathToDir= pathToDir
        self.filename= filename

        self.parentName= None
        self.parentEncoding= None
        self.encoding= None
        self.optionArg= None #za izmenu da ne bude argument nego da bude

        self.fileAction= None

        self.setInfo(pathToDir + '/' + filename)

        self.file= open(pathToDir + '/' + filename,'r')
        self.reader= pfReader.pfReder(self.file)


    def setInfo(self,path):
        markH= mark.Mark()
        info = markH.getInfo(path)
        if len(info) != 5:
            return

        info[1] = markH.decodeEn(info[1])
        info[2] = markH.decodeEn(info[2]) # ZA PREPRAVITI
        self.parentName= info[0]
        self.parentEncoding= info[1]
        self.encoding= info[2]
        if info[3] == 'Translated':
            self.fileAction= 't'
        else:
            self.fileAction= 'c'

        self.optionArg= info[4]

    def readNext(self):
        line= self.reader.readNext()
        if line is False:
            self.file.close()
        return line

    def getFileAction(self):
        return self.fileAction

    def getParentName(self):
        return self.parentName

    def getOptionArg(self):
        return self.optionArg

    def getPathToDir(self):
        return self.pathToDir

    def getEn(self):
        return self.encoding

    def getParEn(self):
        return self.parentEncoding

    def getFullPath(self):
        return self.fullPath

    def getName(self):
        return self.filename

    def reload(self):
        self.file.close()
        self.file= open(self.fullPath,'r')
        self.reader= pfReader.pfReder(self.file)