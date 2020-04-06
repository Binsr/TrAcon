import pfReader
import mark


class Pfile:

    def __init__(self,pathToDir,filename):
        self.pathToDir= pathToDir
        self.filename= filename

        info = self.getInfo(pathToDir + '/' + filename)
        self.parentName= info[0]
        self.parentEncoding= [1]
        self.encoding= info[2]
        self.file= open(pathToDir + '/' + filename,'r')
        self.reader= pfReader.pfReder(self.file)


    def getInfo(self,path):
        markH= mark.Mark()
        info = markH.getInfo(path)
        info[1] = markH.decodeEn(info[1])
        info[2] = markH.decodeEn(info[2]) # ZA PREPRAVITI

        return info

    def readNext(self):
        return self.reader.readNext()
