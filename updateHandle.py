import os
import pfReader
import pfhandle
import mark
import pfile

class UpdateHandle:

    def __init__(self):
        pass

    def updateDir(self, path, parentPath):

        startPos = parentPath.rfind('/') + 1
        parentName= parentPath[startPos:]

        parentFile= pfile.Pfile(path,parentName) #TREBA DA SE RESETUJE ITERATOR U PROP DA KRECE OD POCETKA!

        childs= self.generateChildsArr(path,parentName)

        for file in childs:
            parentFile.reload()
            self.updateFile(file,parentFile)


    def generateChildsArr(self, path, parentName):

        filesArr = []  # Niz fajlova ciji je parent prozledjeni parent

        for filename in os.listdir(path):
            if not filename.endswith(".properties") or filename == parentName:
                continue

            filesArr.append(pfile.Pfile(path, filename))
            if filesArr[-1].getParentName() != parentName:
                filesArr.pop()

        return filesArr

    def updateFile(self,child,parent):

        edtranslator= pfhandle.PFhandle(None,None,child.getTransArg()) #pf handle for encoding/decoding translation
        tmpPath= child.getPathToDir()+ '/' + 'tmp.properties'
        tmpFile= open(tmpPath,'w')

        while True:
            childLine= child.readNext()

            if childLine is False:
                break

            if childLine['type'] == 'comment':
                tmpFile.write(childLine['value'])
                continue

            if childLine['type'] != 'property':
                continue

            parentLine= parent.readNext() #OVA  IDEJA DA BI RADILA MORAJU ISTI REDOSLEDI PROPERTY DA BUDU U OBA FAJLA!
            while parentLine['type'] != 'property':
                parentLine= parent.readNext()

            #OVDE DODATI USLOV za (edit) property
            

            if not childLine['value']['string'].isspace():
                tmpFile.write(childLine['value']['property'] + childLine['value']['string'])
                tmpFile.write('\n\n')
                continue

            str= parentLine['value']['string']
            translatedLine= edtranslator.translateLine(str,child.getEn(),child.getParEn())
            tmpFile.write(parentLine['value']['property'] + " " + translatedLine)
            tmpFile.write('\n\n')

        tmpFile.close()
        os.remove(child.getFullPath())
        os.rename(tmpPath,child.getFullPath())
        print(child.getFullPath() + " :Updated")



