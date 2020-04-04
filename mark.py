

class Mark:

    def __init__(self):
        self.encodings= {None:'utf16','no':'no'}

    def markFile(self,mFile,parentPath,parentEncoding,childEncoding,translationArg):

        posName= parentPath.rfind('/') + 1
        if posName != 0:
            parentName= parentPath[posName:]

        parentEn= self.encodings[parentEncoding]
        childEn= self.encodings[childEncoding]

        mFile.write("#Translated from: " + parentName + " from: ")
        mFile.write("\n\n")


