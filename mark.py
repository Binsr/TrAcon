import re

class Mark:

    def __init__(self):
        self.encodings= {None:'utf16','no':'no'}
        self.decoded= {'utf16': None,'no':'no'}

    def markFile(self,mFile,parentPath,parentEncoding,childEncoding,translationArg,actionPref):
        parentName= None
        posName= parentPath.rfind('/') + 1
        if posName != 0:
            parentName= parentPath[posName:]

        parentEn= self.encodings[parentEncoding]
        childEn= self.encodings[childEncoding]

        mFile.write("#Parent: {" + parentName + '} '
        'parent encoding: {' + self.encodings[parentEncoding] + '} '
        'child encoding: {' + self.encodings[childEncoding] + '} Action preformed: '
        + '{' + actionPref + '} Language: ' + '{' + translationArg + '}')
        mFile.write("\n\n")

    def getInfo(self,filename):

        file= open(filename,'r')
        line= file.readline()
        pattern = re.compile(r'{(.*?)}')
        file.close()

        values= re.findall(pattern, line)
        return values

    def decodeEn(self,en):
        return self.decoded[en]



